from telebot import TeleBot
from telebot.types import Message,CallbackQuery,ReplyKeyboardMarkup,KeyboardButton
from decouple import config
import json

from kb import keyboard


token = config('TOKEN')

bot = TeleBot(token)


@bot.message_handler(['start'])
def start_message(message: Message):
    with open('greeting.html','r') as file:
        bot.send_message(message.chat.id, file.read(),reply_markup=keyboard ,parse_mode='HTML')


@bot.message_handler(func=lambda message:message.text=='О враче')
def about_me(message:Message):
    with open('about_me.html','rb') as file:
        bot.send_message(message.chat.id,file.read(), parse_mode='HTML')



@bot.message_handler(func=lambda message:message.text=='Оплата')
def payment(message:Message):
    with open('payment.html','r') as file:
        bot.send_message(message.chat.id,file.read(),parse_mode='HTML')


@bot.message_handler(func=lambda message:message.text=='Прочее')
def additional(message:Message):
    with open('additional.html','r') as file:
        bot.send_message(message.chat.id,file.read(),parse_mode='HTML')




@bot.message_handler(func=lambda message:message.text=='Услуги')
def services (message:Message):
    with open('services.html','r') as file:
        bot.send_message(message.chat.id,file.read(),parse_mode='HTML')


@bot.message_handler(func=lambda message:message.text=='Отзывы')
def reviews(message:Message):
    reviews = "http://doctor.shin.tilda.ws/#reviews"
    bot.send_message(message.chat.id,reviews)



@bot.message_handler(func=lambda message:message.text=='Контакты')
def contacts (message:Message):
    with open('contacts.html','rb') as file:
        bot.send_message(message.chat.id,file.read(),parse_mode='HTML')


bot.polling()
