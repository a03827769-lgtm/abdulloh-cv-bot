from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from content import MESSAGES, CV_DATA, PORTFOLIO_DATA, H, MEDIA
from keyboards import get_main_menu, get_contact_inline, get_language_kb, get_portfolio_kb, get_ai_keyboard
from config import ADMIN_ID, DATABASE_PATH
from ai_engine import get_ai_response, transcribe_voice
from pdf_generator import generate_cv_pdf
from states import HireMeStates, AdminStates, AIState
from data.database import (
    add_user, get_user_count, get_user_language, 
    set_user_language, log_message, get_all_users,
    get_detailed_stats, get_recent_users
)
import os
import uuid

router = Router()

# ━━━━━━━━━━━━━━━━━━━━
# UTILITY
# ━━━━━━━━━━━━━━━━━━━━

async def notify_admin(bot, user, action: str):
    """Send notification to admin about user activity."""
    if not ADMIN_ID:
        return
    try:
        username = f"@{user.username}" if user.username else "N/A"
        text = (
            f"🔔 *Activity*\n\n"
            f"👤 {user.full_name} \\({username}\\)\n"
            f"📌 {action}"
        )
        await bot.send_message(ADMIN_ID, text, parse_mode="MarkdownV2")
    except Exception:
        pass

def esc(text: str) -> str:
    """Escape special characters for MarkdownV2."""
    chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for c in chars:
        text = text.replace(c, f'\\{c}')
    return text

# ━━━━━━━━━━━━━━━━━━━━
# ADMIN HANDLERS
# ━━━━━━━━━━━━━━━━━━━━

@router.message(Command("admin"), F.from_user.id == ADMIN_ID)
async def cmd_admin(message: Message):
    """Enhanced Admin Dashboard."""
    u_count = await get_user_count()
    stats = await get_detailed_stats()
    
    text = (
        f"👑 *MASTER ADMIN DASHBOARD*\n"
        f"{H}\n\n"
        f"📊 *Statistika:*\n"
        f"◈ Foydalanuvchilar: *{u_count}*\n"
        f"◈ Jami xabarlar: *{stats['messages']}*\n"
        f"◈ AI savollar: *{stats['ai_queries']}*\n\n"
        f"🛠 *Buyruqlar:*\n"
        f"◈ /broadcast — Xabar yuborish\n"
        f"◈ /users — Oxirgi foydalanuvchilar\n"
        f"◈ /db — Ma'lumotlar bazasi\n"
        f"◈ /reply [ID] [Text] — Javob yozish"
    )
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(Command("users"), F.from_user.id == ADMIN_ID)
async def cmd_users(message: Message):
    """Show list of recent users."""
    users = await get_recent_users(10)
    text = "👤 *OXIRGI 10 TA FOYDALANUVCHI*\n\n"
    for uid, name, username in users:
        uname = f"@{esc(username)}" if username else "N/A"
        text += f"◈ {esc(name)} \\({uname}\\)\n└ ID: `{uid}`\n"
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(Command("db"), F.from_user.id == ADMIN_ID)
async def cmd_db(message: Message):
    """Send the database file to admin."""
    if os.path.exists(DATABASE_PATH):
        await message.answer_document(FSInputFile(DATABASE_PATH), caption="📂 Bot Ma'lumotlar Bazasi (SQLite)")
    else:
        await message.answer("❌ Baza topilmadi.")

@router.message(Command("reply"), F.from_user.id == ADMIN_ID)
async def cmd_reply(message: Message, bot):
    """Reply to a specific user by ID."""
    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        await message.answer("❌ Format: `/reply [ID] [Xabar]`")
        return
    
    target_id, text = args[1], args[2]
    try:
        await bot.send_message(target_id, f"✉️ *Administrator xabari:*\n\n{text}", parse_mode="Markdown")
        await message.answer(f"✅ Xabar {target_id} ga yuborildi.")
    except Exception as e:
        await message.answer(f"❌ Xato: {str(e)}")

@router.message(Command("broadcast"), F.from_user.id == ADMIN_ID)
async def start_broadcast(message: Message, state: FSMContext):
    """Start the broadcast process."""
    await message.answer("Enter broadcast message (Text/Photo/Video) or /cancel:")
    await state.set_state(AdminStates.waiting_for_broadcast)

@router.message(AdminStates.waiting_for_broadcast, F.from_user.id == ADMIN_ID)
async def process_broadcast(message: Message, state: FSMContext, bot):
    """Process and send broadcast."""
    users = await get_all_users()
    count = 0
    await message.answer(f"Sending to {len(users)} users...")
    
    for user_id in users:
        try:
            if message.text:
                await bot.send_message(user_id, message.text)
            elif message.photo:
                await bot.send_photo(user_id, message.photo[-1].file_id, caption=message.caption)
            elif message.video:
                await bot.send_video(user_id, message.video.file_id, caption=message.caption)
            count += 1
        except Exception:
            pass
            
    await message.answer(f"✅ Success: {count} users.")
    await state.clear()

# ━━━━━━━━━━━━━━━━━━━━
# COMMANDS & NAVIGATION
# ━━━━━━━━━━━━━━━━━━━━

@router.message(Command("cancel"))
@router.message(F.text.casefold() == "cancel")
@router.message(F.text.regexp(r"(Bekor qilish|Отмена|Cancel|Ortga|Назад|Back)"))
async def cmd_cancel(message: Message, state: FSMContext):
    """Global cancel handler for all states."""
    current_state = await state.get_state()
    if current_state is None:
        # If not in any state, just show menu
        lang = await get_user_language(message.from_user.id)
        await message.answer("✦ Asosiy Menyu", reply_markup=get_main_menu(lang))
        return
    
    await state.clear()
    lang = await get_user_language(message.from_user.id)
    await message.answer("✦ Operatsiya bekor qilindi\\.", reply_markup=get_main_menu(lang), parse_mode="MarkdownV2")

@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle /start — welcome message."""
    uid = message.from_user.id
    await add_user(uid, message.from_user.username, message.from_user.full_name)
    await set_user_language(uid, "uz")
    await message.answer_photo(
        photo=MEDIA["start"],
        caption=MESSAGES["uz"]["start"],
        parse_mode="MarkdownV2",
        reply_markup=get_main_menu("uz")
    )
    await notify_admin(message.bot, message.from_user, "Started the bot")

# Collect all button texts for matching
ALL_ABOUT = [MESSAGES[l]["buttons"]["about"] for l in ("uz", "ru", "en")]
ALL_EXP = [MESSAGES[l]["buttons"]["experience"] for l in ("uz", "ru", "en")]
ALL_SKILLS = [MESSAGES[l]["buttons"]["skills"] for l in ("uz", "ru", "en")]
ALL_PORT = [MESSAGES[l]["buttons"]["portfolio"] for l in ("uz", "ru", "en")]
ALL_CONTACT = [MESSAGES[l]["buttons"]["contact"] for l in ("uz", "ru", "en")]
ALL_LANG = [MESSAGES[l]["buttons"]["lang"] for l in ("uz", "ru", "en")]
ALL_HIRE = [MESSAGES[l]["buttons"]["hire"] for l in ("uz", "ru", "en")]
ALL_AI = [MESSAGES[l]["buttons"]["ai_chat"] for l in ("uz", "ru", "en")]
ALL_FAQ = [MESSAGES[l]["buttons"]["faq"] for l in ("uz", "ru", "en")]

@router.message(F.text.in_(ALL_ABOUT))
async def btn_profile(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer_photo(
        photo=MEDIA["about"],
        caption=MESSAGES[lang]["about"],
        parse_mode="MarkdownV2"
    )

@router.message(F.text.in_(ALL_FAQ))
async def btn_faq(message: Message):
    from content import FAQ_DATA
    lang = await get_user_language(message.from_user.id)
    await message.answer(FAQ_DATA[lang], parse_mode="MarkdownV2")

@router.message(F.text.in_(ALL_EXP))
async def btn_experience(message: Message):
    lang = await get_user_language(message.from_user.id)
    text = f"✦ *PROFESSIONAL EXPERIENCE*\n{H}\n\n"
    for exp in CV_DATA["experience"]:
        text += f"◈  *{esc(exp['title'])}*\n└ {esc(exp['duration'])}\n\n"
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(F.text.in_(ALL_SKILLS))
async def btn_skills(message: Message):
    lang = await get_user_language(message.from_user.id)
    text = f"✦ *SKILLS & EXPERTISE*\n{H}\n\n"
    text += f"◈ *Technical:* {', '.join(CV_DATA['skills']['technical'])}\n"
    text += f"◈ *Soft:* {', '.join(CV_DATA['skills']['soft'])}\n"
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(F.text.in_(ALL_PORT))
async def btn_portfolio(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(MESSAGES[lang]["portfolio"], reply_markup=get_portfolio_kb(), parse_mode="MarkdownV2")

@router.message(F.text.in_(ALL_CONTACT))
async def btn_contact(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(MESSAGES[lang]["contact"], reply_markup=get_contact_inline(), parse_mode="MarkdownV2")

@router.message(F.text.in_(ALL_LANG))
async def btn_lang(message: Message):
    await message.answer("Select language:", reply_markup=get_language_kb())

# ━━━━━━━━━━━━━━━━━━━━
# AI CHAT MODE
# ━━━━━━━━━━━━━━━━━━━━

@router.message(F.text.in_(ALL_AI))
async def ai_mode_start(message: Message, state: FSMContext):
    """Enter AI Chat mode."""
    lang = await get_user_language(message.from_user.id)
    await message.answer(MESSAGES[lang]["ai_intro"], reply_markup=get_ai_keyboard(lang), parse_mode="MarkdownV2")
    await state.set_state(AIState.chatting)
    await notify_admin(message.bot, message.from_user, "Entered AI Chat mode")

@router.message(AIState.chatting, F.text)
async def ai_chat_handler(message: Message):
    """Process messages with AI only in AI mode."""
    # Handle Back/Cancel first
    if any(x in message.text for x in ["Ortga", "Назад", "Back", "Cancel"]):
        lang = await get_user_language(message.from_user.id)
        await message.answer("✦ Asosiy Menyu", reply_markup=get_main_menu(lang))
        return
        
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    lang = await get_user_language(message.from_user.id)
    response = await get_ai_response(message.text, message.from_user.id, lang)
    await message.reply(response)
    await log_message(message.from_user.id, message.text, response)

@router.message(AIState.chatting, F.voice)
async def ai_voice_handler(message: Message, bot):
    """Handle voice in AI mode."""
    lang = await get_user_language(message.from_user.id)
    wait_msg = await message.answer("🎧 _Listening_")
    try:
        file = await bot.get_file(message.voice.file_id)
        path = f"data/{uuid.uuid4()}.ogg"
        await bot.download_file(file.file_path, path)
        text = await transcribe_voice(path)
        os.remove(path)
        if not text:
            await wait_msg.edit_text("❌ Could not recognize voice")
            return
        await wait_msg.edit_text("🤖 _Thinking_")
        response = await get_ai_response(text, message.from_user.id, lang)
        await wait_msg.delete()
        await message.answer(response)
    except Exception as e:
        await wait_msg.edit_text(f"❌ Error: {str(e)[:40]}")

# ━━━━━━━━━━━━━━━━━━━━
# CALLBACKS & OTHERS
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
    lang = await get_user_language(callback.from_user.id)
    file_path = f"Abdulloh_CV_{lang}.pdf"
    await callback.message.answer("⏳ Generating PDF...")
    generate_cv_pdf(lang, file_path, callback.from_user.full_name)
    await callback.message.answer_document(FSInputFile(file_path), caption=f"📄 Abdulloh CV ({lang.upper()})")
    if os.path.exists(file_path): os.remove(file_path)
    await callback.answer()

@router.callback_query(F.data.startswith("port_"))
async def cb_portfolio(callback: CallbackQuery):
    cat = callback.data.split("_")[1]
    lang = await get_user_language(callback.from_user.id)
    text = PORTFOLIO_DATA.get(cat, {}).get(lang, "No data")
    if cat == "mob":
        await callback.message.answer_video(video=MEDIA["mobilography"], caption=text, parse_mode="MarkdownV2")
    else:
        await callback.message.answer(text, parse_mode="MarkdownV2")
    await callback.answer()

@router.message(F.text.in_(ALL_HIRE))
async def btn_hire(message: Message, state: FSMContext):
    lang = await get_user_language(message.from_user.id)
    await message.answer("Enter your name/company:")
    await state.set_state(HireMeStates.waiting_for_name)

@router.message(HireMeStates.waiting_for_name)
async def hire_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("What is the project?")
    await state.set_state(HireMeStates.waiting_for_project)

@router.message(HireMeStates.waiting_for_project)
async def hire_project(message: Message, state: FSMContext):
    await state.update_data(project=message.text)
    await message.answer("Budget?")
    await state.set_state(HireMeStates.waiting_for_budget)

@router.message(HireMeStates.waiting_for_budget)
async def hire_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    await message.answer("Contact info (Phone/Telegram):")
    await state.set_state(HireMeStates.waiting_for_contact)

@router.message(HireMeStates.waiting_for_contact)
async def hire_finish(message: Message, state: FSMContext):
    data = await state.get_data()
    summary = f"🤝 *NEW PROJECT*\n\n👤 From: {esc(data['name'])}\n📝 Project: {esc(data['project'])}\n💰 Budget: {esc(data['budget'])}\n📞 Contact: {esc(message.text)}"
    if ADMIN_ID: await message.bot.send_message(ADMIN_ID, summary, parse_mode="MarkdownV2")
    await message.answer("✅ Sent to Abdulloh. Thank you!")
    await state.clear()

@router.message(F.text)
async def ai_handler(message: Message):
    """Catch-all for text messages outside AI mode."""
    lang = await get_user_language(message.from_user.id)
    btn_text = MESSAGES[lang]['buttons']['ai_chat']
    await message.answer(f"✦ Bot bo'limlaridan foydalaning yoki AI bilan muloqot uchun *{esc(btn_text)}* bo'limiga kiring\\.", parse_mode="MarkdownV2")
