from telebot.types import ReplyKeyboardMarkup,KeyboardButton

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
buttons= [
    KeyboardButton(text='О враче'),
    KeyboardButton(text='Оплата'),
    KeyboardButton(text='Прочее'),
    KeyboardButton(text='Услуги'),
    KeyboardButton(text='Отзывы'),
    KeyboardButton(text='Контакты'),
]
keyboard.add(*buttons)