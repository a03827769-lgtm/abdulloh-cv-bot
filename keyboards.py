from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
    WebAppInfo
)
from content import MESSAGES
from config import WEB_APP_URL

def get_language_kb():
    """Elegant language selection."""
    buttons = [
        [
            InlineKeyboardButton(text="💎 O'zbekcha", callback_data="lang_uz"),
            InlineKeyboardButton(text="💎 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="💎 English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_portfolio_kb():
    """Premium portfolio categories with minimalist aesthetics."""
    buttons = [
        [
            InlineKeyboardButton(text="✦ Mobilography & Arts", callback_data="port_mob"),
            InlineKeyboardButton(text="✦ AI & Systems", callback_data="port_code")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def get_main_menu(lang: str):
    """The Ultimate Master Menu with intuitive layout."""
    btns = MESSAGES[lang]["buttons"]
    rows = [
        [KeyboardButton(text=btns["about"]), KeyboardButton(text=btns["experience"])],
        [KeyboardButton(text=btns["portfolio"]), KeyboardButton(text=btns["skills"])],
        [KeyboardButton(text=btns["ai_chat"]), KeyboardButton(text=btns["mini_app"])],
        [KeyboardButton(text=btns["contact"]), KeyboardButton(text=btns["faq"])],
        [KeyboardButton(text=btns["lang"]), KeyboardButton(text=btns["hire"])]
    ]
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True, input_field_placeholder="✦ Elite System Activated")

def get_ai_keyboard(lang: str):
    """Back button for AI mode, specific to language."""
    btn_text = MESSAGES[lang]["buttons"]["back"]
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=btn_text)]],
        resize_keyboard=True
    )

def get_contact_inline():
    """High-end social connectivity buttons."""
    buttons = [
        [
            InlineKeyboardButton(text="◈ Digital Office (TG)", url="https://t.me/abdulloh_ai"),
            InlineKeyboardButton(text="◈ Visual Gallery (IG)", url="https://instagram.com/abdullokh_mk")
        ],
        [InlineKeyboardButton(text="✧ Official Portfolio Channel", url="https://t.me/upgcard")],
        [InlineKeyboardButton(text="📄 Get Professional CV (PDF)", callback_data="download_cv")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
