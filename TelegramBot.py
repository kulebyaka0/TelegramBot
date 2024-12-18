import telebot
from telebot import types
from bs4 import BeautifulSoup
from telebot.util import content_type_media
import requests

def get_horoscope(url, class_name):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    horoscope_elements = soup.find_all("div", class_=class_name)
    return "\n\n".join([element.get_text(strip=True) for element in horoscope_elements])


bot = telebot.TeleBot('8016050795:AAErC2HM9kw-s3Gi1YIuu71Roalcw-SxiyY')

url1 = "https://astrohoro.ru/goroskop/dlya-ovna/"
url2 = "https://astrohoro.ru/goroskop/dlya-teltsa/"
url3 = "https://astrohoro.ru/goroskop/dlya-bliznetsa/"
url4 = "https://astrohoro.ru/goroskop/dlya-raka/"
url5 = "https://astrohoro.ru/goroskop/dlya-lva/"
url6 = "https://astrohoro.ru/goroskop/dlya-devy/"
url7 = "https://astrohoro.ru/goroskop/dlya-vesy/"
url8 = "https://astrohoro.ru/goroskop/dlya-skorpiona/"
url9 = "https://astrohoro.ru/goroskop/dlya-streltsa/"
url10 = "https://astrohoro.ru/goroskop/dlya-kozeroga/"
url11 = "https://astrohoro.ru/goroskop/dlya-vodoleya/"
url12 = "https://astrohoro.ru/goroskop/dlya-ryby/"

@bot.message_handler(commands = ['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Овен')
    btn2 = types.KeyboardButton('Телец')
    btn3 = types.KeyboardButton('Близнецы')
    markup.row(btn1, btn2, btn3)
    btn4 = types.KeyboardButton('Рак')
    btn5 = types.KeyboardButton('Лев')
    btn6 = types.KeyboardButton('Дева')
    markup.row(btn4, btn5, btn6)
    btn7 = types.KeyboardButton('Весы')
    btn8 = types.KeyboardButton('Скорпион')
    btn9 = types.KeyboardButton('Стрелец')
    markup.row(btn7, btn8, btn9)
    btn10 = types.KeyboardButton('Козерог')
    btn11 = types.KeyboardButton('Водолей')
    btn12 = types.KeyboardButton('Рыбы')
    markup.row(btn10, btn11, btn12)
    bot.send_message(message.chat.id, 'Привет! Этот бот создан для предсказывания твоего гороскопа на сегодняшний день. Не терпится узнать, что уготовано судьбой? Тогда вперед! Для начала выберите свой знак зодиака!', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Овен' or message.text == 'овен':
        const = len(message.text) + 15
        horo = get_horoscope(url1, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Телец' or message.text == 'телец':
        const = len(message.text) + 15
        horo = get_horoscope(url2, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Близнецы' or message.text == 'близнецы':
        const = len(message.text) + 15
        horo = get_horoscope(url3, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Рак' or message.text == 'рак':
        const = len(message.text) + 15
        horo = get_horoscope(url4, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Лев' or message.text == 'лев':
        const = len(message.text) + 15
        horo = get_horoscope(url5, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Дева' or message.text == 'дева':
        const = len(message.text) + 15
        horo = get_horoscope(url6, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Весы' or message.text == 'весы':
        const = len(message.text) + 15
        horo = get_horoscope(url7, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Скорпион' or message.text == 'скорпион':
        const = len(message.text) + 15
        horo = get_horoscope(url8, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Стрелец' or message.text == 'стрелец':
        const = len(message.text) + 15
        horo = get_horoscope(url9, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Козерог' or message.text == 'козерог':
        const = len(message.text) + 15
        horo = get_horoscope(url10, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Водолей' or message.text == 'водолей':
        const = len(message.text) + 15
        horo = get_horoscope(url11, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    if message.text == 'Рыбы' or message.text == 'рыбы':
        const = len(message.text) + 15
        horo = get_horoscope(url12, "horo-text")[const:]
        bot.send_message(message.chat.id, horo)
    user(message)
    bot.register_next_step_handler(message, on_click)

@bot.message_handler()
def user(message):
    if (message.text.lower() != '/start' and message.text.lower() != 'овен' and message.text.lower() != 'телец' and message.text.lower() != 'близнецы' and message.text.lower() != 'рак' and message.text.lower() != 'лев' and message.text.lower() != 'дева' and message.text.lower() != 'весы' and message.text.lower() != 'скорпион' and message.text.lower() != 'козерог' and message.text.lower() != 'стрелец' and message.text.lower() != 'водолей' and message.text.lower() != 'рыбы'):
        bot.send_message(message.chat.id,'Звезды с радостью бы с тобой поговорили, но они не умеют :(. Может тебя интересует, что случится завтра?')
    if (message.text.lower() == '/start'):
        bot.send_message(message.chat.id,'Привет! Этот бот создан для предсказывания твоего гороскопа на сегодняшний день. Не терпится узнать, что уготовано судьбой? Тогда вперед! Для начала выберите свой знак зодиака!')


bot.polling(none_stop=True)
