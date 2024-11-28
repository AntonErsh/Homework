import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from text import *
from keyboards import *
from config import *


logging.basicConfig(level=logging.INFO)

bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start(message):
    await message.answer(start_message, reply_markup=start_kb)


@dp.message_handler(text='О нас')
async def about(message):
    await message.answer(about_text, reply_markup=start_kb)


@dp.message_handler(text='Стоимость')
async def cost(message):
    await message.answer(text='Что Вас интересует? ', reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')
async def buy_medium(call):
    with open('gameM.jpg', 'rb') as img:
        await call.message.answer_photo(img, Mgame, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='large')
async def buy_large(call):
    with open('gameL.jpg', 'rb') as img:
        await call.message.answer_photo(img, Lgame, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='XL')
async def buy_xl(call):
    with open('gameXL.jpeg', 'rb') as img:
        await call.message.answer_photo(img, XLgame, reply_markup=buy_kb)
        await call.answer()


@dp.callback_query_handler(text='other')
async def buy_other(call):
    await call.message.answer(other, reply_markup=buy_kb)
    await call.answer()


@dp.callback_query_handler(text='back')
async def back(call):
    await call.message.answer(start_message, reply_markup=catalog_kb)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
