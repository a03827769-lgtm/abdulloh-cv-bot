"""Bot configuration module."""

import os
from dotenv import load_dotenv

load_dotenv()

# --- Bot ---
BOT_TOKEN: str = os.getenv("BOT_TOKEN", "").strip()
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable is required. Get it from @BotFather.")

# --- Admin ---
ADMIN_ID: int = int(os.getenv("ADMIN_ID", "0"))

# --- AI ---
DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL: str = "https://api.deepseek.com"

GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
GROQ_BASE_URL: str = "https://api.groq.com/openai/v1"
GROQ_MODEL: str = "llama-3.3-70b-versatile" # Premium fast model

# --- Web App ---
WEB_APP_URL: str = os.getenv("WEB_APP_URL", "https://abdulloh-cv.vercel.app/")

# --- Security ---
RATE_LIMIT_SECONDS: float = float(os.getenv("RATE_LIMIT_SECONDS", "1"))
MAX_REQUESTS_PER_MINUTE: int = int(os.getenv("MAX_REQUESTS_PER_MINUTE", "30"))

# --- Database ---
DATABASE_PATH: str = os.path.join(os.path.dirname(__file__), "data", "analytics.db")
