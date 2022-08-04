from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('/Начать')
b2 = KeyboardButton('/О_боте')
b3 = KeyboardButton('Мужчина 👨')
b4 = KeyboardButton('Женщина 👩')
b5 = KeyboardButton('1️⃣')
b6 = KeyboardButton('2️⃣')
b7 = KeyboardButton('3️⃣')
b8 = KeyboardButton('4️⃣')
b9 = KeyboardButton('5️⃣')
b10 = KeyboardButton('Похудение')
b11 = KeyboardButton('Поддержание формы')
b12 = KeyboardButton('Набор массы')


on_startup_button = InlineKeyboardMarkup(row_width=2).row(
    InlineKeyboardButton(text='О боте', callback_data='info'), InlineKeyboardButton(text='Начать', callback_data='calculate'))
# start = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# start.row(b1, b2)
gender_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
gender_button.row(b3, b4)
activity_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
activity_button.row(b5, b6, b7, b8, b9)
goal_button = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
goal_button.row(b10, b11, b12)


