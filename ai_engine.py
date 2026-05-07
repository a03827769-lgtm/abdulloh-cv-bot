import logging
from openai import AsyncOpenAI
from config import GROQ_API_KEY, DEEPSEEK_API_KEY
from content import CV_DATA
import os

client = AsyncOpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

USER_HISTORY = {}
MAX_HISTORY = 12

def get_system_prompt(lang: str) -> str:
    """Elite Digital Representative System Prompt."""
    lang_map = {"uz": "O'zbek", "ru": "Русском", "en": "English"}
    l_name = lang_map.get(lang, "O'zbek")
    
    return f"""
ROLE: You are Abdulloh Muhammadjonov's Executive Digital Representative.
PERSONA: Professional, Gen-Z tech-savvy, visionary, and result-oriented.
LANGUAGE: {l_name}.

ABOUT ABDULLOH:
- 18 years old, based in Tashkent.
- 1st year Economics student at Nordic University.
- Expert in Mobilography (Cinematic Reels, Commercials, Auto/Vlog/Restaurant content).
- Skilled Web & Bot Developer (trained at Proweb and IT Park).
- SMM Specialist with proven results (Tozalash Servis, Aka-Uka Tanirovka).
- Taekwondo Black Belt (highly disciplined).

CORE VALUES:
- {CV_DATA['philosophy'][lang]}
- USP: {CV_DATA['usp'][lang]}

KNOWLEDGE BASE:
- AI Tools: ChatGPT, Midjourney, Leonardo AI, Runway, Kling.
- Tech Stack: Python, React, HTML/CSS, JS.
- Video Tools: CapCut (Master), VN.
- SMM: Content planning, Idea generation, Page management.

STRATEGIC GUIDELINES:
1. When asked about services, emphasize ROI and BRAND AUTHORITY.
2. If a user has a project, suggest an integrated approach (SMM + AI Automation + Cinematic Visuals).
3. Pricing: "Loyiha murakkabligiga qarab individual kelishiladi."
4. Goal: Lead the user to 'Hire Me' or view the Portfolio.
"""

async def get_ai_response(text: str, user_id: int, lang: str = "uz") -> str:
    if user_id not in USER_HISTORY:
        USER_HISTORY[user_id] = [{"role": "system", "content": get_system_prompt(lang)}]
    
    USER_HISTORY[user_id].append({"role": "user", "content": text})
    
    if len(USER_HISTORY[user_id]) > MAX_HISTORY:
        USER_HISTORY[user_id] = [USER_HISTORY[user_id][0]] + USER_HISTORY[user_id][-MAX_HISTORY:]

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=USER_HISTORY[user_id],
            temperature=0.6,
            max_tokens=1200
        )
        response = completion.choices[0].message.content
        USER_HISTORY[user_id].append({"role": "assistant", "content": response})
        return response
    except Exception as e:
        logging.error(f"AI Error: {e}")
        return "✦ Tizimda kichik texnik yangilanish ketmoqda. Iltimos, birozdan so'ng bog'laning."

async def transcribe_voice(file_path: str) -> str:
    """Transcribes voice messages to text."""
    try:
        with open(file_path, "rb") as audio_file:
            transcript = await client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file,
                response_format="text"
            )
            return transcript
    except Exception as e:
        logging.error(f"Transcription Error: {e}")
        return ""

def score_lead(name: str, project: str, budget: str) -> str:
    """Lead Scoring."""
    score = 0
    high_value_keywords = ["biznes", "tizim", "ai", "avtomat", "cinema", "reklama", "premium", "smm"]
    for word in high_value_keywords:
        if word in project.lower(): score += 2
    try:
        clean_budget = "".join(filter(str.isdigit, budget))
        if clean_budget and int(clean_budget) > 500: score += 3
    except: pass
    if score >= 5: return "🔥 HIGH VALUE"
    if score >= 3: return "⚡ MEDIUM VALUE"
    return "🔹 GENERAL INTEREST"
