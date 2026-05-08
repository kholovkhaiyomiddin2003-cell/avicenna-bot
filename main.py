# ==============================================
#   AVICENNA AI BOT — Telegram бот для ТНУ
#   Версия 2.0 — Двуязычная / Дузабона
# ==============================================

import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8711747881:AAG8gtDfsguqxlnl6y9R5A_fWUPY4fR_5o4")
bot = telebot.TeleBot(BOT_TOKEN)

user_lang = {}

def get_lang(user_id):
    return user_lang.get(user_id, "ru")

LANG = {
    "ru": {
        "welcome": (
            "Ассалому алейкум, *{name}*! 👋\n\n"
            "*Avicenna AI Bot* — твой помощник\n"
            "на медицинском факультете ТНУ 🏛️\n\n"
            "📚 Здесь ты найдёшь:\n"
            "• Учебники и PDF по всем предметам\n"
            "• Конспекты и схемы\n"
            "• Тесты и клинические задачи\n"
            "• Материалы для DHA / ГЭК\n\n"
            "👇 Выбери свой курс:"
        ),
        "choose_course":   "🏛️ *Avicenna AI Bot*\n\nВыбери свой курс 👇",
        "choose_subject":  "Выбери предмет 👇",
        "materials_title": "📂 Доступные материалы:\n_(нажми для перехода)_",
        "back_courses":    "⬅️ Назад к курсам",
        "back_subjects":   "⬅️ Назад к предметам",
        "back_main":       "⬅️ Главное меню",
        "about_btn":       "ℹ️ О боте",
        "change_lang":     "🌐 Сменить язык",
        "about_text": (
            "🌿 *Avicenna AI Bot*\n\n"
            "Создан для студентов медицинского факультета\n"
            "*Таджикского национального университета*\n\n"
            "📍 Душанбе, Таджикистан\n\n"
            "Назван в честь великого учёного\n"
            "*Абу Али ибн Сины (Авиценны)* —\n"
            "отца медицины 🌙"
        ),
        "unknown": "👇 Используй меню для навигации:",
        "course_names": {
            "1": "🔬 1 курс", "2": "🫀 2 курс", "3": "💊 3 курс",
            "4": "🏥 4 курс", "5": "🩻 5 курс", "6": "👨‍⚕️ 6 курс",
        },
    },
    "tj": {
        "welcome": (
            "Ассалому алайкум, *{name}*! 👋\n\n"
            "*Avicenna AI Bot* — ёрдамчии ту\n"
            "дар факултети тиббии ДМТ 🏛️\n\n"
            "📚 Дар ин ҷо ту меёбӣ:\n"
            "• Китобҳо ва PDF аз ҳама фанҳо\n"
            "• Конспектҳо ва схемаҳо\n"
            "• Тестҳо ва масъалаҳои клиникӣ\n"
            "• Маводҳо барои DHA / ГЭК\n\n"
            "👇 Курси худро интихоб кун:"
        ),
        "choose_course":   "🏛️ *Avicenna AI Bot*\n\nКурси худро интихоб кунед 👇",
        "choose_subject":  "Фанро интихоб кунед 👇",
        "materials_title": "📂 Маводҳои дастрас:\n_(барои дастрасӣ пахш кунед)_",
        "back_courses":    "⬅️ Бозгашт ба курсҳо",
        "back_subjects":   "⬅️ Бозгашт ба фанҳо",
        "back_main":       "⬅️ Менюи асосӣ",
        "about_btn":       "ℹ️ Дар бораи бот",
        "change_lang":     "🌐 Забонро иваз кунед",
        "about_text": (
            "🌿 *Avicenna AI Bot*\n\n"
            "Барои донишҷӯёни факултети тиббии\n"
            "*Донишгоҳи Миллии Тоҷикистон* сохта шудааст\n\n"
            "📍 Душанбе, Тоҷикистон\n\n"
            "Ба шарофати олими бузург\n"
            "*Абӯалӣ ибни Сино* —\n"
            "падари тибб номгузорӣ шудааст 🌙"
        ),
        "unknown": "👇 Барои навигатсия меню истифода кунед:",
        "course_names": {
            "1": "🔬 Курси 1", "2": "🫀 Курси 2", "3": "💊 Курси 3",
            "4": "🏥 Курси 4", "5": "🩻 Курси 5", "6": "👨‍⚕️ Курси 6",
        },
    },
}

SUBJECTS_RU = {
    "1": [
        {"name": "Анатомия человека",         "icon": "🦴"},
        {"name": "Гистология",                "icon": "🔭"},
        {"name": "Биология",                  "icon": "🧬"},
        {"name": "Химия",                     "icon": "⚗️"},
        {"name": "Латинский язык",            "icon": "📜"},
    ],
    "2": [
        {"name": "Нормальная физиология",     "icon": "💓"},
        {"name": "Биохимия",                  "icon": "🧪"},
        {"name": "Патологическая анатомия",   "icon": "🔬"},
        {"name": "Микробиология",             "icon": "🦠"},
    ],
    "3": [
        {"name": "Патологическая физиология", "icon": "⚡"},
        {"name": "Фармакология",              "icon": "💉"},
        {"name": "Пропедевтика вн. болезней", "icon": "🩺"},
        {"name": "Общая хирургия",            "icon": "🔪"},
    ],
    "4": [
        {"name": "Внутренние болезни",        "icon": "🫁"},
        {"name": "Хирургические болезни",     "icon": "⚕️"},
        {"name": "Акушерство и гинекология",  "icon": "👶"},
        {"name": "Неврология",               "icon": "🧠"},
    ],
    "5": [
        {"name": "Педиатрия",                 "icon": "👦"},
        {"name": "Онкология",                 "icon": "🎗️"},
        {"name": "Инфекционные болезни",      "icon": "🦠"},
        {"name": "Психиатрия",               "icon": "🧩"},
    ],
    "6": [
        {"name": "Субординатура / Интернатура","icon": "🎓"},
        {"name": "Подготовка к ГЭК",         "icon": "📚"},
        {"name": "DHA / USMLE подготовка",    "icon": "🌍"},
    ],
}

SUBJECTS_TJ = {
    "1": [
        {"name": "Анатомияи инсон",                "icon": "🦴"},
        {"name": "Гистология",                     "icon": "🔭"},
        {"name": "Биология",                       "icon": "🧬"},
        {"name": "Химия",                          "icon": "⚗️"},
        {"name": "Забони лотинӣ",                  "icon": "📜"},
    ],
    "2": [
        {"name": "Физиологияи меъёрӣ",             "icon": "💓"},
        {"name": "Биохимия",                       "icon": "🧪"},
        {"name": "Анатомияи патологӣ",             "icon": "🔬"},
        {"name": "Микробиология",                  "icon": "🦠"},
    ],
    "3": [
        {"name": "Физиологияи патологӣ",           "icon": "⚡"},
        {"name": "Фармакология",                   "icon": "💉"},
        {"name": "Пропедевтикаи бемориҳои дохилӣ", "icon": "🩺"},
        {"name": "Ҷарроҳии умумӣ",                "icon": "🔪"},
    ],
    "4": [
        {"name": "Бемориҳои дохилӣ",               "icon": "🫁"},
        {"name": "Бемориҳои ҷарроҳӣ",             "icon": "⚕️"},
        {"name": "Акушерӣ ва гинекология",         "icon": "👶"},
        {"name": "Неврология",                    "icon": "🧠"},
    ],
    "5": [
        {"name": "Педиатрия",                      "icon": "👦"},
        {"name": "Онкология",                      "icon": "🎗️"},
        {"name": "Бемориҳои сироятӣ",              "icon": "🦠"},
        {"name": "Психиатрия",                    "icon": "🧩"},
    ],
    "6": [
        {"name": "Субординатура / Интернатура",    "icon": "🎓"},
        {"name": "Тайёрӣ ба ГЭК",                 "icon": "📚"},
        {"name": "DHA / USMLE тайёрӣ",            "icon": "🌍"},
    ],
}

LINKS = {
    "1": [
        [
            ("📖 Сапин — Анатомия (PDF)",      "https://t.me/avicenna_files"),
            ("📝 Конспекты по анатомии",        "https://t.me/avicenna_files"),
            ("🎥 Видеолекции анатомия",         "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Афанасьев — Гистология (PDF)", "https://t.me/avicenna_files"),
            ("📝 Конспекты по гистологии",      "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Билич — Биология (PDF)",       "https://t.me/avicenna_files"),
            ("📋 Тесты по биологии",            "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Органическая химия (PDF)",     "https://t.me/avicenna_files"),
            ("📖 Неорганическая химия (PDF)",   "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Учебник латыни для медиков",   "https://t.me/avicenna_files"),
            ("📋 Термины и рецептура",          "https://t.me/avicenna_files"),
        ],
    ],
    "2": [
        [
            ("📖 Судаков — Физиология (PDF)",   "https://t.me/avicenna_files"),
            ("📝 Конспекты физиология",         "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Березов — Биохимия (PDF)",     "https://t.me/avicenna_files"),
            ("📋 Задачи по биохимии",           "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Струков — Патанатомия (PDF)",  "https://t.me/avicenna_files"),
            ("📝 Конспекты патанатомия",        "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Воробьёв — Микробиология (PDF)","https://t.me/avicenna_files"),
            ("📋 Тесты микробиология",          "https://t.me/avicenna_files"),
        ],
    ],
    "3": [
        [
            ("📖 Литвицкий — Патфизиология (PDF)","https://t.me/avicenna_files"),
            ("📝 Конспекты патфизиология",       "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Харкевич — Фармакология (PDF)", "https://t.me/avicenna_files"),
            ("📋 Тесты по фармакологии",         "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Мухин — Пропедевтика (PDF)",    "https://t.me/avicenna_files"),
            ("📝 Схема истории болезни",         "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Петров — Общая хирургия (PDF)", "https://t.me/avicenna_files"),
            ("📝 Конспекты хирургия",            "https://t.me/avicenna_files"),
        ],
    ],
    "4": [
        [
            ("📖 Мартынов — Внутренние болезни (PDF)","https://t.me/avicenna_files"),
            ("📋 Клинические задачи",            "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Кузин — Хирургические болезни (PDF)","https://t.me/avicenna_files"),
            ("📝 Конспекты хирургия",            "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Савельева — Акушерство (PDF)",  "https://t.me/avicenna_files"),
            ("📋 Протоколы акушерство",          "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Гусев — Неврология (PDF)",      "https://t.me/avicenna_files"),
            ("📝 Конспекты неврология",          "https://t.me/avicenna_files"),
        ],
    ],
    "5": [
        [
            ("📖 Баранов — Педиатрия (PDF)",     "https://t.me/avicenna_files"),
            ("📋 Дозировки в педиатрии",         "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Ганцев — Онкология (PDF)",      "https://t.me/avicenna_files"),
            ("📝 Конспекты онкология",           "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Ющук — Инфекционные болезни (PDF)","https://t.me/avicenna_files"),
            ("📋 Карантинные инфекции",          "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Тиганов — Психиатрия (PDF)",    "https://t.me/avicenna_files"),
            ("📝 МКБ-10 критерии",              "https://t.me/avicenna_files"),
        ],
    ],
    "6": [
        [
            ("📖 Клинические протоколы МЗ РТ",  "https://t.me/avicenna_files"),
            ("📋 Стандарты лечения",            "https://t.me/avicenna_files"),
        ],
        [
            ("📖 Билеты ГЭК по терапии",        "https://t.me/avicenna_files"),
            ("📖 Билеты ГЭК по хирургии",       "https://t.me/avicenna_files"),
            ("📖 Билеты ГЭК по акушерству",     "https://t.me/avicenna_files"),
        ],
        [
            ("📖 First Aid USMLE Step 1",        "https://t.me/avicenna_files"),
            ("📋 DHA экзамен — вопросы",        "https://t.me/avicenna_files"),
            ("🌐 DHA официальный сайт",         "https://www.dha.gov.ae"),
        ],
    ],
}

# ==============================================
#   КЛАВИАТУРЫ
# ==============================================

def lang_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(
        InlineKeyboardButton("🇷🇺 Русский",  callback_data="lang_ru"),
        InlineKeyboardButton("🇹🇯 Тоҷикӣ", callback_data="lang_tj"),
    )
    return markup

def main_menu_keyboard(lang):
    L = LANG[lang]
    markup = InlineKeyboardMarkup(row_width=2)
    buttons = [
        InlineKeyboardButton(L["course_names"][cid], callback_data=f"course_{cid}")
        for cid in ["1","2","3","4","5","6"]
    ]
    markup.add(*buttons)
    markup.add(
        InlineKeyboardButton(L["about_btn"],   callback_data="about"),
        InlineKeyboardButton(L["change_lang"], callback_data="change_lang"),
    )
    return markup

def subjects_keyboard(lang, course_id):
    L = LANG[lang]
    subjects = SUBJECTS_TJ[course_id] if lang == "tj" else SUBJECTS_RU[course_id]
    markup = InlineKeyboardMarkup(row_width=1)
    for i, subj in enumerate(subjects):
        markup.add(InlineKeyboardButton(
            f"{subj['icon']} {subj['name']}",
            callback_data=f"subj_{course_id}_{i}"
        ))
    markup.add(InlineKeyboardButton(L["back_courses"], callback_data="back_main"))
    return markup

def materials_keyboard(lang, course_id, subj_idx):
    L = LANG[lang]
    links = LINKS[course_id][subj_idx]
    markup = InlineKeyboardMarkup(row_width=1)
    for name, url in links:
        markup.add(InlineKeyboardButton(name, url=url))
    markup.add(InlineKeyboardButton(
        L["back_subjects"], callback_data=f"course_{course_id}"
    ))
    return markup

# ==============================================
#   КОМАНДЫ
# ==============================================

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "🌐 Выбери язык / Забонро интихоб кунед:",
        reply_markup=lang_keyboard()
    )

@bot.message_handler(commands=["help"])
def help_cmd(message):
    lang = get_lang(message.from_user.id)
    if lang == "tj":
        text = "🆘 *Ёрдам*\n\n/start — менюи асосӣ\n/help — ин ёрдам"
    else:
        text = "🆘 *Помощь*\n\n/start — главное меню\n/help — эта справка"
    bot.send_message(message.chat.id, text, parse_mode="Markdown")

# ==============================================
#   CALLBACK
# ==============================================

@bot.callback_query_handler(func=lambda c: c.data.startswith("lang_"))
def set_lang(call):
    lang = call.data.split("_")[1]
    user_lang[call.from_user.id] = lang
    L = LANG[lang]
    name = call.from_user.first_name or ("Донишҷӯ" if lang == "tj" else "Студент")
    bot.edit_message_text(
        L["welcome"].format(name=name),
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(lang)
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data == "change_lang")
def change_lang(call):
    bot.edit_message_text(
        "🌐 Выбери язык / Забонро интихоб кунед:",
        call.message.chat.id,
        call.message.message_id,
        reply_markup=lang_keyboard()
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data == "back_main")
def back_main(call):
    lang = get_lang(call.from_user.id)
    L = LANG[lang]
    bot.edit_message_text(
        L["choose_course"],
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=main_menu_keyboard(lang)
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data.startswith("course_"))
def show_course(call):
    course_id = call.data.split("_")[1]
    lang = get_lang(call.from_user.id)
    L = LANG[lang]
    bot.edit_message_text(
        f"{L['course_names'][course_id]}\n\n{L['choose_subject']}",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=subjects_keyboard(lang, course_id)
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data.startswith("subj_"))
def show_subject(call):
    parts     = call.data.split("_")
    course_id = parts[1]
    subj_idx  = int(parts[2])
    lang      = get_lang(call.from_user.id)
    L         = LANG[lang]
    subjects  = SUBJECTS_TJ[course_id] if lang == "tj" else SUBJECTS_RU[course_id]
    subj      = subjects[subj_idx]
    bot.edit_message_text(
        f"{subj['icon']} *{subj['name']}*\n\n{L['materials_title']}",
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=materials_keyboard(lang, course_id, subj_idx)
    )
    bot.answer_callback_query(call.id)

@bot.callback_query_handler(func=lambda c: c.data == "about")
def show_about(call):
    lang   = get_lang(call.from_user.id)
    L      = LANG[lang]
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(L["back_main"], callback_data="back_main"))
    bot.edit_message_text(
        L["about_text"],
        call.message.chat.id,
        call.message.message_id,
        parse_mode="Markdown",
        reply_markup=markup
    )
    bot.answer_callback_query(call.id)

@bot.message_handler(func=lambda m: True)
def echo(message):
    lang = get_lang(message.from_user.id)
    bot.send_message(
        message.chat.id,
        LANG[lang]["unknown"],
        reply_markup=main_menu_keyboard(lang)
    )

# ==============================================
#   ЗАПУСК
# ==============================================

print("✅ Avicenna AI Bot v2.0 запущен...")
print("🇷🇺 Русский + 🇹🇯 Тоҷикӣ")
print("🛑 Ctrl+C для остановки")

bot.infinity_polling(timeout=30, long_polling_timeout=30)
