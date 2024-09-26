from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp

dp.message_handler(CommandStart(deep_link='kunuz'))
async def bot_start(message: types.message):
    args = message.get_args()
    text = f"Salom, {message.from_user.full_name}!\n"
    text += f"Sizni {args} tavsiya qildi"
    await message.answer(text)
    

@dp.message_handler(commands='start') # bu ko'rinishda istalgan command uchun yozishimiz mumkin
@dp.message_handler(CommandStart(deep_link='kunuz')) # bu handler aynan kunuzdan kirgan va start bosgan userlarni qabul qilib oladi
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")