from aiogram import Bot, Dispatcher
from aiogram.types import Message, ReplyKeyboardMarkup,KeyboardButton
from aiogram.filters import Command
import requests
from dotenv import load_dotenv
import os
load_dotenv()
bot = Bot(token=os.getenv("API_TOKEN"))
dp = Dispatcher()

@dp.message(Command(commands="start"))
async def start_process(msg: Message):
    quote_btn = KeyboardButton(text="цитата")
    activity_btn = KeyboardButton(text="чем заняться?")
    keyboard = ReplyKeyboardMarkup(keyboard=[[quote_btn,activity_btn]],resize_keyboard=True)
    await msg.reply(text="привет",reply_markup=keyboard)

@dp.message(lambda message: message.text == "цитата")
async def quote_process(msg:Message):
    response = requests.get("https://favqs.com/api/qotd")
    quote_data = response.json()
    quote_text = quote_data['quote']['body']
    quote_author = quote_data['quote']['author']
    await msg.answer(f'Цитата: {quote_text}\nАвтор: {quote_author}')
    
@dp.message(lambda message: message.text == "чем заняться?")
async def bored_process(msg:Message):
    await msg.reply(text="сколько вас человек???")
    @dp.message(lambda message:message.text)
    async def get_user_answer(msg:Message):
        try:
            user_answer = msg.text
            response = requests.get(f"http://www.boredapi.com/api/activity?minparticipants={user_answer}&maxparticipants={user_answer}")
            data = response.json()
            await msg.reply(text=f"хорошо, в таком случае я предлаваю вам вот такое занятие на {user_answer} человек:\n{data['activity']}")
        except KeyError: await msg.reply(text=f"извините, ничего не могу предложить для {user_answer} человек")
        

if __name__ == "__main__":
    dp.run_polling(bot) 