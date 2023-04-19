import logging
import random
from os import getenv, system
from datetime import datetime

# Downloaded libraries - Скаченные библиотеки
from aiogram import Bot
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import *

# Created module - Созданный модуль
from core.weather import WeatherService

TOKEN = getenv('TOKEN')
ADMIN = getenv('ADMIN') 

system("clear")
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

Menu = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Казахстан"),
    KeyboardButton("Кыргызстан"),

)
city_KZ = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("Алматы"),
        KeyboardButton("Астана"),
        KeyboardButton("Атырау"),
        KeyboardButton("Актау"),
        KeyboardButton("Орал"),
        KeyboardButton("Усь-Каменагорск"),
        KeyboardButton("Павлодар"),
        KeyboardButton("Сарыагаш"),
        KeyboardButton("Талдыкорган"),
        KeyboardButton("Жетысай"),
        KeyboardButton("Шымкент"),
        KeyboardButton("Кокшетау"),
        KeyboardButton("Жезказган"),
        KeyboardButton("Караганда"),
        KeyboardButton("Семей"),
        KeyboardButton("Menu"),
    )

city_KG = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Бишкек"),
    KeyboardButton("Ош"),
    KeyboardButton("Ыссык-куль"),
    KeyboardButton("Нарын"),
    KeyboardButton("Талас"),
    KeyboardButton("Джал-Абад"),
    KeyboardButton("Баткен"),
    KeyboardButton("Menu"),
)

@dp.message_handler(commands=['start'])
async def start(message: Message):
    photo = open("core/image2.jpg", 'rb')
    text = """Ваш бот-метеоролог мгновенно показывает погоду в любом городе, предоставляя актуальную информацию о температуре воздуха, влажности и вероятности дождя. 
Это помогает планировать дела эффективнее и быть в курсе погодных событий в режиме реального времени."""
    await message.answer_photo(photo, text, reply_markup=Menu)


@dp.message_handler(content_types=ContentType.TEXT)
async def usersanswer(message: Message):
    if message.text.lower() == "menu":
        await message.answer("Вы в меню", reply_markup=Menu)

    elif message.text.lower() == "казахстан":
        await message.answer("Все города Казахстана", reply_markup=city_KZ)

    elif message.text.lower() == "кыргызстан":
        await message.reply("Все города Кыргызстана", reply_markup=city_KG)

    else:
        photo = open("core/image.png", "rb")
        text = WeatherService(message.text)
        await message.reply_photo(photo, text)


if __name__ == '__main__':
    try:
        executor.start_polling(dp)
    except (KeyboardInterrupt, SystemExit):
        pass