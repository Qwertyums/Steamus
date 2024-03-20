#Небольшая заготовка(бота можно найти по этому тегу: @Stimus_bot)
import asyncio
import logging
from DATA import BOT_TOKEN
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,ReplyKeyboardRemove)


bot_token = BOT_TOKEN
bot = Bot(token=bot_token)
dp = Dispatcher()

button_1 = KeyboardButton(text='Цены')
button_2 = KeyboardButton(text='Портфели')

keyboard = ReplyKeyboardMarkup(keyboard=[[button_1, button_2]])

@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Куда топаем?',
        reply_markup=keyboard
    )

keyboard = ReplyKeyboardMarkup(
    keyboard=[[button_1, button_2]],
    resize_keyboard=True,
    one_time_keyboard=True
)

@dp.message(F.text == 'Цены')
async def process_dog_answer(message: Message):
    await message.answer(
        text='Работаю над реализацией '
    )


@dp.message(F.text == 'Портфели')
async def process_cucumber_answer(message: Message):
    await message.answer(
        text='Работаю над реализацией '
    )


if __name__ == '__main__':
    dp.run_polling(bot)
