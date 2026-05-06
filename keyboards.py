from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,
    WebAppInfo
)
from content import MESSAGES
from config import WEB_APP_URL


def get_language_kb():
    """Returns language selection inline keyboard."""
    buttons = [
        [
            InlineKeyboardButton(text="🇺🇿 O'zbekcha", callback_data="lang_uz"),
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton(text="🇺🇸 English", callback_data="lang_en")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_portfolio_kb():
    """Returns portfolio category inline buttons with minimalist icons."""
    buttons = [
        [
            InlineKeyboardButton(text="✦ Mobilography", callback_data="port_mob"),
            InlineKeyboardButton(text="✦ Web & Bots", callback_data="port_code")
        ],
        [
            InlineKeyboardButton(text="✦ AI Solutions", callback_data="port_ai"),
            InlineKeyboardButton(text="✦ Automotive", callback_data="port_car")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_main_menu(lang: str):
    """Returns the Master Level main menu with FAQ."""
    btns = MESSAGES[lang]["buttons"]
    rows = [
        [KeyboardButton(text=btns["about"]), KeyboardButton(text=btns["experience"])],
        [KeyboardButton(text=btns["portfolio"]), KeyboardButton(text=btns["skills"])],
        [KeyboardButton(text=btns["ai_chat"]), KeyboardButton(text=btns["mini_app"])],
        [KeyboardButton(text=btns["contact"]), KeyboardButton(text=btns["faq"])],
        [KeyboardButton(text=btns["lang"]), KeyboardButton(text=btns["hire"])]
    ]
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)

def get_ai_keyboard(lang: str):
    """Keyboard for AI Chatting mode."""
    text = "⬅️ Ortga / Назад / Back"
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=text)]],
        resize_keyboard=True
    )

def get_contact_inline():
    """Returns minimalist inline buttons for social links."""
    buttons = [
        [
            InlineKeyboardButton(text="◈ Telegram", url="https://t.me/abdulloh_ai"),
            InlineKeyboardButton(text="◈ Instagram", url="https://instagram.com/abdullokh_mk")
        ],
        [InlineKeyboardButton(text="✧ Portfolio Channel", url="https://t.me/upgcard")],
        [InlineKeyboardButton(text="📄 Download CV (PDF)", callback_data="download_cv")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
