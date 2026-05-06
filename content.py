"""
ULTRA PROFESSIONAL CONTENT DATA - ABDULLOH CV BOT v3.0
Language: Multi-language (UZ, RU, EN)
Style: Elite Agency Minimalist
"""

CV_DATA = {
    "name": "Muhammadjonov Abdulloh",
    "age": 18,
    "location": "Toshkent, O'zbekiston",
    "contacts": {
        "telegram": "@abdulloh_ai",
        "portfolio": "@upgcard",
        "instagram": "abdullokh_mk"
    },
    "education": {
        "university": "Nordic University",
        "major": "Economics & Mathematics",
        "year": "1st Year",
    },
    "experience": [
        {
            "title": "Creative Director & Mobilographer",
            "duration": "1.5 Years",
            "desc": {
                "uz": "Cinematic kontentlar yaratish orqali brendlarni vizual darajasini ko'tarish. 100+ dan ortiq muvaffaqiyatli Reels va reklama roliklari.",
                "ru": "Повышение визуального уровня брендов через создание кинематографического контента. Более 100 успешных Reels и рекламных роликов.",
                "en": "Elevating brand visual identity through cinematic content creation. Over 100+ successful Reels and commercial videos."
            }
        },
        {
            "title": "AI & Bot Infrastructure Developer",
            "duration": "1 Year",
            "desc": {
                "uz": "Python va AI texnologiyalari yordamida biznes jarayonlarini 80% gacha avtomatlashtiruvchi ekotizimlar yaratish.",
                "ru": "Создание экосистем, автоматизирующих бизнес-процессы до 80% с использованием технологий Python и AI.",
                "en": "Building ecosystems that automate business processes by up to 80% using Python and AI technologies."
            }
        }
    ],
    "skills": {
        "technical": ["Mobilography", "Python (AI/FastAPI)", "React/Next.js", "Prompt Engineering", "Digital Marketing"],
        "soft": ["Strategic Thinking", "Discipline", "Leadership", "Fast Learning"]
    },
    "projects": [
        {
            "name": "UPG Card",
            "type": "Product",
            "uz": "◈ *Missiya:* Biznes egalari uchun raqamli identifikatsiyani osonlashtirish.\n◈ *Yutuq:* 50+ dan ortiq faol foydalanuvchilar va barqaror tizim.",
            "ru": "◈ *Миссия:* Упрощение цифровой идентификации для владельцев бизнеса.\n◈ *Достижение:* Более 50+ активных пользователей и стабильная система.",
            "en": "◈ *Mission:* Simplifying digital identification for business owners.\n◈ *Result:* Over 50+ active users and a highly stable system."
        },
        {
            "name": "Smart Balance",
            "type": "AI Tool",
            "uz": "◈ *Missiya:* Kichik biznes moliya tizimini tartibga solish.\n◈ *Yutuq:* AI yordamida xatolarni 0% ga tushirish va vaqtni tejash.",
            "ru": "◈ *Миссия:* Организация финансовой системы малого бизнеса.\n◈ *Достижение:* Снижение ошибок до 0% с помощью AI и экономия времени.",
            "en": "◈ *Mission:* Organizing small business financial systems.\n◈ *Result:* Reducing errors to 0% with AI and significant time savings."
        }
    ]
}

H = "──────────────────────────"

MESSAGES = {
    "uz": {
        "start": (
            f"✦ *MUHAMMADJONOV ABDULLOH*\n"
            f"{H}\n\n"
            f"Creative Director  ·  AI Developer  ·  SMM Strategist\n\n"
            f"Assalomu alaykum\\. Siz hozirda Abdullohning shaxsiy raqamli asisstenti bilan muloqot qilyapsiz\\. "
            f"Sizga qanday yordam bera olaman?"
        ),
        "menu": "Pastdagi elite menyudan foydalaning ⬦",
        "about": (
            f"✦ *PROFESSIONAL PROFILE*\n"
            f"{H}\n\n"
            f"Men — Abdulloh Muhammadjonov, zamonaviy texnologiyalar va vizual san'atni birlashtirgan holda innovatsion yechimlar yarataman\\.\n\n"
            f"◈ *Ta'lim:* Nordic University \\(Iqtisodiyot va Matematika\\)\n"
            f"◈ *Tajriba:* Mobilografiya, Dasturlash va AI tizimlari\\.\n"
            f"◈ *Tamoyilim:* 'Sifat — bu shunchaki talab emas, bu bizning brendimizdir\\.'\n\n"
            f"_Abdulloh bilan ishlash — bu kelajak texnologiyalarini bugun qo'llash demakdir\\._"
        ),
        "portfolio": (
            f"✦ *EXPERT PORTFOLIO*\n"
            f"{H}\n\n"
            f"Mening ijodiy va texnik ishlarimni quyidagi bo'limlar orqali ko'rishingiz mumkin:"
        ),
        "contact": (
            f"✦ *CONNECT*\n"
            f"{H}\n\n"
            f"Muvaffaqiyatli hamkorlikni hoziroq boshlash uchun quyidagi tugmalarni bosing:"
        ),
        "ai_intro": (
            f"🤖 *AI ASSISTANT ACTIVATED*\n"
            f"{H}\n\n"
            f"Men Abdullohning barcha loyihalari va imkoniyatlari haqida to'liq ma'lumotga egaman\\. "
            f"Savollaringizni bemalol berishingiz mumkin\\.\n\n"
            f"_Chiqish uchun '⬅️ Ortga' tugmasini bosing\\._"
        ),
        "faq": (
            f"✦ *ESSENTIAL FAQ*\n"
            f"{H}\n\n"
            f"◈ *Qaysi yo'nalishlarda hamkorlik qilasiz?*\n"
            f"└ Videomontaj, Botlar yaratish va Brend dizayni\\.\n\n"
            f"◈ *Ish jarayoni qancha davom etadi?*\n"
            f"└ Loyiha murakkabligiga qarab 3 kundan 2 haftagacha\\.\n\n"
            f"◈ *Narxlar qanday?*\n"
            f"└ Har bir loyiha budjeti individual belgilanadi\\."
        ),
        "lang_select": "🌐 Master Interface: Select Language",
        "buttons": {
            "about": "👤 Profil",
            "experience": "💼 Tajriba",
            "skills": "🛠 Mahorat",
            "portfolio": "📁 Portfolio",
            "contact": "📞 Aloqa",
            "lang": "🌐 Til",
            "hire": "🤝 Hamkorlik",
            "mini_app": "🚀 Web CV",
            "ai_chat": "🤖 AI Yordamchi",
            "faq": "❓ FAQ",
            "back": "⬅️ Ortga"
        }
    },
    "ru": {
        "start": (
            f"✦ *МУХАММАДЖОНОВ АБДУЛЛОХ*\n"
            f"{H}\n\n"
            f"Креативный директор  ·  AI Разработчик  ·  SMM Стратег\n\n"
            f"Здравствуйте\\. Вы находитесь в цифровом пространстве Абдуллоха\\. "
            f"Чем я могу быть вам полезен?"
        ),
        "menu": "Используйте элитное меню ниже ⬦",
        "about": (
            f"✦ *ПРОФЕССИОНАЛЬНЫЙ ПРОФИЛЬ*\n"
            f"{H}\n\n"
            f"Я — Абдуллох Мухаммаджонов, создаю инновационные решения на стыке технологий и визуального искусства\\.\n\n"
            f"◈ *Учеба:* Nordic University \\(Экономика и Математика\\)\n"
            f"◈ *Опыт:* Мобилография, Разработка и AI системы\\.\n"
            f"◈ *Принцип:* 'Качество — это не просто требование, это наш бренд\\.'\n\n"
            f"_Работа с Абдуллохом — это использование технологий будущего уже сегодня\\._"
        ),
        "portfolio": (
            f"✦ *ЭКСПЕРТНОЕ ПОРТФОЛИО*\n"
            f"{H}\n\n"
            f"Ознакомьтесь с моими работами в следующих разделах:"
        ),
        "contact": (
            f"✦ *СВЯЗЬ*\n"
            f"{H}\n\n"
            f"Начните успешное сотрудничество прямо сейчас:"
        ),
        "ai_intro": (
            f"🤖 *AI ПОМОЩНИК АКТИВИРОВАН*\n"
            f"{H}\n\n"
            f"Я владею полной информацией о проектах и возможностях Абдуллоха\\. "
            f"Задавайте любые вопросы\\.\n\n"
            f"_Для выхода нажмите '⬅️ Назад'\\._"
        ),
        "faq": (
            f"✦ *ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ*\n"
            f"{H}\n\n"
            f"◈ *В каких направлениях вы сотрудничаете?*\n"
            f"└ Видеомонтаж, создание ботов и дизайн бренда\\.\n\n"
            f"◈ *Сколько длится рабочий процесс?*\n"
            f"└ От 3 дней до 2 недель в зависимости от сложности\\.\n\n"
            f"◈ *Каковы цены?*\n"
            f"└ Бюджет каждого проекта определяется индивидуально\\."
        ),
        "lang_select": "🌐 Master Interface: Выберите язык",
        "buttons": {
            "about": "👤 Профиль",
            "experience": "💼 Опыт",
            "skills": "🛠 Навыки",
            "portfolio": "📁 Портфолио",
            "contact": "📞 Контакты",
            "lang": "🌐 Язык",
            "hire": "🤝 Сотрудничество",
            "mini_app": "🚀 Web CV",
            "ai_chat": "🤖 AI Помощник",
            "faq": "❓ FAQ",
            "back": "⬅️ Назад"
        }
    },
    "en": {
        "start": (
            f"✦ *ABDULLOH MUHAMMADJONOV*\n"
            f"{H}\n\n"
            f"Creative Director  ·  AI Developer  ·  SMM Strategist\n\n"
            f"Hello\\. You are communicating with Abdulloh's personal digital assistant\\. "
            f"How can I help you today?"
        ),
        "menu": "Use the elite menu below ⬦",
        "about": (
            f"✦ *PROFESSIONAL PROFILE*\n"
            f"{H}\n\n"
            f"I am Abdulloh Muhammadjonov, creating innovative solutions by combining modern technology and visual arts\\.\n\n"
            f"◈ *Education:* Nordic University \\(Economics & Mathematics\\)\n"
            f"◈ *Expertise:* Mobilography, Coding, and AI Systems\\.\n"
            f"◈ *Principle:* 'Quality is not just a requirement, it is our brand\\.'\n\n"
            f"_Working with Abdulloh means applying tomorrow's technology today\\._"
        ),
        "portfolio": (
            f"✦ *EXPERT PORTFOLIO*\n"
            f"{H}\n\n"
            f"You can view my creative and technical work through the sections below:"
        ),
        "contact": (
            f"✦ *CONNECT*\n"
            f"{H}\n\n"
            f"Start a successful collaboration right now:"
        ),
        "ai_intro": (
            f"🤖 *AI ASSISTANT ACTIVATED*\n"
            f"{H}\n\n"
            f"I have full information about Abdulloh's projects and capabilities\\. "
            f"Feel free to ask any questions\\.\n\n"
            f"_Click '⬅️ Back' to exit AI mode\\._"
        ),
        "faq": (
            f"✦ *ESSENTIAL FAQ*\n"
            f"{H}\n\n"
            f"◈ *In which areas do you collaborate?*\n"
            f"└ Video editing, Bot creation, and Brand design\\.\n\n"
            f"◈ *How long does the work process take?*\n"
            f"└ 3 days to 2 weeks depending on complexity\\.\n\n"
            f"◈ *What are the prices?*\n"
            f"└ Each project budget is set individually\\."
        ),
        "lang_select": "🌐 Master Interface: Select Language",
        "buttons": {
            "about": "👤 Profile",
            "experience": "💼 Experience",
            "skills": "🛠 Skills",
            "portfolio": "📁 Portfolio",
            "contact": "📞 Contact",
            "lang": "🌐 Language",
            "hire": "🤝 Hire Me",
            "mini_app": "🚀 Web CV",
            "ai_chat": "🤖 AI Assistant",
            "faq": "❓ FAQ",
            "back": "⬅️ Back"
        }
    }
}

PORTFOLIO_DATA = {
    "mob": {
        "uz": "📸 *Mobilografiya Galereyasi*\n\nLoyihalarimda yuqori sifatli cinematic yondashuvdan foydalanaman\\.\n◈ *Natija:* Tomoshabinlar e'tiborini 80% ko'proq ushlab turuvchi kontentlar\\.",
        "ru": "📸 *Галерея Мобилографии*\n\nВ проектах я использую качественный кинематографический подход\\.\n◈ *Результат:* Контент, удерживающий внимание зрителей на 80% эффективнее\\.",
        "en": "📸 *Mobilography Gallery*\n\nI use a high-quality cinematic approach in my projects\\.\n◈ *Result:* Content that retains audience attention 80% more effectively\\."
    },
    "code": {
        "uz": "💻 *Development Showcase*\n\n◈ *CV Bot:* Ushbu bot — mening to'liq imkoniyatlarim namunasi\\.\n◈ *Smart Balance:* AI bilan integratsiyalangan moliyaviy yordamchi\\.\n◈ *Arenda Bot:* Biznes jarayonlarini avtomatlashtirish tizimi\\.",
        "ru": "💻 *Витрина Разработки*\n\n◈ *CV Bot:* Этот бот — пример моих полных возможностей\\.\n◈ *Smart Balance:* Финансовый помощник с интеграцией AI\\.\n◈ *Arenda Bot:* Система автоматизации бизнес-процессов\\.",
        "en": "💻 *Development Showcase*\n\n◈ *CV Bot:* This bot is a prime example of my full capabilities\\.\n◈ *Smart Balance:* Financial assistant with AI integration\\.\n◈ *Arenda Bot:* Business process automation system\\."
    }
}

MEDIA = {
    "start": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
    "about": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
    "mobilography": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
}
