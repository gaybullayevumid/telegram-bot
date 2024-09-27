from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

SUPERUSERS = [5323321097, 5323321097]
BLACKLIST = [5363341097, 5363341097]

@dp.message_handler(chat_id=SUPERUSERS, text='secret')
async def id_filter_example(msg: types.Message):
    await msg.answer('Xush kelibsiz, SuperUSER!')