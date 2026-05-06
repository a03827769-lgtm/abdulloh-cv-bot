"""CV content data and multi-language messages with premium formatting."""

# ━━━━━━━━━━━━━━━━━━━━
# CV DATA
# ━━━━━━━━━━━━━━━━━━━━

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
        "major": "Iqtisod (Economics)",
        "year": "1-kurs",
    },
    "projects": [
        {
            "name": "UPG Card",
            "type": "Portfolio / SMM",
            "link": "@upgcard",
            "desc": "Shaxsiy brend va mobilografiya ishlari uchun yaratilgan platforma."
        },
        {
            "name": "Smart Balance Mini App",
            "type": "Development",
            "desc": "Tadbirkorlar uchun moliya boshqaruv tizimi (Telegram Mini App)."
        },
        {
            "name": "Arenda Bot",
            "type": "Bot Development",
            "desc": "Ijara xizmatlari uchun avtomatlashtirilgan tizim."
        }
    ],
    "experience": [
        {
            "title": "Mobilograf & Content Creator",
            "duration": "1.5 yil",
            "desc": {
                "uz": "Sifatli video kontentlar, 4K montaj, rangli korreksiya va kreativ ssenariylar ustida ishlash.",
                "ru": "Создание качественного видеоконтента, монтаж в 4K, цветокоррекция и работа над креативными сценариями.",
                "en": "Creating high-quality video content, 4K editing, color correction, and working on creative scripts."
            }
        },
        {
            "title": "Full-Stack Bot Developer",
            "duration": "1 yil",
            "desc": {
                "uz": "Aiogram, FastAPI va AI integratsiyalari bilan murakhhab botlar va Mini App'lar yaratish.",
                "ru": "Создание сложных ботов и Mini Apps с использованием Aiogram, FastAPI и AI интеграций.",
                "en": "Building complex bots and Mini Apps using Aiogram, FastAPI, and AI integrations."
            }
        },
        {
            "title": "SMM Specialist",
            "duration": "5 oy",
            "desc": {
                "uz": "Brendni rivojlantirish, auditoriya bilan ishlash va Reels/Posts strategiyasini tuzish.",
                "ru": "Развитие бренда, работа с аудиторией и создание стратегии Reels/Posts.",
                "en": "Brand development, audience engagement, and creating Reels/Posts strategies."
            }
        },
        {
            "title": "Car Detailing Specialist",
            "duration": "1 yil",
            "desc": {
                "uz": "Tanirovka, broniplyonka va laminatsiya xizmatlari bo'yicha professional tajriba.",
                "ru": "Профессиональный опыт в услугах тонировки, бронепленке и ламинации.",
                "en": "Professional experience in car tinting, protective film, and lamination services."
            }
        }
    ],
    "skills": {
        "technical": ["Mobilografiya", "Python (Aiogram/FastAPI)", "Web Development (React/Vite)", "AI Engineering", "SMM"],
        "soft": {
            "uz": ["Jamoada ishlash", "Liderlik", "Matematik tahlil", "Kreativ fikrlash"],
            "ru": ["Командная работа", "Лидерство", "Математический анализ", "Креативное мышление"],
            "en": ["Teamwork", "Leadership", "Mathematical Analysis", "Creative Thinking"]
        },
        "extra": {
            "uz": ["Taekwondo (5 yil, Medal va Sertifikatlar)", "IELTS 5.5"],
            "ru": ["Тхэквондо (5 лет, медали и сертификаты)", "IELTS 5.5"],
            "en": ["Taekwondo (5 years, Medals & Certificates)", "IELTS 5.5"]
        }
    },
    "languages_spoken": [
        {"lang": "O'zbek", "level": "Ona tili (Native)"},
        {"lang": "English", "level": "IELTS 5.5"},
        {"lang": "Русский", "level": "Свободное общение"}
    ]
}

# ━━━━━━━━━━━━━━━━━━━━
# MEDIA (Telegram File IDs or Direct URLs)
# ━━━━━━━━━━━━━━━━━━━━

MEDIA = {
    "start": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97", # Welcome Image
    "about": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d", # Profile Photo
    "mobilography": "https://v1.pinimg.com/videos/mc/720p/f1/8c/6b/f18c6b7d3453716d1f568a86576b5d9d.mp4", # Sample Video
}

# ━━━━━━━━━━━━━━━━━━━━
# PREMIUM FORMATTING
# ━━━━━━━━━━━━━━━━━━━━

H = "━━━━━━━━━━━━━━━━━━━━━━━━━━"
DOT = "◉"

# ━━━━━━━━━━━━━━━━━━━━
# MESSAGES (3 LANGUAGES)
# ━━━━━━━━━━━━━━━━━━━━

MESSAGES = {
    "uz": {
        "start": (
            f"{H}\n"
            f"👤  *MUHAMMADJONOV ABDULLOH*\n"
            f"{H}\n\n"
            f"Mobilograf  ·  Developer  ·  AI Expert\n\n"
            f"Assalomu alaykum\\! Men Abdullohning shaxsiy AI\\-assistentiman\\.\n"
            f"Pastdagi menyudan kerakli bo'limni tanlang yoki bemalol savol bering\\!\n\n"
            f"🤖 _Men siz bilan Abdulloh haqida gaplasha olaman\\._"
        ),
        "menu": "Pastdagi menyudan foydalaning 👇",
        "about": (
            f"{H}\n"
            f"👤  *MEN HAQIMDA*\n"
            f"{H}\n\n"
            f"Abdulloh — zamonaviy texnologiyalar va vizual san'at\n"
            f"uyg'unligida ishlovchi 18 yoshli mutaxassis\\.\n\n"
            f"🏛  *Ta'lim:* Nordic University \\(Iqtisod, 1\\-kurs\\)\n"
            f"📍  *Manzil:* Toshkent shahri\n"
            f"🥋  *Sport:* Taekwondo — 5 yil \\(Medallar sohibi\\)\n"
            f"🌍  *Tillar:* O'zbek \\| English \\(IELTS 5\\.5\\) \\| Русский\n\n"
            f"_U nafaqat kod yozadi, balki kadrlarni jonlantiradi\\!_"
        ),
        "experience": (
            f"{H}\n"
            f"💼  *PROFESSIONAL TAJRIBA*\n"
            f"{H}\n\n"
        ),
        "skills": (
            f"{H}\n"
            f"🛠  *MAHORAT VA KO'NIKMALAR*\n"
            f"{H}\n\n"
        ),
        "education": (
            f"{H}\n"
            f"🎓  *TA'LIM*\n"
            f"{H}\n\n"
            f"🏛  *Muassasa:* Nordic University\n"
            f"📖  *Yo'nalish:* Iqtisodiyot\n"
            f"⏳  *Bosqich:* 1\\-kurs talabasi\n\n"
            f"📐 *Qo'shimcha:* Matematika kursida 1\\.5 yil davomida\n"
            f"chuqurlashtirilgan bilim olgan\\."
        ),
        "portfolio": (
            f"{H}\n"
            f"📁  *VISUAL PORTFOLIO*\n"
            f"{H}\n\n"
            f"Abdullohning barcha ijodiy ishlarini quyidagi\n"
            f"kategoriyalar orqali ko'rishingiz mumkin\\."
        ),
        "contact": (
            f"{H}\n"
            f"📞  *ALOQA MA'LUMOTLARI*\n"
            f"{H}\n\n"
            f"Siz Abdulloh bilan to'g'ridan\\-to'g'ri\n"
            f"bog'lanishingiz mumkin:"
        ),
        "buttons": {
            "about": "👤 Haqimda",
            "experience": "💼 Tajriba",
            "skills": "🛠 Ko'nikmalar",
            "education": "🎓 Ta'lim",
            "portfolio": "📁 Portfolio",
            "contact": "📞 Aloqa",
            "lang": "🌐 Til / Language",
            "hire": "💼 Hamkorlik",
            "mini_app": "🚀 Web CV"
        }
    },
    "ru": {
        "start": (
            f"{H}\n"
            f"👤  *МУХАММАДЖОНОВ АБДУЛЛОХ*\n"
            f"{H}\n\n"
            f"Мобилограф  ·  Разработчик  ·  AI Эксперт\n\n"
            f"Здравствуйте\\! Я личный AI\\-ассистент Абдуллоха\\.\n"
            f"Выберите раздел из меню или задайте любой вопрос\\!\n\n"
            f"🤖 _Я могу рассказать вам всё об Абдуллохе\\._"
        ),
        "menu": "Используйте меню ниже 👇",
        "about": (
            f"{H}\n"
            f"👤  *ОБО МНЕ*\n"
            f"{H}\n\n"
            f"Абдуллох — 18\\-летний специалист на стыке\n"
            f"современных технологий и визуального искусства\\.\n\n"
            f"🏛  *Учеба:* Nordic University \\(Экономика, 1\\-й курс\\)\n"
            f"📍  *Локация:* Ташкент\n"
            f"🥋  *Спорт:* Тхэквондо — 5 лет \\(обладатель медалей\\)\n"
            f"🌍  *Языки:* Узбекский \\| English \\(IELTS 5\\.5\\) \\| Русский\n\n"
            f"_Он не просто пишет код — он оживляет кадры\\!_"
        ),
        "experience": (
            f"{H}\n"
            f"💼  *ПРОФЕССИОНАЛЬНЫЙ ОПЫТ*\n"
            f"{H}\n\n"
        ),
        "skills": (
            f"{H}\n"
            f"🛠  *НАВЫКИ И УМЕНИЯ*\n"
            f"{H}\n\n"
        ),
        "education": (
            f"{H}\n"
            f"🎓  *ОБРАЗОВАНИЕ*\n"
            f"{H}\n\n"
            f"🏛  *Учреждение:* Nordic University\n"
            f"📖  *Направление:* Экономика\n"
            f"⏳  *Курс:* 1\\-й курс\n\n"
            f"📐 *Дополнительно:* 1\\.5 года углубленного\n"
            f"изучения математики\\."
        ),
        "portfolio": (
            f"{H}\n"
            f"📁  *ВИЗУАЛЬНОЕ ПОРТФОЛИО*\n"
            f"{H}\n\n"
            f"Просмотрите творческие работы Абдуллоха\n"
            f"по категориям\\."
        ),
        "contact": (
            f"{H}\n"
            f"📞  *КОНТАКТНАЯ ИНФОРМАЦИЯ*\n"
            f"{H}\n\n"
            f"Вы можете связаться с Абдуллохом напрямую:"
        ),
        "buttons": {
            "about": "👤 Обо мне",
            "experience": "💼 Опыт",
            "skills": "🛠 Навыки",
            "education": "🎓 Образование",
            "portfolio": "📁 Портфолио",
            "contact": "📞 Контакты",
            "lang": "🌐 Язык / Til",
            "hire": "💼 Сотрудничество",
            "mini_app": "🚀 Web CV"
        }
    },
    "en": {
        "start": (
            f"{H}\n"
            f"👤  *ABDULLOH MUHAMMADJONOV*\n"
            f"{H}\n\n"
            f"Mobilographer  ·  Developer  ·  AI Expert\n\n"
            f"Hello\\! I am Abdulloh's personal AI assistant\\.\n"
            f"Choose a section from the menu or ask me anything\\!\n\n"
            f"🤖 _I can tell you everything about Abdulloh\\._"
        ),
        "menu": "Use the menu below 👇",
        "about": (
            f"{H}\n"
            f"👤  *ABOUT ME*\n"
            f"{H}\n\n"
            f"Abdulloh is an 18\\-year\\-old specialist at the\n"
            f"intersection of modern tech and visual arts\\.\n\n"
            f"🏛  *Education:* Nordic University \\(Economics, 1st year\\)\n"
            f"📍  *Location:* Tashkent, Uzbekistan\n"
            f"🥋  *Sports:* Taekwondo — 5 years \\(Medal winner\\)\n"
            f"🌍  *Languages:* Uzbek \\| English \\(IELTS 5\\.5\\) \\| Russian\n\n"
            f"_He doesn't just write code — he brings frames to life\\!_"
        ),
        "experience": (
            f"{H}\n"
            f"💼  *PROFESSIONAL EXPERIENCE*\n"
            f"{H}\n\n"
        ),
        "skills": (
            f"{H}\n"
            f"🛠  *MASTERY \\& SKILLS*\n"
            f"{H}\n\n"
        ),
        "education": (
            f"{H}\n"
            f"🎓  *EDUCATION*\n"
            f"{H}\n\n"
            f"🏛  *Institution:* Nordic University\n"
            f"📖  *Major:* Economics\n"
            f"⏳  *Year:* 1st\\-year student\n\n"
            f"📐 *Extra:* 1\\.5 years of advanced mathematics studies\\."
        ),
        "portfolio": (
            f"{H}\n"
            f"📁  *VISUAL PORTFOLIO*\n"
            f"{H}\n\n"
            f"View Abdulloh's creative works by category\\."
        ),
        "contact": (
            f"{H}\n"
            f"📞  *CONTACT INFORMATION*\n"
            f"{H}\n\n"
            f"Get in touch with Abdulloh directly:"
        ),
        "buttons": {
            "about": "👤 About Me",
            "experience": "💼 Experience",
            "skills": "🛠 Skills",
            "education": "🎓 Education",
            "portfolio": "📁 Portfolio",
            "contact": "📞 Contact",
            "lang": "🌐 Language / Til",
            "hire": "💼 Hire Me",
            "mini_app": "🚀 Web CV"
        }
    }
}

# Portfolio category details (used by handlers)
PORTFOLIO_DATA = {
    "mob": {
        "uz": "📸  *Mobilografiya*\n\nProfessional video kontentlar, reklamalar va kreativ loyihalar\\.\nTajriba: 1\\.5 yil\\.\n\n👉 To'liq ishlar: @upgcard",
        "ru": "📸  *Мобилография*\n\nПрофессиональный видеоконтент, рекламы и креативные проекты\\.\nОпыт: 1\\.5 года\\.\n\n👉 Все работы: @upgcard",
        "en": "📸  *Mobilography*\n\nProfessional video content, ads, and creative projects\\.\nExperience: 1\\.5 years\\.\n\n👉 Full works: @upgcard"
    },
    "code": {
        "uz": f"💻  *Web \\& Telegram Bots*\n\n{DOT} CV Bot \\(aynan shu bot\\)\n{DOT} Smart Balance Mini App\n{DOT} Arenda Bot\n\n👉 Telegram: @abdulloh\\_ai",
        "ru": f"💻  *Web \\& Telegram Боты*\n\n{DOT} CV Bot \\(этот самый бот\\)\n{DOT} Smart Balance Mini App\n{DOT} Arenda Bot\n\n👉 Telegram: @abdulloh\\_ai",
        "en": f"💻  *Web \\& Telegram Bots*\n\n{DOT} CV Bot \\(this very bot\\)\n{DOT} Smart Balance Mini App\n{DOT} Arenda Bot\n\n👉 Telegram: @abdulloh\\_ai"
    },
    "ai": {
        "uz": "🤖  *AI \\& SMM*\n\nAI yordamida kontent yaratish, post dizayn,\nvideo ishlab chiqish\\.\nSMM tajribasi: 5 oy\\.\n\n👉 Instagram: abdullokh\\_mk",
        "ru": "🤖  *AI \\& SMM*\n\nСоздание контента с помощью AI, дизайн постов,\nвидеопроизводство\\.\nОпыт SMM: 5 месяцев\\.\n\n👉 Instagram: abdullokh\\_mk",
        "en": "🤖  *AI \\& SMM*\n\nAI\\-powered content creation, post design,\nvideo production\\.\nSMM experience: 5 months\\.\n\n👉 Instagram: abdullokh\\_mk"
    },
    "car": {
        "uz": "🚗  *Car Detailing*\n\nTanirovka, broniplyonka va laminatsiya\nbo'yicha professional tajriba\\.\nTajriba: 1 yil\\.",
        "ru": "🚗  *Детейлинг Авто*\n\nПрофессиональный опыт в тонировке,\nбронепленке и ламинации\\.\nОпыт: 1 год\\.",
        "en": "🚗  *Car Detailing*\n\nProfessional experience in car tinting,\nprotective film, and lamination\\.\nExperience: 1 year\\."
    }
}
