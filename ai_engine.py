import httpx
from openai import AsyncOpenAI
import logging
from config import GROQ_API_KEY, GROQ_BASE_URL, GROQ_MODEL, DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL
from content import CV_DATA

# Setup logging for AI engine
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AI_ENGINE")

# Initialize AI client
client = None
MODEL_NAME = None
PROVIDER = None

# Debug: check loaded keys (masked for security)
def mask(key: str):
    if not key: return "None"
    if len(key) < 8: return "***"
    return f"{key[:5]}...{key[-3:]}"

logger.info(f"DEBUG: GROQ_API_KEY loaded: {mask(GROQ_API_KEY)}")
logger.info(f"DEBUG: DEEPSEEK_API_KEY loaded: {mask(DEEPSEEK_API_KEY)}")

# Logic to pick the provider
if GROQ_API_KEY and not GROQ_API_KEY.startswith("gsk_your_key") and len(GROQ_API_KEY) > 10:
    http_client = httpx.AsyncClient()
    client = AsyncOpenAI(
        api_key=GROQ_API_KEY.strip(),
        base_url=GROQ_BASE_URL,
        http_client=http_client
    )
    MODEL_NAME = GROQ_MODEL
    PROVIDER = "Groq"
    logger.info(f"AI Provider initialized: {PROVIDER} ({MODEL_NAME})")
elif DEEPSEEK_API_KEY and not DEEPSEEK_API_KEY.startswith("sk-your-key") and len(DEEPSEEK_API_KEY) > 10:
    http_client = httpx.AsyncClient()
    client = AsyncOpenAI(
        api_key=DEEPSEEK_API_KEY.strip(),
        base_url=DEEPSEEK_BASE_URL,
        http_client=http_client
    )
    MODEL_NAME = "deepseek-chat"
    PROVIDER = "DeepSeek"
    logger.info(f"AI Provider initialized: {PROVIDER}")
else:
    logger.warning("No valid AI API Key found in .env! AI features will be disabled.")

# Memory for conversation history {user_id: [messages]}
USER_HISTORY = {}
MAX_HISTORY = 10 

def get_system_prompt(lang_name: str) -> str:
    """Generates a highly detailed system prompt for the AI assistant."""
    projects_list = "\n".join([f"- {p['name']} ({p['type']}): {p['desc']}" for p in CV_DATA['projects']])
    exp_list = "\n".join([f"- {e['title']} ({e['duration']})" for e in CV_DATA['experience']])
    
    return f"""
Siz Muhammadjonov Abdulloh (@abdulloh_ai) ismli yuqori darajali mutaxassisning "Elite AI" assistentisiz. 

ABDULLOH HAQIDAGI STRATEGIK MA'LUMOTLAR:
- To'liq ismi: {CV_DATA['name']}
- Mutaxassisligi: Mobilograf (Cinematic Content Creator), Full-Stack Bot Developer, AI Engineering va SMM Strategist.
- Ta'lim: Nordic University (Iqtisodiyot va Matematik tahlil bo'yicha chuqur bilimga ega).
- Sport: Taekwondo bo'yicha 5 yillik tajriba va medallar sohibi (bu uning intizomi va irodasini ko'rsatadi).

SIZNING ELITE VAZIFANGIZ:
1. Siz nafaqat savollarga javob berasiz, balki Abdullohning brendini eng yuqori darajada taqdim etasiz. 
2. Javoblaringiz samimiy, intellektual va professional bo'lishi shart.
3. Abdullohning ish tajribasi (Mobilografiya, Bot yaratish, Car Detailing) haqida so'rashsa, uning har tomonlama rivojlangan ("Polymath") shaxs ekanligini ta'kidlang.
4. Agar foydalanuvchi hamkorlik taklif qilsa, uni "Hire Me" (Hamkorlik) bo'limiga yo'naltiring.
5. Foydalanuvchi tili ({lang_name}) da mukammal darajada javob bering.

MUHIM: Har bir javobingizda Abdullohning kreativligi va texnik bilimini uyg'unlashtira olishini (vizual kadr + murakkab kod) aks ettiring.
"""

async def get_ai_response(user_text: str, user_id: int, lang: str = "uz") -> str:
    """Gets response from AI with conversation history."""
    lang_names = {"uz": "O'zbek", "ru": "Русский", "en": "English"}
    lang_name = lang_names.get(lang, "O'zbek")
    
    if not client:
        return "⚠️ AI tizimi hozircha ulanmagan. Iltimos, .env faylini tekshiring."

    if user_id not in USER_HISTORY:
        USER_HISTORY[user_id] = [{"role": "system", "content": get_system_prompt(lang_name)}]

    USER_HISTORY[user_id].append({"role": "user", "content": user_text})
    
    if len(USER_HISTORY[user_id]) > MAX_HISTORY:
        USER_HISTORY[user_id] = [USER_HISTORY[user_id][0]] + USER_HISTORY[user_id][-(MAX_HISTORY-1):]

    try:
        response = await client.chat.completions.create(
            model=MODEL_NAME,
            messages=USER_HISTORY[user_id],
            temperature=0.6,
            max_tokens=800
        )
        ai_text = response.choices[0].message.content
        USER_HISTORY[user_id].append({"role": "assistant", "content": ai_text})
        return ai_text
    except Exception as e:
        logger.error(f"{PROVIDER} AI Error: {e}")
        if "402" in str(e) or "balance" in str(e).lower() or "limit" in str(e).lower():
            return f"⚠️ Kechirasiz, {PROVIDER} AI xizmati balansida mablag' yoki limit tugagan. Iltimos, @abdulloh_ai ga xabar bering."
        return f"⚠️ AI xatolik: {str(e)[:50]}..."
async def transcribe_voice(file_path: str) -> str:
    """Transcribes voice message to text using Groq Whisper."""
    if PROVIDER != "Groq":
        return ""
    
    try:
        with open(file_path, "rb") as audio_file:
            transcription = await client.audio.transcriptions.create(
                file=audio_file,
                model="whisper-large-v3",
                response_format="text"
            )
            return transcription
    except Exception as e:
        logger.error(f"Transcription Error: {e}")
        return ""
