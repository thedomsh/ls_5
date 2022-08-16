from telebot import TeleBot
from telebot.types import Message
from config import *
import requests

bot = TeleBot(TOKEN)
currency = requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').json()
USD = currency['CcyNm_EN']['US Dollar']['Rate']
EURO = currency['CcyNm_EN']['Euro']['Rate']


@bot.message_handler(commands=['start', 'help', 'about_dev', 'get_usd', 'get_euro'])
def start(message: Message):
    full_name = message.from_user.full_name
    chat_id = message.chat.id
    if message.text == '/start':
        bot.send_message(chat_id, f'''Hi, {full_name}!
I am a currency-bot, can show you exchange rates today''')
    elif message.text == '/help':
        bot.send_message(chat_id, f'''Dear {full_name},
this Bot was developed in PROWEB Educational Center🙌''')
    elif message.text == '/about_dev':
        bot.send_message(chat_id, f'''Hi, {full_name}!
this Bot was developed by t.me/thedomsh himself''')
    elif message.text == '/get_usd':
        bot.send_message(chat_id, f'1 USD = {USD} UZS')
    elif message.text == '/get_euro':
        bot.send_message(chat_id, f'1 EURO = {EURO} UZS')
        pass


bot.polling(none_stop=True)
