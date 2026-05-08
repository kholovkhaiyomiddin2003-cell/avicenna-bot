import telebot
from telebot import types
import os

# Твой токен
TOKEN = '8711747881:AAG8gtDfsguqxlnl6y9R5A_fWUPY4fR_5o4'

bot = telebot.TeleBot(TOKEN)

# Папка с материалами (создай её)
MATERIALS_DIR = 'materials'
os.makedirs(MATERIALS_DIR, exist_ok=True)

# Главное меню
def main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('1 курс')
    btn2 = types.KeyboardButton('2 курс')
    btn3 = types.KeyboardButton('3 курс')
    btn4 = types.KeyboardButton('4 курс')
    btn5 = types.KeyboardButton('5 курс')
    btn6 = types.KeyboardButton('6 курс')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    welcome_text = """Добро пожаловать в **Avicenna AI Bot**! 

Я помогу студентам-медикам Донишгоҳи Миллӣ с материалами.

Выбери свой курс:"""
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(), parse_mode='Markdown')

# Обработчики курсов
@bot.message_handler(func=lambda message: message.text in ['1 курс', '2 курс', '3 курс', '4 курс', '5 курс', '6 курс'])
def course_handler(message):
    course = message.text
    markup = types.InlineKeyboardMarkup(row_width=2)
    
    # Пример материалов — замени на реальные файлы
    pdf_btn = types.InlineKeyboardButton("📕 Анатомия (PDF)", callback_data=f"{course}_anatomy")
    notes_btn = types.InlineKeyboardButton("📝 Конспекты", callback_data=f"{course}_notes")
    books_btn = types.InlineKeyboardButton("📚 Учебники", callback_data=f"{course}_books")
    
    markup.add(pdf_btn, notes_btn, books_btn)
    
    bot.send_message(message.chat.id, f"Материалы для **{course}**:", reply_markup=markup, parse_mode='Markdown')

# Callback для inline-кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    data = call.data
    chat_id = call.message.chat.id
    
    if '_anatomy' in data:
        # Отправка PDF (положи файл в materials/anatomy.pdf)
        try:
            with open(f'{MATERIALS_DIR}/anatomy.pdf', 'rb') as f:
                bot.send_document(chat_id, f, caption="Анатомия - PDF")
        except FileNotFoundError:
            bot.send_message(chat_id, "Файл пока не загружен. Добавь anatomy.pdf в папку materials/")
    
    elif '_notes' in data:
        bot.send_message(chat_id, "Конспекты будут здесь (добавь текст или файлы)")
    
    elif '_books' in data:
        bot.send_message(chat_id, "Список учебников:\n1. ...")

# Запуск бота
if __name__ == '__main__':
    print("Avicenna AI Bot запущен...")
    bot.infinity_polling()
