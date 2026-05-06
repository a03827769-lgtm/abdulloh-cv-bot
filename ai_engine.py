import logging
from openai import AsyncOpenAI
from config import GROQ_API_KEY, DEEPSEEK_API_KEY
from content import CV_DATA
import os

client = AsyncOpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

USER_HISTORY = {}
MAX_HISTORY = 12

def get_system_prompt(lang: str) -> str:
    """Next-Level Business Strategist System Prompt."""
    lang_map = {"uz": "O'zbek", "ru": "Русском", "en": "English"}
    l_name = lang_map.get(lang, "O'zbek")
    
    return f"""
ROLE: You are Abdulloh's Executive Digital Representative and Business Strategist.
PERSONA: Professional, visionary, analytical, and highly persuasive. You don't just answer; you consult.
LANGUAGE: {l_name}.

CORE VALUES:
- {CV_DATA['philosophy'][lang]}
- USP: {CV_DATA['usp'][lang]}

KNOWLEDGE BASE:
- Abdulloh is an expert in Mobilography (Cinematic Visuals) and AI Systems (Business Automation).
- He creates ROI-driven content (increased sales, saved time).
- He is a Taekwondo practitioner (highly disciplined and focused).

STRATEGIC GUIDELINES:
1. When asked about services, explain the BUSINESS VALUE. 
   - Not just 'video', but 'High-conversion cinematic marketing'.
   - Not just 'bot', but 'AI-driven operational efficiency'.
2. If a user mentions a project, suggest how Abdulloh can optimize it.
3. Pricing: Maintain exclusivity. "Abdulloh har bir loyihaga chuqur individual yondashadi. Hamkorlikni boshlash uchun loyiha detallarini ko'rib chiqishimiz kerak."
4. Structure: Use ✦ for headers and ◈ for bullet points.
5. Goal: Convert the conversation into a 'Hire Me' request or a Portfolio view.
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
            temperature=0.6, # Lower temperature for more professional consistency
            max_tokens=1200
        )
        response = completion.choices[0].message.content
        USER_HISTORY[user_id].append({"role": "assistant", "content": response})
        return response
    except Exception as e:
        logging.error(f"AI Error: {e}")
        return "✦ Tizimda kichik texnik yangilanish ketmoqda. Iltimos, birozdan so'ng bog'laning."

def score_lead(name: str, project: str, budget: str) -> str:
    """Simple Lead Scoring to help Abdulloh prioritize."""
    score = 0
    high_value_keywords = ["biznes", "tizim", "ai", "avtomat", "cinema", "reklama", "premium"]
    
    # Check project description
    for word in high_value_keywords:
        if word in project.lower():
            score += 2
            
    # Check budget (very simple heuristic)
    try:
        clean_budget = "".join(filter(str.isdigit, budget))
        if clean_budget and int(clean_budget) > 1000: # Assuming USD or large numbers
            score += 3
    except: pass
    
    if score >= 5: return "🔥 HIGH VALUE"
    if score >= 3: return "⚡ MEDIUM VALUE"
    return "🔹 GENERAL INTEREST"
