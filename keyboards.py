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
    """Returns portfolio category inline buttons."""
    buttons = [
        [
            InlineKeyboardButton(text="📸 Mobilografiya", callback_data="port_mob"),
            InlineKeyboardButton(text="💻 Web & Bots", callback_data="port_code")
        ],
        [
            InlineKeyboardButton(text="🤖 AI & SMM", callback_data="port_ai"),
            InlineKeyboardButton(text="🚗 Car Detailing", callback_data="port_car")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_main_menu(lang: str):
    """Returns the main reply keyboard menu based on language."""
    btns = MESSAGES[lang]["buttons"]
    # Build rows of regular text buttons
    rows = [
        [KeyboardButton(text=btns["about"]), KeyboardButton(text=btns["experience"])],
        [KeyboardButton(text=btns["skills"]), KeyboardButton(text=btns["education"])],
        [KeyboardButton(text=btns["portfolio"]), KeyboardButton(text=btns["contact"])],
        [KeyboardButton(text=btns["hire"]), KeyboardButton(text=btns["lang"])],
    ]
    # If a Web App URL is configured, add a dedicated button that opens the Mini App
    if WEB_APP_URL:
        rows.append([KeyboardButton(text=btns.get("mini_app", "Web CV"), web_app=WebAppInfo(url=WEB_APP_URL))])
    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)


def get_contact_inline():
    """Returns inline buttons for social links and PDF download."""
    buttons = [
        [
            InlineKeyboardButton(text="💬 Telegram", url="https://t.me/abdulloh_ai"),
            InlineKeyboardButton(text="📷 Instagram", url="https://instagram.com/abdullokh_mk")
        ],
        [InlineKeyboardButton(text="📢 Portfolio Channel", url="https://t.me/upgcard")],
        [InlineKeyboardButton(text="📄 CV yuklab olish (PDF)", callback_data="download_cv")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)
