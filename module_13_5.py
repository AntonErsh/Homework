from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb_sex = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button1 = KeyboardButton(text='М')
button2 = KeyboardButton(text='Ж')
kb_sex.row(button1, button2)
kb_sex_remove = ReplyKeyboardRemove()

kb_start = ReplyKeyboardMarkup(resize_keyboard=True)
button_calc = KeyboardButton(text='Рассчитать норму калорий')
button_info = KeyboardButton(text='Информация')
kb_start.row(button_calc, button_info)


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать норму калорий')
async def set_sex(message):
    await message.answer('Укажите ваш пол: М или Ж ', reply_markup=kb_sex)
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой возраст ', reply_markup=kb_sex_remove)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост ')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес ')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    if data['sex'] == 'М':
        male_calories_allowance = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
        await message.answer(f'Ваша норма калорий в сутки: {male_calories_allowance}')
    if data['sex'] == 'Ж':
        female_calories_allowance = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
        await message.answer(f'Ваша норма калорий в сутки: {female_calories_allowance}')
    await state.finish()


@dp.message_handler(commands='start')
async def start_message(message):
    await message.answer('Привет, я бот, помогающий твоему здоровью!', reply_markup=kb_start)


@dp.message_handler(text='Информация')
async def get_info(message):
    await message.answer('Этот раздел пока пуст, бот в разработке')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду "/start", чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
