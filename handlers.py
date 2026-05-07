from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.fsm.context import FSMContext

from content import MESSAGES, CV_DATA, PORTFOLIO_DATA, H, MEDIA
from keyboards import get_main_menu, get_contact_inline, get_language_kb, get_portfolio_kb, get_ai_keyboard
from config import ADMIN_ID, DATABASE_PATH, WEB_APP_URL
from ai_engine import get_ai_response, transcribe_voice
from pdf_generator import generate_cv_pdf
from states import HireMeStates, AdminStates, AIState
from data.database import (
    add_user, get_user_count, get_user_language, 
    set_user_language, log_message, get_all_users,
    get_detailed_stats, get_recent_users, log_action
)
import os
import uuid
import asyncio

router = Router()

# ━━━━━━━━━━━━━━━━━━━━
# UTILITY & SECURITY
# ━━━━━━━━━━━━━━━━━━━━

def esc(text: str) -> str:
    """Ultra-safe MarkdownV2 escaping for production."""
    if not text: return ""
    chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    res = str(text)
    for c in chars:
        res = res.replace(c, f'\\{c}')
    return res

async def notify_admin(bot, user, action: str):
    """Professional admin notifications."""
    if not ADMIN_ID: return
    try:
        username = f"@{esc(user.username)}" if user.username else "N/A"
        text = f"🔔 *Master Alert*\n{H}\n👤 {esc(user.full_name)} \\({username}\\)\n📌 {esc(action)}"
        await bot.send_message(ADMIN_ID, text, parse_mode="MarkdownV2")
    except Exception: pass

# ━━━━━━━━━━━━━━━━━━━━
# CORE NAVIGATION
# ━━━━━━━━━━━━━━━━━━━━

@router.message(CommandStart())
async def cmd_start(message: Message):
    uid = message.from_user.id
    await add_user(uid, message.from_user.username, message.from_user.full_name)
    await log_action(uid, "Started Bot")
    lang = await get_user_language(uid)
    await message.answer_photo(
        photo=MEDIA["start"],
        caption=MESSAGES[lang]["start"],
        parse_mode="MarkdownV2",
        reply_markup=get_main_menu(lang)
    )

@router.message(F.text.regexp(r"(Ortga|Назад|Back|cancel)"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    lang = await get_user_language(message.from_user.id)
    await message.answer(MESSAGES[lang]["menu"], reply_markup=get_main_menu(lang))

# ━━━━━━━━━━━━━━━━━━━━
# PROFILE & SKILLS
# ━━━━━━━━━━━━━━━━━━━━

def get_btns(key): return [MESSAGES[l]["buttons"][key] for l in ("uz", "ru", "en")]

@router.message(F.text.in_(get_btns("about")))
async def btn_profile(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Viewed Profile")
    lang = await get_user_language(uid)
    await message.answer_photo(photo=MEDIA["about"], caption=MESSAGES[lang]["about"], parse_mode="MarkdownV2")

@router.message(F.text.in_(get_btns("experience")))
async def btn_experience(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Viewed Experience")
    lang = await get_user_language(uid)
    header = {"uz": "TAJRIBA", "ru": "ОПЫТ", "en": "EXPERIENCE"}
    text = f"✦ *{header[lang]}*\n{H}\n\n"
    for exp in CV_DATA["experience"]:
        text += f"◈  *{esc(exp['title'])}* \\({esc(exp['duration'])}\\)\n└ {exp['desc'][lang]}\n\n"
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(F.text.in_(get_btns("skills")))
async def btn_skills(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Viewed Skills")
    lang = await get_user_language(uid)
    header = {"uz": "MAHORAT", "ru": "НАВЫКИ", "en": "SKILLS"}
    text = f"✦ *{header[lang]}*\n{H}\n\n"
    text += f"◈ *Technical:* {esc(', '.join(CV_DATA['skills']['technical']))}\n"
    text += f"◈ *Soft:* {esc(', '.join(CV_DATA['skills']['soft']))}\n"
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(F.text.in_(get_btns("portfolio")))
async def btn_portfolio(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Viewed Portfolio Menu")
    lang = await get_user_language(uid)
    await message.answer(MESSAGES[lang]["portfolio"], reply_markup=get_portfolio_kb(), parse_mode="MarkdownV2")

@router.message(F.text.in_(get_btns("faq")))
async def btn_faq(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Viewed FAQ")
    lang = await get_user_language(uid)
    await message.answer(MESSAGES[lang]["faq"], parse_mode="MarkdownV2")

@router.message(F.text.in_(get_btns("contact")))
async def btn_contact(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Viewed Contact")
    lang = await get_user_language(uid)
    await message.answer(MESSAGES[lang]["contact"], reply_markup=get_contact_inline(), parse_mode="MarkdownV2")

@router.message(F.text.in_(get_btns("lang")))
async def btn_lang(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Opened Language Menu")
    lang = await get_user_language(uid)
    await message.answer(MESSAGES[lang]["lang_select"], reply_markup=get_language_kb())

@router.message(F.text.in_(get_btns("mini_app")))
async def btn_web_cv(message: Message):
    uid = message.from_user.id
    await log_action(uid, "Opened Mini App")
    lang = await get_user_language(uid)
    await message.answer(
        f"✦ {esc(MESSAGES[lang]['buttons']['mini_app'])}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[[
            InlineKeyboardButton(text="🚀 Launch Elite Experience", web_app=WebAppInfo(url=WEB_APP_URL))
        ]])
    )

# ━━━━━━━━━━━━━━━━━━━━
# AI CHAT
# ━━━━━━━━━━━━━━━━━━━━

@router.message(F.text.in_(get_btns("ai_chat")))
async def ai_mode_start(message: Message, state: FSMContext):
    uid = message.from_user.id
    await log_action(uid, "Entered AI Chat")
    lang = await get_user_language(uid)
    await message.answer(MESSAGES[lang]["ai_intro"], reply_markup=get_ai_keyboard(lang), parse_mode="MarkdownV2")
    await state.set_state(AIState.chatting)

@router.message(AIState.chatting, F.voice)
async def ai_voice_handler(message: Message, state: FSMContext):
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    file_id = message.voice.file_id
    file = await message.bot.get_file(file_id)
    file_path = f"data/{uuid.uuid4()}.ogg"
    await message.bot.download_file(file.file_path, file_path)

    text = await transcribe_voice(file_path)
    if os.path.exists(file_path): os.remove(file_path)

    if not text:
        await message.reply("❌ Ovozni aniqlab bo'lmadi. Iltimos, qaytadan urining.")
        return

    lang = await get_user_language(message.from_user.id)
    response = await get_ai_response(text, message.from_user.id, lang)
    await message.reply(f"🎤 *Sizning savolingiz:* {esc(text)}\n\n{response}", parse_mode="Markdown")
    await log_message(message.from_user.id, text, response)

@router.message(AIState.chatting, F.text)
async def ai_chat_handler(message: Message, state: FSMContext):
    if any(x in message.text for x in ["Ortga", "Назад", "Back", "cancel"]):
        await state.clear()
        lang = await get_user_language(message.from_user.id)
        await message.answer(MESSAGES[lang]["menu"], reply_markup=get_main_menu(lang))
        return
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    lang = await get_user_language(message.from_user.id)
    response = await get_ai_response(message.text, message.from_user.id, lang)
    try: await message.reply(response, parse_mode="Markdown")
    except Exception: await message.reply(response)
    await log_message(message.from_user.id, message.text, response)

# ━━━━━━━━━━━━━━━━━━━━
# CALLBACKS
# ━━━━━━━━━━━━━━━━━━━━

@router.callback_query(F.data.startswith("lang_"))
async def cb_language(callback: CallbackQuery):
    lang = callback.data.split("_")[1]
    await set_user_language(callback.from_user.id, lang)
    await callback.message.delete()
    await callback.message.answer(MESSAGES[lang]["menu"], reply_markup=get_main_menu(lang))
    await callback.answer()

@router.callback_query(F.data == "download_cv")
async def cb_download_cv(callback: CallbackQuery):
    uid = callback.from_user.id
    await log_action(uid, "Downloaded PDF CV")
    lang = await get_user_language(uid)
    file_path = f"Abdulloh_CV_{lang}.pdf"
    msg = await callback.message.answer("⏳ _Generating Master-Grade CV..._")
    generate_cv_pdf(lang, file_path, callback.from_user.full_name)
    await msg.delete()
    await callback.message.answer_document(FSInputFile(file_path), caption=f"📄 Professional CV ({lang.upper()})")
    if os.path.exists(file_path): os.remove(file_path)
    await callback.answer()

@router.callback_query(F.data.startswith("port_"))
async def cb_portfolio(callback: CallbackQuery):
    cat = callback.data.split("_")[1]
    uid = callback.from_user.id
    await log_action(uid, f"Viewed Portfolio: {cat}")
    lang = await get_user_language(uid)
    text = PORTFOLIO_DATA.get(cat, {}).get(lang, "N/A")
    
    try:
        if cat == "mob": await callback.message.answer_video(video=MEDIA["mobilography"], caption=text, parse_mode="MarkdownV2")
        else: await callback.message.answer(text, parse_mode="MarkdownV2")
    except Exception: 
        await callback.message.answer(text.replace("\\", ""))
    await callback.answer()

# ━━━━━━━━━━━━━━━━━━━━
# HIRE ME FLOW
# ━━━━━━━━━━━━━━━━━━━━

@router.message(F.text.in_(get_btns("hire")))
async def btn_hire(message: Message, state: FSMContext):
    await log_action(message.from_user.id, "Started Hire Me Flow")
    await message.answer("👤 *Ismingiz yoki Kompaniya nomi:*", parse_mode="Markdown")
    await state.set_state(HireMeStates.waiting_for_name)

@router.message(HireMeStates.waiting_for_name)
async def hire_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("📝 *Loyihangiz haqida qisqacha:*", parse_mode="Markdown")
    await state.set_state(HireMeStates.waiting_for_project)

@router.message(HireMeStates.waiting_for_project)
async def hire_project(message: Message, state: FSMContext):
    await state.update_data(project=message.text)
    await message.answer("💰 *Taxminiy budjetingiz:*", parse_mode="Markdown")
    await state.set_state(HireMeStates.waiting_for_budget)

@router.message(HireMeStates.waiting_for_budget)
async def hire_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    await message.answer("📞 *Siz bilan bog'lanish uchun raqam yoki Telegram:*", parse_mode="Markdown")
    await state.set_state(HireMeStates.waiting_for_contact)

@router.message(HireMeStates.waiting_for_contact)
async def hire_finish(message: Message, state: FSMContext):
    data = await state.get_data()
    from ai_engine import score_lead
    quality = score_lead(data['name'], data['project'], data['budget'])
    
    summary = (
        f"🤝 *STRATEGIC LEAD: {quality}*\n{H}\n"
        f"👤 *Client:* {esc(data['name'])}\n"
        f"📝 *Brief:* {esc(data['project'])}\n"
        f"💰 *Budget:* {esc(data['budget'])}\n"
        f"📞 *Connect:* {esc(message.text)}"
    )
    if ADMIN_ID: await message.bot.send_message(ADMIN_ID, summary, parse_mode="MarkdownV2")
    await message.answer("✅ *So'rovingiz qabul qilindi\\.*\n\nAbdulloh loyiha detallarini tahlil qilib, tez orada siz bilan bog'lanadi\\. Rahmat\\!", parse_mode="MarkdownV2")
    await state.clear()

# ━━━━━━━━━━━━━━━━━━━━
# ADMIN COMMANDS
# ━━━━━━━━━━━━━━━━━━━━

@router.message(Command("admin"), F.from_user.id == ADMIN_ID)
async def cmd_admin_master(message: Message):
    stats = await get_detailed_stats()
    text = (
        f"👑 *ULTRA ADMIN PANEL*\n{H}\n\n"
        f"📊 *Users:* {stats['users']}\n"
        f"💬 *AI Messages:* {stats['messages']}\n"
        f"🔥 *Hot Action:* {stats['popular']}\n\n"
        f"🛠 /broadcast | /stats | /users"
    )
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(Command("broadcast"), F.from_user.id == ADMIN_ID)
async def cmd_broadcast(message: Message, state: FSMContext):
    await message.answer("📝 *Barcha foydalanuvchilarga yuboriladigan xabarni kiriting:*")
    await state.set_state(AdminStates.waiting_for_broadcast)

@router.message(AdminStates.waiting_for_broadcast, F.from_user.id == ADMIN_ID)
async def process_broadcast(message: Message, state: FSMContext):
    users = await get_all_users()
    count = 0
    await message.answer(f"🚀 {len(users)} ta foydalanuvchiga yuborish boshlandi...")

    for user_id in users:
        try:
            await message.copy_to(user_id)
            count += 1
            await asyncio.sleep(0.05) # Prevent flood
        except Exception:
            pass

    await message.answer(f"✅ Xabar {count} ta foydalanuvchiga muvaffaqiyatli yetkazildi.")
    await state.clear()

@router.message(F.text)
async def ai_handler(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(f"✦ Bo'limni tanlang yoki *{esc(MESSAGES[lang]['buttons']['ai_chat'])}*ga kiring\\.", parse_mode="MarkdownV2")
