from aiogram import types
from aiogram.dispatcher import filters
from loader import dp

@dp.message_handler(content_types='document')
@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(msg: types.Message):
    await msg.answer('Bu nima?')

# @dp.message_handler(content_types='photo')
# async def photo_handler(msg: types.Message):
#     await msg.answer('Nima rasm bu?')

@dp.message_handler(content_types='sticker')
async def emoji_handler(msg: types.Message):
    await msg.answer('😂')


@dp.message_handler(content_types='contact')
async def contact_handler(msg: types.Message):
    await msg.answer('Kim bu odam?')


@dp.message_handler(content_types=types.ContentType.VOICE)
async def audio_handler(msg: types.Message):
    await msg.answer('Yaxshi eshitmadim')