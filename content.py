"""CV content data with Professional Case Studies and FAQ."""

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
    "projects": [
        {
            "name": "UPG Card",
            "type": "Production",
            "uz": "◈ *Muammo:* Mijozlar uchun portfoliosini ko'rsatish murakkab edi.\n◈ *Yechim:* Premium vizitka va bot tizimi yaratildi.\n◈ *Natija:* 50+ mijozlar oqimi.",
            "ru": "◈ *Проблема:* Сложность в демонстрации портфолио.\n◈ *Решение:* Создана система премиум-визиток и ботов.\n◈ *Результат:* Поток из 50+ клиентов.",
            "en": "◈ *Problem:* Difficulty in showcasing portfolios.\n◈ *Solution:* Premium business card and bot system created.\n◈ *Result:* Inflow of 50+ clients."
        },
        {
            "name": "Smart Balance",
            "type": "AI System",
            "uz": "◈ *Muammo:* Moliya boshqaruvida inson omili xatolari.\n◈ *Yechim:* AI integratsiyali Mini App tizimi.\n◈ *Natija:* 99% hisob-kitob aniqligi.",
            "ru": "◈ *Проблема:* Человеческий фактор в финансах.\n◈ *Решение:* Mini App с AI интеграцией.\n◈ *Результат:* 99% точность расчетов.",
            "en": "◈ *Problem:* Human error in finance management.\n◈ *Solution:* AI-integrated Mini App system.\n◈ *Result:* 99% calculation accuracy."
        }
    ],
    "experience": [
        {"title": "Mobilographer & Director", "duration": "1.5 Years"},
        {"title": "Full-Stack Developer", "duration": "1 Year"},
        {"title": "SMM Strategist", "duration": "5 Months"},
        {"title": "Car Detailing Expert", "duration": "1 Year"}
    ],
    "skills": {
        "technical": ["Mobilography", "Python (AI/FastAPI)", "React", "SMM"],
        "soft": ["Leadership", "Analytical Thinking", "Creativity"]
    }
}

FAQ_DATA = {
    "uz": (
        f"✦ *KO'P BERILADIGAN SAVOLLAR*\n"
        f"──────────────────────────\n\n"
        f"◈ *Qaysi dasturlarda ishlaysiz?*\n"
        f"└ Adobe Premiere, CapCut, Python (Aiogram/FastAPI), React\\.\n\n"
        f"◈ *Hamkorlik shartlari qanday?*\n"
        f"└ Har bir loyiha individual yondashuv va shartnoma asosida kelishiladi\\.\n\n"
        f"◈ *Ish vaqtingiz?*\n"
        f"└ Moslashuvchan grafik, asosan 10:00 — 20:00\\.\n\n"
        f"◈ *Siz bilan qanday bog'lanish mumkin?*\n"
        f"└ Botdagi 'Aloqa' bo'limi yoki to'g'ridan-to'g'ri @abdulloh\\_ai orqali\\."
    ),
    "ru": (
        f"✦ *ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ*\n"
        f"──────────────────────────\n\n"
        f"◈ *В каких программах работаете?*\n"
        f"└ Adobe Premiere, CapCut, Python, React\\.\n\n"
        f"◈ *Условия сотрудничества?*\n"
        f"└ Каждый проект обсуждается индивидуально на основе договора\\.\n\n"
        f"◈ *График работы?*\n"
        f"└ Гибкий график, в основном 10:00 — 20:00\\.\n\n"
        f"◈ *Как с вами связаться?*\n"
        f"└ Через раздел 'Контакты' или напрямую @abdulloh\\_ai\\."
    ),
    "en": (
        f"✦ *FREQUENTLY ASKED QUESTIONS*\n"
        f"──────────────────────────\n\n"
        f"◈ *What software do you use?*\n"
        f"└ Adobe Premiere, CapCut, Python, React\\.\n\n"
        f"◈ *What are the cooperation terms?*\n"
        f"└ Each project is negotiated individually based on a contract\\.\n\n"
        f"◈ *Working hours?*\n"
        f"└ Flexible schedule, mainly 10:00 AM — 8:00 PM\\.\n\n"
        f"◈ *How to contact you?*\n"
        f"└ Through the 'Contact' section or directly via @abdulloh\\_ai\\."
    )
}

# ━━━━━━━━━━━━━━━━━━━━
# MEDIA & FORMATTING (Kept for compatibility)
# ━━━━━━━━━━━━━━━━━━━━

MEDIA = {
    "start": "https://images.unsplash.com/photo-1517694712202-14dd9538aa97",
    "about": "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d",
    "mobilography": "https://v1.pinimg.com/videos/mc/720p/f1/8c/6b/f18c6b7d3453716d1f568a86576b5d9d.mp4",
}

H = "──────────────────────────"

MESSAGES = {
    "uz": {
        "start": (
            f"✦ *MUHAMMADJONOV ABDULLOH*\n"
            f"{H}\n\n"
            f"Creative Director  ·  Developer  ·  AI Engineer\n\n"
            f"Assalomu alaykum\\. Abdullohning raqamli ekotizimiga xush kelibsiz\\.\n"
            f"Sizga qanday yordam bera olaman?"
        ),
        "menu": "Pastdagi menyudan foydalaning ⬦",
        "about": (
            f"✦ *PERSONAL PROFILE*\n"
            f"{H}\n\n"
            f"Abdulloh — texnologiya va vizual san'at chegarasida ishlovchi mutaxassis\\.\n\n"
            f"◈ *Ta'lim:* Nordic University\n"
            f"◈ *Manzil:* Toshkent, O'zbekiston\n"
            f"◈ *Yutuq:* Taekwondo — 5 yillik intizom va medallar\n\n"
            f"_Sifat — bu bizning asosiy tamoyilimiz\\._"
        ),
        "portfolio": (
            f"✦ *VISUAL PORTFOLIO*\n"
            f"{H}\n\n"
            f"Loyihalarni kategoriyalar bo'yicha tanlang:"
        ),
        "contact": (
            f"✦ *CONNECT*\n"
            f"{H}\n\n"
            f"Hamkorlik yoki savollar uchun aloqaga chiqing:"
        ),
        "ai_intro": (
            f"🤖 *AI YORDAMCHI REJIMIDA*\n"
            f"{H}\n\n"
            f"Men Abdullohning barcha loyihalari va tajribasi haqida ma'lumotga egaman\\.\n"
            f"Menga xohlagan savolingizni berishingiz mumkin\\.\n\n"
            f"_Chiqish uchun 'Ortga' tugmasini bosing\\._"
        ),
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
            "faq": "❓ FAQ"
        }
    },
    "ru": {
        "start": (
            f"✦ *МУХАММАДЖОНОВ АБДУЛЛОХ*\n"
            f"{H}\n\n"
            f"Креативный директор  ·  Разработчик  ·  AI Инженер\n\n"
            f"Добро пожаловать в цифровую экосистему Абдуллоха\\.\n"
            f"Чем я могу вам помочь?"
        ),
        "menu": "Используйте меню ниже ⬦",
        "about": (
            f"✦ *ПЕРСОНАЛЬНЫЙ ПРОФИЛЬ*\n"
            f"{H}\n\n"
            f"Абдуллох — специалист, работающий на стыке технологий и искусства\\.\n\n"
            f"◈ *Учеба:* Nordic University\n"
            f"◈ *Локация:* Ташкент, Узбекистан\n"
            f"◈ *Спорт:* Тхэквондо — 5 лет дисциплины и медалей\n\n"
            f"_Качество — наш главный принцип\\._"
        ),
        "portfolio": (
            f"✦ *ПОРТФОЛИО*\n"
            f"{H}\n\n"
            f"Выберите категорию проектов:"
        ),
        "contact": (
            f"✦ *СВЯЗЬ*\n"
            f"{H}\n\n"
            f"Свяжитесь для сотрудничества или вопросов:"
        ),
        "ai_intro": (
            f"🤖 *РЕЖИМ AI ПОМОЩНИКА*\n"
            f"{H}\n\n"
            f"Я знаю всё о проектах и опыте Абдуллоха\\.\n"
            f"Вы можете задать мне любой вопрос\\.\n\n"
            f"_Для выхода нажмите 'Назад'\\._"
        ),
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
            "faq": "❓ FAQ"
        }
    },
    "en": {
        "start": (
            f"✦ *ABDULLOH MUHAMMADJONOV*\n"
            f"{H}\n\n"
            f"Creative Director  ·  Developer  ·  AI Engineer\n\n"
            f"Welcome to Abdulloh's digital ecosystem\\.\n"
            f"How may I assist you today?"
        ),
        "menu": "Use the menu below ⬦",
        "about": (
            f"✦ *PERSONAL PROFILE*\n"
            f"{H}\n\n"
            f"Abdulloh is a specialist working at the edge of tech and visual arts\\.\n\n"
            f"◈ *Education:* Nordic University\n"
            f"◈ *Location:* Tashkent, Uzbekistan\n"
            f"◈ *Achievements:* 5 years of Taekwondo discipline\n\n"
            f"_Quality is our primary principle\\._"
        ),
        "portfolio": (
            f"✦ *PORTFOLIO*\n"
            f"{H}\n\n"
            f"Select a project category:"
        ),
        "contact": (
            f"✦ *CONNECT*\n"
            f"{H}\n\n"
            f"Get in touch for collaboration or inquiries:"
        ),
        "ai_intro": (
            f"🤖 *AI ASSISTANT MODE*\n"
            f"{H}\n\n"
            f"I have full knowledge of Abdulloh's projects and experience\\.\n"
            f"Feel free to ask me anything\\.\n\n"
            f"_Click 'Back' to exit AI mode\\._"
        ),
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
            "faq": "❓ FAQ"
        }
    }
}

PORTFOLIO_DATA = {
    "mob": {
        "uz": "📸 *Mobilografiya*\n\n◈ *Project:* Cinematic Ad\n◈ *Muammo:* Mahsulotni dinamik ko'rsatish kerak edi.\n◈ *Natija:* Sifatli kadrlar va brend taniluvchanligi oshishi.",
        "ru": "📸 *Мобилография*\n\n◈ *Проект:* Cinematic Ad\n◈ *Проблема:* Нужна динамика продукта.\n◈ *Результат:* Рост узнаваемости бренда.",
        "en": "📸 *Mobilography*\n\n◈ *Project:* Cinematic Ad\n◈ *Problem:* Product needed dynamic visuals.\n◈ *Result:* High quality frames and brand awareness."
    },
    "code": {
        "uz": "💻 *Development*\n\n◈ CV Bot (Master Level)\n◈ Smart Balance App (AI)\n◈ Arenda Bot Infrastructure",
        "ru": "💻 *Разработка*\n\n◈ CV Bot (Master Level)\n◈ Smart Balance App (AI)\n◈ Arenda Bot Infrastructure",
        "en": "💻 *Development*\n\n◈ CV Bot (Master Level)\n◈ Smart Balance App (AI)\n◈ Arenda Bot Infrastructure"
    },
    "ai": {
        "uz": "🤖 *AI Solutions*\n\n◈ AI Content Creation\n◈ Post Design & Strategy",
        "ru": "🤖 *AI Решения*\n\n◈ AI Создание контента\n◈ Пост-дизайн и стратегия",
        "en": "🤖 *AI Solutions*\n\n◈ AI Content Creation\n◈ Post Design & Strategy"
    },
    "car": {
        "uz": "🚗 *Automotive*\n\n◈ Detailing & Protection\n◈ Professional Experience: 1 year",
        "ru": "🚗 *Автомобили*\n\n◈ Детейлинг и защита\n◈ Профессиональный опыт: 1 год",
        "en": "🚗 *Automotive*\n\n◈ Detailing & Protection\n◈ Professional Experience: 1 year"
    }
}
