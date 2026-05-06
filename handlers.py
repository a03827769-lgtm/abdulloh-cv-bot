from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiogram.types import FSInputFile
from aiogram.fsm.context import FSMContext
from content import MESSAGES, CV_DATA, PORTFOLIO_DATA, H, MEDIA
from keyboards import get_main_menu, get_contact_inline, get_language_kb, get_portfolio_kb
from data.database import add_user, get_user_count, get_user_language, set_user_language, log_message, get_all_users
from config import ADMIN_ID
from ai_engine import get_ai_response, transcribe_voice
from pdf_generator import generate_cv_pdf
from states import HireMeStates, AdminStates
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
            f"🔔 *Bildirishnoma*\n\n"
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
    """Admin dashboard with stats and broadcast button."""
    count = await get_user_count()
    text = (
        f"👑 *Admin Paneli*\n\n"
        f"📊 Statistika:\n"
        f"└ Foydalanuvchilar soni: *{count}*\n\n"
        f"Yangi xabar yubormoqchi bo'lsangiz /broadcast buyrug'ini bering\\."
    )
    await message.answer(text, parse_mode="MarkdownV2")

@router.message(Command("broadcast"), F.from_user.id == ADMIN_ID)
async def start_broadcast(message: Message, state: FSMContext):
    """Start the broadcast process."""
    await message.answer("Yubormoqchi bo'lgan xabaringizni yuboring (Text, Photo yoki Video)\\.\nBekor qilish uchun /cancel deb yozing\\.")
    await state.set_state(AdminStates.waiting_for_broadcast)

@router.message(AdminStates.waiting_for_broadcast, F.from_user.id == ADMIN_ID)
async def process_broadcast(message: Message, state: FSMContext, bot):
    """Process and send broadcast to all users."""
    users = await get_all_users()
    count = 0
    await message.answer(f"Xabar {len(users)} ta foydalanuvchiga yuborilmoqda\\.\\.\\.")
    
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
            
    await message.answer(f"✅ Xabar muvaffaqiyatli {count} ta foydalanuvchiga yuborildi\\.")
    await state.clear()

# ━━━━━━━━━━━━━━━━━━━━
# COMMANDS
# ━━━━━━━━━━━━━━━━━━━━

@router.message(CommandStart())
async def cmd_start(message: Message):
    """Handle /start — welcome message in Uzbek."""
    uid = message.from_user.id
    await add_user(uid, message.from_user.username, message.from_user.full_name)
    await set_user_language(uid, "uz")
    await message.answer_photo(
        photo=MEDIA["start"],
        caption=MESSAGES["uz"]["start"],
        parse_mode="MarkdownV2",
        reply_markup=get_main_menu("uz")
    )
    await notify_admin(message.bot, message.from_user, "Botni ishga tushirdi 🚀")


@router.message(Command("help"))
async def cmd_help(message: Message):
    """Handle /help — show available commands."""
    lang = await get_user_language(message.from_user.id)
    help_texts = {
        "uz": (
            f"{H}\n"
            f"📋  *BUYRUQLAR*\n"
            f"{H}\n\n"
            f"/start — Botni qayta ishga tushirish\n"
            f"/help — Buyruqlar ro'yxati\n"
            f"/about — Men haqimda\n"
            f"/portfolio — Portfolio\n"
            f"/contact — Aloqa ma'lumotlari\n"
            f"/language — Tilni o'zgartirish"
        ),
        "ru": (
            f"{H}\n"
            f"📋  *КОМАНДЫ*\n"
            f"{H}\n\n"
            f"/start — Перезапустить бота\n"
            f"/help — Список команд\n"
            f"/about — Обо мне\n"
            f"/portfolio — Портфолио\n"
            f"/contact — Контакты\n"
            f"/language — Сменить язык"
        ),
        "en": (
            f"{H}\n"
            f"📋  *COMMANDS*\n"
            f"{H}\n\n"
            f"/start — Restart the bot\n"
            f"/help — List of commands\n"
            f"/about — About me\n"
            f"/portfolio — Portfolio\n"
            f"/contact — Contact info\n"
            f"/language — Change language"
        )
    }
    await message.answer(help_texts[lang], parse_mode="MarkdownV2")


@router.message(Command("about"))
async def cmd_about(message: Message):
    """Handle /about command."""
    lang = await get_user_language(message.from_user.id)
    await message.answer_photo(
        photo=MEDIA["about"],
        caption=MESSAGES[lang]["about"],
        parse_mode="MarkdownV2"
    )
    await notify_admin(message.bot, message.from_user, f"Haqida bo'limini ko'rdi ({lang})")


@router.message(Command("portfolio"))
async def cmd_portfolio(message: Message):
    """Handle /portfolio command."""
    lang = await get_user_language(message.from_user.id)
    await message.answer(
        MESSAGES[lang]["portfolio"],
        reply_markup=get_portfolio_kb(),
        parse_mode="MarkdownV2"
    )


@router.message(Command("contact"))
async def cmd_contact(message: Message):
    """Handle /contact command."""
    lang = await get_user_language(message.from_user.id)
    await message.answer(
        MESSAGES[lang]["contact"],
        reply_markup=get_contact_inline(),
        parse_mode="MarkdownV2"
    )


@router.message(Command("language"))
async def cmd_language(message: Message):
    """Handle /language command."""
    await message.answer(
        "🌐 Tilni tanlang / Выберите язык / Choose language:",
        reply_markup=get_language_kb()
    )


@router.message(Command("stats"))
async def cmd_stats(message: Message):
    """Handle /stats — admin only."""
    if message.from_user.id != ADMIN_ID:
        await message.answer("❌ Bu buyruq faqat administrator uchun\\.", parse_mode="MarkdownV2")
        return
    count = await get_user_count()
    await message.answer(
        f"{H}\n📊  *BOT STATISTIKASI*\n{H}\n\nJami foydalanuvchilar: *{count}*",
        parse_mode="MarkdownV2"
    )


# ━━━━━━━━━━━━━━━━━━━━
# CALLBACK QUERIES
# ━━━━━━━━━━━━━━━━━━━━

@router.callback_query(F.data.startswith("lang_"))
async def cb_language(callback: CallbackQuery):
    """Handle language selection."""
    lang = callback.data.split("_")[1]
    await set_user_language(callback.from_user.id, lang)
    await callback.message.delete()
    await callback.message.answer(
        MESSAGES[lang]["menu"],
        reply_markup=get_main_menu(lang)
    )
    await callback.answer()


@router.callback_query(F.data == "download_cv")
async def cb_download_cv(callback: CallbackQuery):
    """Generate and send CV as PDF."""
    lang = await get_user_language(callback.from_user.id)
    file_path = f"Abdulloh_CV_{lang}.pdf"
    
    await callback.message.answer("⏳ PDF tayyorlanmoqda\\.\\.\\.", parse_mode="MarkdownV2")
    generate_cv_pdf(lang, file_path, callback.from_user.full_name)
    
    document = FSInputFile(file_path)
    await callback.message.answer_document(
        document,
        caption=f"📄 Muhammadjonov Abdulloh — CV ({lang.upper()})"
    )
    if os.path.exists(file_path):
        os.remove(file_path)
    
    await callback.answer()
    await notify_admin(callback.bot, callback.from_user, f"CV yuklab oldi \\({lang}\\)")


@router.callback_query(F.data.startswith("port_"))
async def cb_portfolio_category(callback: CallbackQuery):
    """Handle portfolio category selection."""
    category = callback.data.split("_")[1]
    lang = await get_user_language(callback.from_user.id)
    
    if category in PORTFOLIO_DATA and lang in PORTFOLIO_DATA[category]:
        text = PORTFOLIO_DATA[category][lang]
    else:
        text = "Ma'lumot topilmadi\\."
    
    if category == "mob":
        await callback.message.answer_video(
            video=MEDIA["mobilography"],
            caption=text,
            parse_mode="MarkdownV2"
        )
    else:
        await callback.message.answer(text, parse_mode="MarkdownV2")
    
    await callback.answer()


# ━━━━━━━━━━━━━━━━━━━━
# MENU BUTTON HANDLERS
# ━━━━━━━━━━━━━━━━━━━━

# Collect all button texts for matching
ALL_ABOUT = [MESSAGES[l]["buttons"]["about"] for l in ("uz", "ru", "en")]
ALL_EXP = [MESSAGES[l]["buttons"]["experience"] for l in ("uz", "ru", "en")]
ALL_SKILLS = [MESSAGES[l]["buttons"]["skills"] for l in ("uz", "ru", "en")]
ALL_EDU = [MESSAGES[l]["buttons"]["education"] for l in ("uz", "ru", "en")]
ALL_PORT = [MESSAGES[l]["buttons"]["portfolio"] for l in ("uz", "ru", "en")]
ALL_CONTACT = [MESSAGES[l]["buttons"]["contact"] for l in ("uz", "ru", "en")]
ALL_LANG = [MESSAGES[l]["buttons"]["lang"] for l in ("uz", "ru", "en")]
ALL_HIRE = [MESSAGES[l]["buttons"]["hire"] for l in ("uz", "ru", "en")]


@router.message(F.text.in_(ALL_ABOUT))
async def btn_about(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(MESSAGES[lang]["about"], parse_mode="MarkdownV2")


@router.message(F.text.in_(ALL_EXP))
async def btn_experience(message: Message):
    lang = await get_user_language(message.from_user.id)
    text = MESSAGES[lang]["experience"]
    for exp in CV_DATA["experience"]:
        dur = esc(exp.get("duration", ""))
        title = esc(exp["title"])
        desc_raw = exp["desc"][lang] if isinstance(exp["desc"], dict) else exp["desc"]
        desc = esc(desc_raw)
        text += f"◉  *{title}* — {dur}\n{desc}\n\n"
    await message.answer(text, parse_mode="MarkdownV2")


@router.message(F.text.in_(ALL_SKILLS))
async def btn_skills(message: Message):
    lang = await get_user_language(message.from_user.id)
    text = MESSAGES[lang]["skills"]
    
    tech = ", ".join([esc(s) for s in CV_DATA["skills"]["technical"]])
    text += f"✅  *Technical:*\n{tech}\n\n"
    
    soft_list = CV_DATA["skills"]["soft"].get(lang, CV_DATA["skills"]["soft"]["uz"])
    soft = ", ".join([esc(s) for s in soft_list])
    text += f"🤝  *Soft Skills:*\n{soft}\n\n"
    
    extra_list = CV_DATA["skills"]["extra"].get(lang, CV_DATA["skills"]["extra"]["uz"])
    extra = ", ".join([esc(s) for s in extra_list])
    text += f"🏆  *Extra:*\n{extra}"
    
    await message.answer(text, parse_mode="MarkdownV2")


@router.message(F.text.in_(ALL_EDU))
async def btn_education(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(MESSAGES[lang]["education"], parse_mode="MarkdownV2")


@router.message(F.text.in_(ALL_PORT))
async def btn_portfolio(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(
        MESSAGES[lang]["portfolio"],
        reply_markup=get_portfolio_kb(),
        parse_mode="MarkdownV2"
    )


@router.message(F.text.in_(ALL_CONTACT))
async def btn_contact(message: Message):
    lang = await get_user_language(message.from_user.id)
    await message.answer(
        MESSAGES[lang]["contact"],
        reply_markup=get_contact_inline(),
        parse_mode="MarkdownV2"
    )


@router.message(F.text.in_(ALL_LANG))
async def btn_language(message: Message):
    await message.answer(
        "🌐 Tilni tanlang / Выберите язык / Choose language:",
        reply_markup=get_language_kb()
    )


# ━━━━━━━━━━━━━━━━━━━━
# HIRE ME (FSM)
# ━━━━━━━━━━━━━━━━━━━━

@router.message(F.text.in_(ALL_HIRE))
async def hire_start(message: Message, state: FSMContext):
    lang = await get_user_language(message.from_user.id)
    texts = {
        "uz": "Assalomu alaykum! Hamkorlikka tayyorman. 🤝\nIsmingiz yoki kompaniya nomini kiriting:",
        "ru": "Здравствуйте! Готов к сотрудничеству. 🤝\nВведите ваше имя или название компании:",
        "en": "Hello! I'm ready for collaboration. 🤝\nEnter your name or company name:"
    }
    await message.answer(texts[lang])
    await state.set_state(HireMeStates.waiting_for_name)


@router.message(HireMeStates.waiting_for_name)
async def hire_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    lang = await get_user_language(message.from_user.id)
    texts = {
        "uz": "Ajoyib! Qanday loyiha ustida ishlaymiz?",
        "ru": "Отлично! Над каким проектом будем работать?",
        "en": "Great! What project will we work on?"
    }
    await message.answer(texts[lang])
    await state.set_state(HireMeStates.waiting_for_project)


@router.message(HireMeStates.waiting_for_project)
async def hire_project(message: Message, state: FSMContext):
    await state.update_data(project=message.text)
    lang = await get_user_language(message.from_user.id)
    texts = {
        "uz": "Loyiha uchun budjetingiz? (Yoki 'Kelishiladi' deb yozing):",
        "ru": "Бюджет проекта? (Или напишите 'По договоренности'):",
        "en": "Project budget? (Or write 'Negotiable'):"
    }
    await message.answer(texts[lang])
    await state.set_state(HireMeStates.waiting_for_budget)


@router.message(HireMeStates.waiting_for_budget)
async def hire_budget(message: Message, state: FSMContext):
    await state.update_data(budget=message.text)
    lang = await get_user_language(message.from_user.id)
    texts = {
        "uz": "Aloqa uchun telefon raqam yoki Telegram username:",
        "ru": "Телефон или Telegram username для связи:",
        "en": "Phone number or Telegram username for contact:"
    }
    await message.answer(texts[lang])
    await state.set_state(HireMeStates.waiting_for_contact)


@router.message(HireMeStates.waiting_for_contact)
async def hire_finish(message: Message, state: FSMContext):
    data = await state.get_data()
    username = f"@{message.from_user.username}" if message.from_user.username else "N/A"
    
    summary = (
        f"💼 *YANGI LOYIHA TAKLIFI\\!*\n\n"
        f"👤 Kimdan: {esc(data['name'])}\n"
        f"📝 Loyiha: {esc(data['project'])}\n"
        f"💰 Budjet: {esc(data['budget'])}\n"
        f"📞 Aloqa: {esc(message.text)}\n"
        f"💬 Telegram: {esc(username)}"
    )
    
    if ADMIN_ID:
        await message.bot.send_message(ADMIN_ID, summary, parse_mode="MarkdownV2")
    
    lang = await get_user_language(message.from_user.id)
    done_texts = {
        "uz": "✅ Rahmat! Ma'lumotlaringiz Abdullohga yuborildi. Tez orada siz bilan bog'lanadi!",
        "ru": "✅ Спасибо! Ваши данные отправлены Абдуллоху. Он свяжется с вами в ближайшее время!",
        "en": "✅ Thank you! Your details have been sent to Abdulloh. He'll get back to you soon!"
    }
    await message.answer(done_texts[lang])
    await state.clear()


# ━━━━━━━━━━━━━━━━━━━━
# INLINE MODE
# ━━━━━━━━━━━━━━━━━━━━

@router.inline_query()
async def inline_handler(inline_query: InlineQuery):
    """Handle inline queries for sharing CV in other chats."""
    results = [
        InlineQueryResultArticle(
            id=str(uuid.uuid4()),
            title="Muhammadjonov Abdulloh — CV",
            description="Developer · Mobilographer · AI Expert",
            input_message_content=InputTextMessageContent(
                message_text=(
                    "👤 *Muhammadjonov Abdulloh*\n\n"
                    "Mobilograf · Developer · AI Expert\n\n"
                    "🏛 Nordic University \\(Economics\\)\n"
                    "📍 Tashkent, Uzbekistan\n\n"
                    "💬 @abdulloh\\_ai\n"
                    "📷 Instagram: abdullokh\\_mk\n"
                    "📢 Portfolio: @upgcard"
                ),
                parse_mode="MarkdownV2"
            )
        )
    ]
    await inline_query.answer(results, is_personal=True, cache_time=300)


# ━━━━━━━━━━━━━━━━━━━━
# AI CATCH-ALL (must be last!)
# ━━━━━━━━━━━━━━━━━━━━

@router.message(F.voice)
async def voice_handler(message: Message, bot):
    """Handle voice messages: transcribe and process with AI."""
    lang = await get_user_language(message.from_user.id)
    
    # 1. Notify user
    wait_msg = await message.answer("🎧 _Ovozli xabar eshitilmoqda\\.\\.\\._", parse_mode="MarkdownV2")
    
    try:
        # 2. Download voice file
        file_id = message.voice.file_id
        file = await bot.get_file(file_id)
        file_path = f"data/{uuid.uuid4()}.ogg"
        await bot.download_file(file.file_path, file_path)
        
        # 3. Transcribe
        text = await transcribe_voice(file_path)
        
        # Cleanup
        if os.path.exists(file_path):
            os.remove(file_path)
            
        if not text:
            await wait_msg.edit_text("⚠️ Kechirasiz, ovozni taniy olmadim\\.")
            return
            
        # 4. Process with AI
        await wait_msg.edit_text("🤖 _AI javob tayyorlamoqda\\.\\.\\._", parse_mode="MarkdownV2")
        response = await get_ai_response(text, message.from_user.id, lang)
        
        # 5. Log and respond
        await wait_msg.delete()
        await message.answer(response, parse_mode="Markdown")
        await log_message(message.from_user.id, f"[Voice] {text}", response)
        await notify_admin(bot, message.from_user, f"Ovozli savol berdi: {text[:50]}")
        
    except Exception as e:
        await wait_msg.edit_text(f"⚠️ Xatolik yuz berdi: {str(e)[:50]}")

@router.message(F.text)
async def ai_handler(message: Message):
    """Handle all other text messages via DeepSeek AI."""
    await message.bot.send_chat_action(chat_id=message.chat.id, action="typing")
    
    uid = message.from_user.id
    lang = await get_user_language(uid)
    
    response = await get_ai_response(message.text, user_id=uid, lang=lang)
    await message.reply(response)
    
    await log_message(uid, message.text, response)
    await notify_admin(message.bot, message.from_user, f"AI savol: {esc(message.text[:40])}\\.\\.\\.")
