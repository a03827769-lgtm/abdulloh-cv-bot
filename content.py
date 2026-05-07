"""
EXECUTIVE DIGITAL IDENTITY - ABDULLOH MUHAMMADJONOV v5.0
Theme: Elite, Multidisciplinary, Result-Oriented
"""

H = "──────────────────────────"

def esc(text: str) -> str:
    """Safe MarkdownV2 escaping."""
    if not text: return ""
    chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    res = str(text)
    for c in chars:
        res = res.replace(c, f'\\{c}')
    return res

CV_DATA = {
    "name": "Abdulloh Muhammadjonov",
    "title": "Creative Technologist | SMM Specialist | AI Architect",
    "age": 18,
    "location": "Tashkent, Uzbekistan",
    "philosophy": {
        "uz": "◈ *Falsafa:* 'Men texnologiya va san'atning kesishish nuqtasida ishlayman. Maqsadim — AI orqali bizneslarni avtomatlashtirish va cinematic vizuallar orqali brendlarni yangi bosqichga olib chiqish.'",
        "ru": "◈ *Философия:* 'Я работаю на стыке технологий и искусства. Моя цель — автоматизировать бизнес через AI и выводить бренды на новый уровень с помощью кинематографичного визуала.'",
        "en": "◈ *Philosophy:* 'I work at the intersection of technology and art. My goal is to automate businesses via AI and elevate brands to new heights through cinematic visuals.'"
    },
    "usp": {
        "uz": "Gen-Z ijodkorining tezkorligi, SMM strategiyasining chuqurligi va AI muhandisining aniqligi.",
        "ru": "Скорость креатора Gen-Z, глубина SMM-стратегии и точность AI-инженера.",
        "en": "The agility of a Gen-Z creator, the depth of an SMM strategy, and the precision of an AI engineer."
    },
    "contacts": {
        "phone": "+998 88 788 70 11",
        "email": "abdullohmuhammadjonov777@gmail.com",
        "telegram": "@abdulloh_ai",
        "instagram": "abdullokh_mk",
        "portfolio_channel": "t.me/upgcard",
        "instagram_url": "https://www.instagram.com/abdullokh_mk",
        "domain": "abdullohvfx.online"
    },
    "education": [
        {
            "institution": "Nordic University",
            "major": "Economics",
            "period": "2025 - Present",
            "details": "1st year student, focusing on Digital Economy and Market Trends."
        },
        {
            "institution": "Proweb Learning Center",
            "major": "Web Development (Offline)",
            "period": "1 Year",
            "details": "Professional training in HTML, CSS, JavaScript, and React. Certificate obtained."
        },
        {
            "institution": "IT Park Uzbekistan",
            "major": "Professional Video Editing",
            "period": "6 Months",
            "details": "Advanced course in cinematic editing and motion design."
        }
    ],
    "experience": [
        {
            "title": "Freelance SMM & Content Creator",
            "duration": "1.5+ Years",
            "desc": {
                "uz": "100+ dan ortiq cinematic reels va reklama roliklari yaratish. 'Aka-uka Tanirovka' va boshqa brendlar uchun SMM strategiyalari.",
                "ru": "Создание 100+ кинематографичных рилсов и рекламных роликов. SMM-стратегии для 'Aka-uka Tanirovka' и других брендов.",
                "en": "Creating 100+ cinematic reels and commercials. SMM strategies for brands like 'Aka-uka Tanirovka' and others."
            }
        },
        {
            "title": "AI Bot Architect & Developer",
            "duration": "1 Year",
            "desc": {
                "uz": "'Tozalash Servis' uchun to'liq funksional AI-buyurtma botini yaratish. Biznes jarayonlarini avtomatlashtirish bo'yicha ekspert.",
                "ru": "Создание полнофункционального AI-бота для приема заказов для 'Tozalash Servis'. Эксперт по автоматизации бизнес-процессов.",
                "en": "Developing a fully functional AI ordering bot for 'Tozalash Servis'. Expert in business process automation."
            }
        }
    ],
    "projects": [
        {
            "name": "Tozalash Servis Bot",
            "url": "https://t.me/tozalash_servisbot",
            "uz": "Mijozlardan buyurtma oladigan va AI yordamida muloqot qiladigan mukammal tizim.",
            "en": "A perfect system that takes orders and communicates using AI."
        },
        {
            "name": "Aka-Uka Tanirovka",
            "type": "Full SMM Service",
            "uz": "Brendning vizual identifikatsiyasi va ijtimoiy tarmoqlardagi faolligini oshirish.",
            "en": "Visual identity and social media growth strategy for the brand."
        }
    ],
    "skills": {
        "visual": ["Reels Production", "Commercial Video", "Auto Content", "Vlog Editing", "Color Grading (CapCut/VN)"],
        "tech": ["Python (Bot Dev)", "HTML/CSS", "JavaScript", "React", "AI Prompt Engineering"],
        "ai": ["ChatGPT", "Midjourney", "Leonardo AI", "Runway", "Kling"],
        "smm": ["Content Plan", "Idea Generation", "Copywriting", "Page Management", "Telegram Growth"]
    },
    "achievements": {
        "sports": "Taekwondo - Highest belt level, 5-time City level medalist.",
        "certs": ["IELTS (Speaking high)", "Web Development (Proweb)", "Video Editing (IT Park)"]
    }
}

MESSAGES = {
    "uz": {
        "start": (
            f"✦ *ELITE DIGITAL ECOSYSTEM: ABDULLOH*\n"
            f"{H}\n\n"
            f"Salom! Men Abdulloh Muhammadjonovning raqamli strategiman\\. "
            f"Biznesingizni AI orqali avtomatlashtirish yoki premium vizuallar yaratish vaqti keldi\\.\n\n"
            f"◈ *Sizga qanday yordam bera olaman?*"
        ),
        "menu": f"✦ *Asosiy Menyuga xush kelibsiz*\n{H}\n\nO'zingizni qiziqtirgan bo'limni tanlang:",
        "about": (
            f"✦ *BRAND IDENTITY*\n"
            f"{H}\n\n"
            f"👤 *Abdulloh Muhammadjonov* \\(18 yosh\\)\n"
            f"🎓 *Nordic University* iqtisodchisi\n"
            f"🥋 *Taekwondo* ustasi \\(5 karra sovrindor\\)\n\n"
            f"{CV_DATA['philosophy']['uz']}\n\n"
            f"◈ *Slogan:* 'Innovatsiya va Estetika uyg'unligi\\.'"
        ),
        "portfolio": f"✦ *PORTFOLIO & ISHLAR*\n{H}\n\nQuyidagi yo'nalishlar bo'yicha tajribamizni ko'ring:",
        "faq": (
            f"✦ *SAVOL-JAVOBLAR*\n"
            f"{H}\n\n"
            f"◈ *Xizmatlar narxi qancha?*\n"
            f"Har bir loyiha uning murakkabligidan kelib chiqib individual narxlanadi\\. Biznes qiymati doim ustuvor\\.\n\n"
            f"◈ *SMM xizmatiga nimalar kiradi?*\n"
            f"Strategiya, suratga olish, montaj va sahifa yuritish — hammasi ichida\\.\n\n"
            f"◈ *Botni qanchada yasaysiz?*\n"
            f"Oddiy botlar 3\\-5 kun, murakkab AI tizimlar 2 hafta va undan ko'proq\\."
        ),
        "contact": (
            f"✦ *BOG'LANISH*\n"
            f"{H}\n\n"
            f"📞 *Tel:* {esc(CV_DATA['contacts']['phone'])}\n"
            f"📧 *Email:* {esc(CV_DATA['contacts']['email'])}\n"
            f"🌐 *Web:* {esc(CV_DATA['contacts']['domain'])}\n\n"
            f"Loyiha muhokamasi uchun istalgan kanal orqali yozishingiz mumkin\\."
        ),
        "lang_select": "🌐 *Muloqot tilini tanlang:*",
        "ai_intro": (
            f"✦ *AI STRATEG BILAN MULOQOT*\n"
            f"{H}\n\n"
            f"Savollaringizni yo'llang\\. Men Abdullohning barcha tajribasi: SMM, Mobilografiya va Dasturlash bo'yicha sizga maslahat beraman\\."
        ),
        "buttons": {
            "about": "💎 Brend",
            "experience": "💼 Tajriba",
            "skills": "🛠 Mahorat",
            "portfolio": "📁 Portfolio",
            "contact": "📞 Kontakt",
            "lang": "🌐 Til",
            "hire": "🤝 Hamkorlik",
            "mini_app": "🚀 Web Experience",
            "ai_chat": "🤖 AI Konsultant",
            "faq": "❓ FAQ",
            "back": "⬅️ Ortga"
        }
    },
    "ru": {
        "start": (
            f"✦ *ELITE DIGITAL ECOSYSTEM: ABDULLOH*\n"
            f"{H}\n\n"
            f"Привет! Я цифровой стратег Абдуллоха Мухаммаджонова\\. "
            f"Пришло время автоматизировать ваш бизнес через AI или создать премиальный визуал\\.\n\n"
            f"◈ *Чем я могу вам помочь?*"
        ),
        "menu": f"✦ *Главное Меню*\n{H}\n\nВыберите раздел:",
        "about": (
            f"✦ *BRAND IDENTITY*\n"
            f"{H}\n\n"
            f"👤 *Абдуллох Мухаммаджонов* \\(18 лет\\)\n"
            f"🎓 *Nordic University* \\(Экономика\\)\n"
            f"🥋 *Тхэквондо* \\(5\\-кратный медалист\\)\n\n"
            f"{CV_DATA['philosophy']['ru']}"
        ),
        "portfolio": f"✦ *ПОРТФОЛИО*\n{H}\n\nНаши проекты:",
        "faq": (
            f"✦ *ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ*\n"
            f"{H}\n\n"
            f"◈ *Цены?*\nИндивидуально для каждого проекта\\.\n\n"
            f"◈ *AI Боты?*\nРазработка от 5 дней\\."
        ),
        "contact": (
            f"✦ *КОНТАКТЫ*\n"
            f"{H}\n\n"
            f"📞 {esc(CV_DATA['contacts']['phone'])}\n"
            f"📧 {esc(CV_DATA['contacts']['email'])}\n"
            f"🌐 {esc(CV_DATA['contacts']['domain'])}"
        ),
        "lang_select": "🌐 *Выберите язык:*",
        "ai_intro": "✦ *ЧАТ С AI КОНСУЛЬТАНТОМ*\n{H}\n\nЗадавайте любые вопросы по SMM, видео или ботам\\.",
        "buttons": {
            "about": "💎 Бренд",
            "experience": "💼 Опыт",
            "skills": "🛠 Навыки",
            "portfolio": "📁 Проекты",
            "contact": "📞 Контакты",
            "lang": "🌐 Язык",
            "hire": "🤝 Партнерство",
            "mini_app": "🚀 Web Experience",
            "ai_chat": "🤖 AI Консультант",
            "faq": "❓ FAQ",
            "back": "⬅️ Назад"
        }
    },
    "en": {
        "start": (
            f"✦ *ELITE DIGITAL ECOSYSTEM: ABDULLOH*\n"
            f"{H}\n\n"
            f"Hello! I am Abdulloh Muhammadjonov's digital strategist\\. "
            f"It's time to automate your business with AI or create premium visuals\\.\n\n"
            f"◈ *How can I assist you?*"
        ),
        "menu": f"✦ *Main Menu activated*\n{H}\n\nExplore our sections:",
        "about": (
            f"✦ *BRAND IDENTITY*\n"
            f"{H}\n\n"
            f"👤 *Abdulloh Muhammadjonov* \\(18 years old\\)\n"
            f"🎓 *Nordic University* \\(Economics\\)\n"
            f"🥋 *Taekwondo* \\(5\\-time Medalist\\)\n\n"
            f"{CV_DATA['philosophy']['en']}"
        ),
        "portfolio": f"✦ *PORTFOLIO*\n{H}\n\nCheck our latest work:",
        "faq": (
            f"✦ *FAQ*\n"
            f"{H}\n\n"
            f"◈ *Pricing?*\nCustom based on value and complexity\\.\n\n"
            f"◈ *Services?*\nAI Bots, Cinematic Visuals, and SMM Architecture\\."
        ),
        "contact": (
            f"✦ *CONNECT*\n"
            f"{H}\n\n"
            f"📞 {esc(CV_DATA['contacts']['phone'])}\n"
            f"📧 {esc(CV_DATA['contacts']['email'])}\n"
            f"🌐 {esc(CV_DATA['contacts']['domain'])}"
        ),
        "lang_select": "🌐 *Choose your language:*",
        "ai_intro": "✦ *AI CONSULTANT CHAT*\n{H}\n\nAsk me anything about SMM, Video Production, or AI Systems\\.",
        "buttons": {
            "about": "💎 Brand",
            "experience": "💼 Experience",
            "skills": "🛠 Skills",
            "portfolio": "📁 Projects",
            "contact": "📞 Connect",
            "lang": "🌐 Language",
            "hire": "🤝 Hire Me",
            "mini_app": "🚀 Web Experience",
            "ai_chat": "🤖 AI Strategist",
            "faq": "❓ FAQ",
            "back": "⬅️ Back"
        }
    }
}

PORTFOLIO_DATA = {
    "mob": {
        "uz": "📸 *VISUAL ARTS & MOBILOGRAPHY*\n\nMen CapCut va VN orqali cinematic asarlar yarataman\\. Har bir kadr brendingiz darajasini ko'rsatadi\\.\n\n◈ *Yo'nalishlar:* Reels, Reklama, Restoran/Cafe, Avto, Vlog\\.",
        "ru": "📸 *ВИЗУАЛЬНОЕ ИСКУССТВО*\n\nСоздаю кинематографичные рилсы в CapCut/VN\\. Каждый кадр работает на ваш статус\\.\n\n◈ *Направления:* Reels, Реклама, Рестораны, Авто, Влоги\\.",
        "en": "📸 *VISUAL ARTS & MOBILOGRAPHY*\n\nCrafting cinematic masterpieces using CapCut/VN\\. Every frame elevates your brand status\\.\n\n◈ *Specialties:* Reels, Ads, Restaurant, Auto, Vlogs\\."
    },
    "code": {
        "uz": "💻 *WEB & BOT DEVELOPMENT*\n\nMurakkab botlar va professional veb-saytlar yaratish bo'yicha Proweb va IT Park tajribasi\\.\n\n◈ *Yechimlar:* AI Bots, CRM Systems, Portfolio Websites\\.",
        "ru": "💻 *WEB & BOT DEVELOPMENT*\n\nОпыт Proweb и IT Park в создании сложных ботов и профессиональных сайтов\\.",
        "en": "💻 *WEB & BOT DEVELOPMENT*\n\nLeveraging Proweb and IT Park expertise to build complex bots and professional websites\\."
    }
}

MEDIA = {
    "start": "https://images.unsplash.com/photo-1512756783935-7c8d9d499acd",
    "about": "https://images.unsplash.com/photo-1499951360447-b19be8fe80f5",
    "mobilography": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
}
