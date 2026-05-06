import logging
from openai import AsyncOpenAI
from config import GROQ_API_KEY, DEEPSEEK_API_KEY
from content import CV_DATA, CV_DATA
import os

# Initialize AI Client with fallback to Groq for speed
client = AsyncOpenAI(api_key=GROQ_API_KEY, base_url="https://api.groq.com/openai/v1")

# Conversation Memory
USER_HISTORY = {}
MAX_HISTORY = 10

def get_system_prompt(lang: str) -> str:
    """Master Level Sales Closer System Prompt."""
    lang_map = {"uz": "O'zbek", "ru": "Русском", "en": "English"}
    l_name = lang_map.get(lang, "O'zbek")
    
    projects = "\n".join([f"- {p['name']} ({p['type']}): {p[lang]}" for p in CV_DATA['projects']])
    skills = ", ".join(CV_DATA['skills']['technical'])
    
    return f"""
You are the personal AI Assistant of Abdulloh Muhammadjonov. Your goal is to represent him as a TOP-TIER Professional.
Response Language: {l_name}.

CONTEXT:
- Abdulloh is an expert in Mobilography, AI Bot Development, and SMM.
- He is a student at Nordic University with high discipline (Taekwondo experience).
- PROJECTS:
{projects}
- SKILLS: {skills}

RULES:
1. Tone: Elite, confident, minimalist, and extremely helpful.
2. If asked about his background, emphasize his discipline and innovative approach.
3. If asked about price, say: "Har bir loyiha individual yondashuvni talab qiladi. Aniqroq ma'lumot uchun 'Hamkorlik' bo'limi orqali so'rov yuborishingiz mumkin."
4. Use professional symbols (✦, ◈) to structure your answers.
5. Always try to lead the user towards booking a consultation or looking at the portfolio.
6. Keep answers concise but high-value.
"""

async def get_ai_response(text: str, user_id: int, lang: str = "uz") -> str:
    """Fetches AI response with context awareness and retry logic."""
    if user_id not in USER_HISTORY:
        USER_HISTORY[user_id] = [{"role": "system", "content": get_system_prompt(lang)}]
    
    USER_HISTORY[user_id].append({"role": "user", "content": text})
    
    # Trim history if too long
    if len(USER_HISTORY[user_id]) > MAX_HISTORY:
        USER_HISTORY[user_id] = [USER_HISTORY[user_id][0]] + USER_HISTORY[user_id][-MAX_HISTORY:]

    try:
        completion = await client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=USER_HISTORY[user_id],
            temperature=0.7,
            max_tokens=1000
        )
        response = completion.choices[0].message.content
        USER_HISTORY[user_id].append({"role": "assistant", "content": response})
        return response
    except Exception as e:
        logging.error(f"AI Error: {e}")
        return "✦ Kechirasiz, tizimda vaqtinchalik uzilish yuz berdi. Iltimos, birozdan so'ng urinib ko'ring."

async def transcribe_voice(file_path: str) -> str:
    """Uses Whisper to transcribe voice messages."""
    try:
        with open(file_path, "rb") as audio_file:
            transcript = await client.audio.transcriptions.create(
                model="whisper-large-v3",
                file=audio_file
            )
            return transcript.text
    except Exception as e:
        logging.error(f"STT Error: {e}")
        return ""
