from bs4 import BeautifulSoup as BS
import requests
from aiogram import types, executor, Dispatcher, Bot

base_url = 'https://hermes-recovery.info/'
HEADERS = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
              'Chrome/107.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'



}

def parser(url):
    session = requests.Session()
    response = session.get(url, headers=HEADERS)
    soup = BS(response.content, 'html.parser')





parser(url=base_url)

bot = Bot('5834430432:AAEvLxRl37jP7k5Xbhaq8ZgiSx1IjjIQdM4')
dp = Dispatcher(bot)


# команда /start
@dp.message_handler(commands=['start'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, """ 
Привет друзья! С вами на связи Виталий Пятенко, я ваш друг и знаю новости компании  <b><a href="https://hermes-recovery.info">Гермес</a></b>

    """,
                           parse_mode="html", disable_web_page_preview=0)


# парсер

@dp.message_handler(commands=['новости'])
async def start(message: types.message):
    await bot.send_message(message.chat.id, print(soup.get_text),
    parse_mode = "html", disable_web_page_preview = 0)

executor.start_polling(dp)