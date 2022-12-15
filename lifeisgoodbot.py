import requests
from aiogram import types, executor, Dispatcher, Bot
from bs4 import BeautifulSoup as BS


bot = Bot('5834430432:AAEvLxRl37jP7k5Xbhaq8ZgiSx1IjjIQdM4')
dp = Dispatcher(bot)

#команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, """ 
Привет друзья! С вами на связи Виталий Пятенко, я ваш друг и знаю новости компании  <b><a href="https://hermes-recovery.info">Гермес</a></b>
    
    """,
    parse_mode="html", disable_web_page_preview=0)

#парсер

@dp.message_handler(content_types=['text'])
async def parser(message: types.message):
    url = 'https://hermes-recovery.info/' + message.text
    request = requests.get(url)
    soup = BeautifulSoup(resp, 'html.parser')

    links = soup.find_all("div")



executor.start_polling(dp)

