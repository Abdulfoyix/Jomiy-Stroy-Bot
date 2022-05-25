"""
 2This is a echo bot.
 3It echoes any incoming text messages.
 4"""

import logging
from aiogram.types import \
    InlineKeyboardMarkup, \
    InlineKeyboardButton, \
    CallbackQuery, \
    InputFile, ReplyKeyboardMarkup, KeyboardButton

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '5362182250:AAHhw8o783gHYgvyYNgwLSgESAY68ib6h6g'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(mess:types.Message):
    await mess.answer("Bosh menu",reply_markup=Inline_keyboard)




Inline_keyboard=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🏠Xo'jalik Mollari",callback_data="gips"),
            InlineKeyboardButton(text="Kraskalar Bo'limi",callback_data="Kraska"),
            InlineKeyboardButton(text="⚒Qurilish Mollari",callback_data="Qurilish")
        ],
        [
            InlineKeyboardButton(text="📍Lokatsiya",callback_data="Manzil"),
            InlineKeyboardButton(text="🚗Dostafka",callback_data="dostafka")
        ],
    ]
)


@dp.callback_query_handler(text="Manzil")
async def Lokatsiya(call:CallbackQuery):
    # await call.message.delete_reply_markup()
    await call.message.answer_location(latitude=41.35543973944746,longitude=69.24234055316249)



@dp.message_handler(text="Orqaga")
async def back(message: types.Message):
    await message.answer("Bosh menu", reply_markup=Inline_keyboard)


















@dp.message_handler()
async def echo(message: types.Message):
    # old style:
   # await bot.send_message(message.chat.id, message.text)

   await message.answer("Bu buyruq hozircha mavjud emas!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)