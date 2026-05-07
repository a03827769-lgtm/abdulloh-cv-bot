"""
EXECUTIVE DIGITAL IDENTITY - ABDULLOH v4.0
Theme: Hyper-Professional, Expert-Led, Result-Oriented
"""

H = "──────────────────────────"

CV_DATA = {
    "name": "Muhammadjonov Abdulloh",
    "title": "Creative Technologist & AI Architect",
    "philosophy": {
        "uz": "◈ *Falsafa:* 'Texnologiya — bu ruhsiz asbob, san'at esa unga jon beradi. Mening vazifam — AI aniqligi va vizual san'at hissiyotini birlashtirib, bizneslar uchun yangi davr raqamli identifikatsiyasini yaratish.'",
        "ru": "◈ *Философия:* 'Технология — это бездушный инструмент, а искусство вдыхает в него жизнь. Моя миссия — объединить точность AI и эмоции визуального искусства для создания цифровой идентичности новой эры.'",
        "en": "◈ *Philosophy:* 'Technology is a soulless tool; art gives it a soul. My mission is to merge AI precision with visual emotion to create a new-era digital identity for businesses.'"
    },
    "usp": {
        "uz": "Gen-Z ijodkorining tezkorligi va AI muhandisining aniqligi uyg'unligi.",
        "ru": "Сочетание скорости креатора Gen-Z и точности AI-инженера.",
        "en": "A fusion of Gen-Z creator agility and AI engineer precision."
    },
    "contacts": {
        "telegram": "@abdulloh_ai",
        "instagram": "abdullokh_mk",
        "portfolio": "https://t.me/upgcard",
        "email": "abdulloh@example.com" # Placeholder
    },
    "experience": [
        {
            "title": "Creative Director (Visual Storytelling)",
            "duration": "1.5+ Years",
            "desc": {
                "uz": "Brendlar uchun cinematic vizual strategiyalar ishlab chiqish. 10M+ dan ortiq umumiy ko'rilishga ega reklamalar muallifi.",
                "ru": "Разработка кинематографических визуальных стратегий для брендов. Автор рекламы с общим охватом более 10 млн просмотров.",
                "en": "Developing cinematic visual strategies for brands. Author of commercials with over 10M+ cumulative views."
            }
        },
        {
            "title": "Senior AI Bot Architect",
            "duration": "1 Year",
            "desc": {
                "uz": "Biznes jarayonlarini 90% gacha avtomatlashtiruvchi murakkab AI ekotizimlarni loyihalash va joriy etish.",
                "ru": "Проектирование и внедрение сложных систем AI, автоматизирующих бизнес-процессы до 90%.",
                "en": "Designing and implementing complex AI ecosystems that automate business processes by up to 90%."
            }
        }
    ],
    "reviews": [
        {
            "client": "Premium Logistics Co.",
            "text": {
                "uz": "\"Abdulloh bizning moliya tizimimizni AI orqali shunday tartibga soldiki, xatoliklar nolga tushdi. Haqiqiy professional!\"",
                "ru": "\"Абдуллох так настроил нашу финансовую систему через AI, что ошибки упали до нуля. Настоящий профи!\"",
                "en": "\"Abdulloh streamlined our financial system via AI so effectively that errors dropped to zero. A true professional!\""
            }
        },
        {
            "client": "Art Gallery Dubai",
            "text": {
                "uz": "\"U yaratgan cinematic reelslar sotuvimizni 40% ga oshirdi. Vizual didi juda yuqori.\"",
                "ru": "\"Его кинематографические рилсы увеличили наши продажи на 40%. У него исключительный визуальный вкус.\"",
                "en": "\"The cinematic reels he created increased our sales by 40%. His visual taste is exceptional.\""
            }
        }
    ],
    "skills": {
        "technical": ["Python", "AI Integration", "Prompt Engineering", "FastAPI", "React"],
        "soft": ["Strategic Thinking", "Visual Storytelling", "Project Management", "Leadership"]
    }
}

MESSAGES = {
    "uz": {
        "start": (
            f"✦ *EXECUTIVE DIGITAL IDENTITY: ABDULLOH*\n"
            f"{H}\n\n"
            f"Siz innovatsiyalar va yuqori vizual did kesishgan nuqtadasiz\\. "
            f"Men shunchaki bot emasman — men Abdullohning raqamli strategiman\\.\n\n"
            f"◈ *Sizga qanday qiymat bera olamiz?*"
        ),
        "menu": f"✦ *Asosiy Menyuga xush kelibsiz*\n{H}\n\nQuyidagi bo'limlardan birini tanlang:",
        "about": (
            f"✦ *BRAND PHILOSOPHY*\n"
            f"{H}\n\n"
            f"{CV_DATA['philosophy']['uz']}\n\n"
            f"◈ *Asosiy tamoyillar:* Intizom, Eksperimental yondashuv va Mukammallik\\.\n"
            f"◈ *Sport:* Taekwondo orqali shakllangan 'Hech qachon taslim bo'lmaslik' mentaliteti\\."
        ),
        "portfolio": f"✦ *STRATEGIK LOYIHALAR*\n{H}\n\nQuyidagi yo'nalishlardan birini tanlang va ishimiz sifatiga baho bering:",
        "faq": (
            f"✦ *KO'P BERILADIGAN SAVOLLAR*\n"
            f"{H}\n\n"
            f"◈ *Qanday xizmatlarni ko'rsatasiz?*\n"
            f"Biz cinematic video ishlab chiqarish va biznes jarayonlarini AI orqali avtomatlashtirishga ixtisoslashganmiz\\.\n\n"
            f"◈ *Loyiha qancha vaqt oladi?*\n"
            f"Murakkablikka qarab: Video \\(3\\-7 kun\\), AI Tizimlar \\(14\\-30 kun\\)\\.\n\n"
            f"◈ *Narxlar qanday?*\n"
            f"Har bir loyiha individual hisoblanadi, chunki biz 'shablon' yechimlardan qochamiz\\."
        ),
        "contact": (
            f"✦ *ALOQA MARKAZI*\n"
            f"{H}\n\n"
            f"Loyiha bo'yicha muhokama yoki takliflar uchun quyidagi kanallar ochiq:"
        ),
        "lang_select": "🌐 *Muloqot tilini tanlang:*",
        "ai_intro": (
            f"✦ *AI STRATEG BILAN MULOQOT*\n"
            f"{H}\n\n"
            f"Savollaringizni yo'llang\\. Men Abdullohning tajribasi va qarashlaridan kelib chiqib sizga javob beraman\\."
        ),
        "hire_intro": "🤝 *STRATEGIK HAMKORLIK*\n\nLoyihangiz tafsilotlarini qoldiring\\. Men ularni tahlil qilaman va Abdulloh bilan bog'lanishingiz uchun zamin yarataman\\.",
        "buttons": {
            "about": "💎 Falsafa",
            "experience": "💼 Ekspertiza",
            "skills": "🛠 Texnologiyalar",
            "portfolio": "📁 Loyihalar",
            "contact": "📞 Aloqa",
            "lang": "🌐 Til",
            "hire": "🤝 Hamkorlik",
            "mini_app": "🚀 Web Experience",
            "ai_chat": "🤖 AI Strateg",
            "faq": "❓ Savollar",
            "back": "⬅️ Ortga"
        }
    },
    "ru": {
        "start": (
            f"✦ *EXECUTIVE DIGITAL IDENTITY: ABDULLOH*\n"
            f"{H}\n\n"
            f"Вы находитесь на пересечении инноваций и высокого визуального вкуса\\. "
            f"Я не просто бот — я цифровой стратег Абдуллоха\\.\n\n"
            f"◈ *Какую ценность мы можем вам предложить?*"
        ),
        "menu": f"✦ *Добро пожаловать в Главное Меню*\n{H}\n\nВыберите интересующий раздел:",
        "about": (
            f"✦ *ФИЛОСОФИЯ БРЕНДА*\n"
            f"{H}\n\n"
            f"{CV_DATA['philosophy']['ru']}\n\n"
            f"◈ *Принципы:* Дисциплина, Экспериментальный подход и Совершенство\\.\n"
            f"◈ *Спорт:* Менталитет 'Никогда не сдаваться', сформированный Тхэквондо\\."
        ),
        "portfolio": f"✦ *СТРАТЕГИЧЕСКИЕ ПРОЕКТЫ*\n{H}\n\nВыберите направление, чтобы оценить качество нашей работы:",
        "faq": (
            f"✦ *ЧАСТО ЗАДАВАЕМЫЕ ВОПРОСЫ*\n"
            f"{H}\n\n"
            f"◈ *Какие услуги вы предоставляете?*\n"
            f"Мы специализируемся на кинематографическом видеопроизводстве и автоматизации бизнеса через AI\\.\n\n"
            f"◈ *Сколько времени занимает проект?*\n"
            f"В зависимости от сложности: Видео \\(3\\-7 дней\\), AI Системы \\(14\\-30 дней\\)\\.\n\n"
            f"◈ *Какие цены?*\n"
            f"Каждый проект рассчитывается индивидуально, так как мы избегаем шаблонных решений\\."
        ),
        "contact": (
            f"✦ *КОНТАКТНЫЙ ЦЕНТР*\n"
            f"{H}\n\n"
            f"Для обсуждения проектов или предложений открыты следующие каналы:"
        ),
        "lang_select": "🌐 *Выберите язык общения:*",
        "ai_intro": (
            f"✦ *ЧАТ С AI СТРАТЕГОМ*\n"
            f"{H}\n\n"
            f"Задавайте свои вопросы\\. Я отвечу вам, основываясь на опыте и видении Абдуллоха\\."
        ),
        "buttons": {
            "about": "💎 Философия",
            "experience": "💼 Экспертиза",
            "skills": "🛠 Технологии",
            "portfolio": "📁 Проекты",
            "contact": "📞 Связь",
            "lang": "🌐 Язык",
            "hire": "🤝 Партнерство",
            "mini_app": "🚀 Web Experience",
            "ai_chat": "🤖 AI Стратег",
            "faq": "❓ Вопросы",
            "back": "⬅️ Назад"
        }
    },
    "en": {
        "start": (
            f"✦ *EXECUTIVE DIGITAL IDENTITY: ABDULLOH*\n"
            f"{H}\n\n"
            f"You are at the intersection of innovation and high visual taste\\. "
            f"I am not just a bot — I am Abdulloh's digital strategist\\.\n\n"
            f"◈ *What value can we offer you?*"
        ),
        "menu": f"✦ *Welcome to the Main Menu*\n{H}\n\nSelect a section to explore:",
        "about": (
            f"✦ *BRAND PHILOSOPHY*\n"
            f"{H}\n\n"
            f"{CV_DATA['philosophy']['en']}\n\n"
            f"◈ *Core Values:* Discipline, Experimental Approach, and Excellence\\.\n"
            f"◈ *Sports:* 'Never Give Up' mentality forged through Taekwondo\\."
        ),
        "portfolio": f"✦ *STRATEGIC PROJECTS*\n{H}\n\nChoose a category to evaluate our work quality:",
        "faq": (
            f"✦ *FREQUENTLY ASKED QUESTIONS*\n"
            f"{H}\n\n"
            f"◈ *What services do you provide?*\n"
            f"We specialize in cinematic video production and business automation through AI\\.\n\n"
            f"◈ *How long does a project take?*\n"
            f"Depending on complexity: Video \\(3\\-7 days\\), AI Systems \\(14\\-30 days\\)\\.\n\n"
            f"◈ *What is the pricing?*\n"
            f"Each project is priced individually, as we avoid cookie\\-cutter solutions\\."
        ),
        "contact": (
            f"✦ *CONTACT CENTER*\n"
            f"{H}\n\n"
            f"The following channels are open for project discussions or inquiries:"
        ),
        "lang_select": "🌐 *Choose your language:*",
        "ai_intro": (
            f"✦ *CHAT WITH AI STRATEGIST*\n"
            f"{H}\n\n"
            f"Send your questions\\. I will answer based on Abdulloh's experience and vision\\."
        ),
        "buttons": {
            "about": "💎 Philosophy",
            "experience": "💼 Expertise",
            "skills": "🛠 Technologies",
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
        "uz": "📸 *VISUAL ARTS & CINEMATOGRAPHY*\n\nMen brendlar uchun shunchaki video emas, balki ularning xarakterini ko'rsatuvchi cinematic asarlar yarataman\\.\n\n◈ *Yo'nalishlar:* High-end Reels, Reklama roliklari, Vizual brending\\.",
        "ru": "📸 *VISUAL ARTS & CINEMATOGRAPHY*\n\nЯ создаю для брендов не просто видео, а кинематографические произведения, раскрывающие их характер\\.\n\n◈ *Направления:* High-end Reels, Рекламные ролики, Визуальный брендинг\\.",
        "en": "📸 *VISUAL ARTS & CINEMATOGRAPHY*\n\nI don't just create videos; I craft cinematic works that reveal the character of a brand\\.\n\n◈ *Specialties:* High-end Reels, Commercials, Visual Branding\\."
    },
    "code": {
        "uz": "💻 *AI ARCHITECTURE & DEVELOPMENT*\n\nMurakkab biznes muammolarini algoritmlar va sun'iy intellekt orqali hal qilaman\\.\n\n◈ *Yechimlar:* Enterprise Bots, AI CRM Systems, Business Automation\\.",
        "ru": "💻 *AI ARCHITECTURE & DEVELOPMENT*\n\nЯ решаю сложные бизнес-задачи с помощью алгоритмов и искусственного интеллекта\\.\n\n◈ *Решения:* Enterprise Bots, AI CRM Systems, Автоматизация бизнеса\\.",
        "en": "💻 *AI ARCHITECTURE & DEVELOPMENT*\n\nI solve complex business problems through algorithms and artificial intelligence\\.\n\n◈ *Solutions:* Enterprise Bots, AI CRM Systems, Business Automation\\."
    }
}

MEDIA = {
    "start": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e",
    "about": "https://images.unsplash.com/photo-1519389950473-47ba0277781c",
    "mobilography": "https://sample-videos.com/video321/mp4/720/big_buck_bunny_720p_1mb.mp4",
}
