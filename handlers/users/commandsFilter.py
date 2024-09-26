from aiogram import types
from aiogram.dispatcher.filters.builtin import Command
from loader import dp


@dp.message_handler(Command('til'))
async def changeLanguage(message: types.Message):
    await message.answer("Til o'zgardi")