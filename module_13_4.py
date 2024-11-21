from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    sex = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Норма калорий')
async def set_sex(message):
    await message.answer('Укажите ваш пол: М или Ж ')
    await UserState.sex.set()


@dp.message_handler(state=UserState.sex)
async def set_age(message, state):
    await state.update_data(sex=message.text)
    await message.answer('Введите свой возраст ')
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
    if data['sex'] == 'М' or 'м':
        male_calories_allowance = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
        await message.answer(f'Ваша норма калорий в сутки: {male_calories_allowance}')
    if data['sex'] == 'Ж' or 'ж':
        female_calories_allowance = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
        await message.answer(f'Ваша норма калорий в сутки: {female_calories_allowance}')
    await state.finish()


@dp.message_handler(commands='start')
async def start_message(message):
    await message.answer('Привет, я бот, помогающий твоему здоровью!')
    await asyncio.sleep(1)
    await message.answer('Напишите "Норма калорий", чтобы узнать свою норму калорий')


@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду "/start", чтобы начать общение')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
