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

API_TOKEN = '5373327609:AAH-Ak7tDjwaUabAguKhuRRBMDUbtmT4DyA'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


stroy_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gips", callback_data="gips"),
            InlineKeyboardButton(text="Sement", callback_data="sement")
        ],
        [
            InlineKeyboardButton(text="Kraska", callback_data="kraska"),
            InlineKeyboardButton(text="Truba", callback_data="truba"),
            InlineKeyboardButton(text="Mix", callback_data='mix')
        ],
        [
            InlineKeyboardButton(text="Armatura", callback_data="armatura")
        ]
    ]
)

kontent_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Foto"),
            KeyboardButton(text="Video"),
            KeyboardButton(text="Gif")
        ],
        [
            KeyboardButton(text="Audio"),
            KeyboardButton(text="Ovoz")
        ],
        [
            KeyboardButton(text="Lokatsiya"),
            KeyboardButton(text="Kontakt")
        ]

    ],

    resize_keyboard=True
)
@dp.message_handler(commands=['start'])
async def start(mess:types.Message):
    await mess.answer("Bosh menu",reply_markup=kontent_keyboard)

fotolar=ReplyKeyboardMarkup(
    keyboard=[

    [
        KeyboardButton(text="1-rasm"),
        KeyboardButton(text="2-rasm"),
        KeyboardButton(text="3-rasm")
        ],
        [
            KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True

)

#fayllar fotolar
@dp.message_handler(text="1-rasm")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19368"
    await mess.answer_photo(url,caption="Yulduz")

@dp.message_handler(text="2-rasm")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19366"
    await mess.answer_photo(url,caption="Yulduz")

@dp.message_handler(text="3-rasm")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19365"
    await mess.answer_photo(url,caption="Yulduz")














#videolar toplami
videolar=ReplyKeyboardMarkup(
    keyboard=[

    [    KeyboardButton("1-video"),
        KeyboardButton("2-video"),
        KeyboardButton("3-video")
        ],
        [
            KeyboardButton("4-video"),
            KeyboardButton("5-video"),
        ],
        [
            KeyboardButton("Orqaga")
        ]
    ],
    resize_keyboard=True
)


#Bu videolar
@dp.message_handler(text="1-video")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19367"
    await mess.answer_video(url,caption="Yulduz")

@dp.message_handler(text="2-video")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19363"
    await mess.answer_video(url,caption="Yulduz")

@dp.message_handler(text="3-video")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19361"
    await mess.answer_video(url,caption="Yulduz")

@dp.message_handler(text="4-video")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19360"
    await mess.answer_video(url,caption="Yulduz")


@dp.message_handler(text="5-video")
async def rasm(mess:types.Message):
    url="https://t.me/ky24uz/19358"
    await mess.answer_video(url,caption="Yulduz")






#Giflar toplami
giflar=ReplyKeyboardMarkup(
    keyboard=[

    [    KeyboardButton("1-gif"),
        KeyboardButton("2-gif"),
        KeyboardButton("3-gif")
        ],
        [
            KeyboardButton("4-gif"),
            KeyboardButton("Orqaga"),
            KeyboardButton("5-gif")
        ]
    ],
    resize_keyboard=True
)


#Gif fayllar

@dp.message_handler(text="1-gif")
async def gif(mess:types.Message):
    id="CgACAgQAAxkBAAEP0RNigpjexqrTZGuwJediSJjwoolk4AAC3wIAAt8WDFPgUsDtcJlBOiQE"

    await mess.answer_animation(id,caption="Happy")

@dp.message_handler(text="2-gif")
async def gif(mess:types.Message):
    id="CgACAgQAAxkBAAEP0Rtigpo_RKNNM85aKwVveS64SSi_tAACSgMAAr-5JFOb_9ukNMA9MyQE"

    await mess.answer_animation(id,caption="Sased")

@dp.message_handler(text="3-gif")
async def gif(mess:types.Message):
    id="CgACAgQAAxkBAAEP0SFigprcK7lqh9ofxN5FpYFhmxdxQQACFgMAAp5KBFMCZPAiR4SdsSQE"

    await mess.answer_animation(id,caption="Spanjbob")


@dp.message_handler(text="4-gif")
async def gif(mess: types.Message):
    id = "CgACAgQAAxkBAAEP0SNigpsxKTRzJuYi9UPPuzs8cwn0dgAC0AIAAtacDVMw4LV2eHv86iQE"

    await mess.answer_animation(id, caption="Tanks")


@dp.message_handler(text="5-gif")
async def gif(mess: types.Message):
    id = "CgACAgQAAxkBAAEP0SdigpteLH_jLM80ZEhVPK736E-S_AACEwMAAgqtDFM9bhEwsT3mUCQE"

    await mess.answer_animation(id, caption="Hello")


#Audio toplami
Audio=ReplyKeyboardMarkup(
    keyboard=[

    [    KeyboardButton("1-Audio"),
        KeyboardButton("2-Audio"),
        KeyboardButton("3-Audio")
        ],
        [
            KeyboardButton("4-Audio"),
            KeyboardButton("Orqaga"),
            KeyboardButton("5-Audio")
        ]
    ],
    resize_keyboard=True
)

#Audio fayllar toplami
@dp.message_handler(text="1-Audio")
async def audio1(mes: types.Message):
    id1="CQACAgIAAxkBAAEP1eJihH8y6y8Z4iwj_mWMUeDunPgcpQACEBoAAhPyIEinikmdqq2T7CQE"
    await mes.answer_audio(id1, caption="1-audio")




#Ovoz toplami
Ovoz=ReplyKeyboardMarkup(
    keyboard=[

    [    KeyboardButton("1-ovoz"),
        KeyboardButton("2-ovoz"),
        KeyboardButton("3-ovoz")
        ],
        [
            KeyboardButton("4-ovoz"),
            KeyboardButton("Orqaga"),
            KeyboardButton("5-ovoz")
        ]
    ],
    resize_keyboard=True
)


#Ovoz fayllar toplami!!!

@dp.message_handler(text="1-ovoz")
async def gif(mess: types.Message):
    id = "AwACAgIAAxkBAAEP0VdigqRaU7RUSFhBgV0UO44HYU2qKQACURoAAnwBGUhM1H8WpM8zhyQE"

    await mess.answer_voice(id, caption="Hello")

@dp.message_handler(text="2-ovoz")
async def gif(mess: types.Message):
    id = "AwACAgIAAxkBAAEP0V1igqT9eachvV33oV9o2ll6fvp1wwACWRoAAnwBGUio977ABWrNeiQE"

    await mess.answer_voice(id, caption="my")


@dp.message_handler(text="3-ovoz")
async def gif(mess: types.Message):
    id = "AwACAgIAAxkBAAEP0WNigqVDNR0htlcV63QYP_1zSfLhvQACXBoAAnwBGUivV4X_HFmtHiQE"

    await mess.answer_voice(id, caption="your")

@dp.message_handler(text="4-ovoz")
async def gif(mess: types.Message):
    id = "AwACAgIAAxkBAAEP0WtigqV-a9y_E-o14UaQfUZ25Z0uIwACXxoAAnwBGUjwH3mJRMUD3yQE"

    await mess.answer_voice(id, caption="one")

@dp.message_handler(text="5-ovoz")
async def gif(mess: types.Message):
    id = "AwACAgIAAxkBAAEP0XFigqX6YSSCjgzXy43SVVLYatSBcgACZRoAAnwBGUgmnZBl18nWviQE"

    await mess.answer_voice(id, caption="two")






#Lokatsiya toplami
Lokatsiya=ReplyKeyboardMarkup(
    keyboard=[

    [    KeyboardButton("1-Lokatsiya"),
        KeyboardButton("2-Lokatsiya"),
        KeyboardButton("3-Lokatsiya")
        ],
        [
            KeyboardButton("4-Lokatsiya"),
            KeyboardButton("Orqaga"),
            KeyboardButton("5-Lokatsiya")
        ]
    ],
    resize_keyboard=True
)

#Lokatsiya fayllar toplami

@dp.message_handler(text="1-Lokatsiya")
async def Location(mess:types.Message):

    await mess.answer_location(longitude=41.40180400452301,latitude=69.28791809999726)#41.40180400452301, 69.28791809999726

@dp.message_handler(text="2-Lokatsiya")
async def Location(mess:types.Message):

    await mess.answer_location(longitude=41.23101112975504,latitude=69.07462309557633)#41.23101112975504, 69.07462309557633

@dp.message_handler(text="3-Lokatsiya")
async def Location(mess:types.Message):

    await mess.answer_location(longitude=41.24513691609403,latitude=70.43557671794379)#

@dp.message_handler(text="4-Lokatsiya")
async def Location(mess:types.Message):

    await mess.answer_location(longitude=40.733838327418994,latitude=69.55631018632182)#

@dp.message_handler(text="5-Lokatsiya")
async def Location(mess:types.Message):

    await mess.answer_location(longitude=40.55918026341861,latitude=71.0374780561142)




#nomerlar jamlammasi
Kontakt=ReplyKeyboardMarkup(
    keyboard=[

    [    KeyboardButton("1-Nomer"),
        KeyboardButton("2-Nomer"),
        KeyboardButton("3-Nomer")
        ],
        [
            KeyboardButton("4-Nomer"),
            KeyboardButton("Orqaga"),
            KeyboardButton("5-Nomer")
    ]
    ],
    resize_keyboard=True
)
#Nomerlar jamlanmasi
@dp.message_handler(text="1-Nomer")
async def Contact(mess:types.Message):
    id="998946837954"
    await mess.answer_contact(id,first_name="Abdulloh")

@dp.message_handler(text="2-Nomer")
async def Contact(mess:types.Message):
    id="998909606699"
    await mess.answer_contact(id,first_name="Boho Nura")



@dp.message_handler(text="3-Nomer")
async def Contact(mess:types.Message):
    id="998974047244"
    await mess.answer_contact(id,first_name="Fazliddin Sinf")

@dp.message_handler(text="4-Nomer")
async def Contact(mess:types.Message):
    id="998971986066"
    await mess.answer_contact(id,first_name="Izzat")

@dp.message_handler(text="5-Nomer")
async def Contact(mess:types.Message):
    id="998998112151"
    await mess.answer_contact(id,first_name="Jabbor")

















@dp.message_handler(text="Orqaga")
async def back(message: types.Message):
    await message.answer("Bosh menu", reply_markup=kontent_keyboard)







@dp.callback_query_handler(text="gips")
async def gipsnarxi(call: CallbackQuery):
    url = "https://img1.freepng.ru/20180919/yev/kisspng-logo-knauf-font-vector-graphics-brand-knauf-logo-svg-vector-amp-png-transparent-vect-5ba2f319918544.2530618215374057215961.jpg"
    await call.message.answer_photo(url, caption="Gips narxi 30 000 so'm")

# bu sement handleri
@dp.callback_query_handler(text="sement")
async  def sementnarx(call:CallbackQuery):
    # url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.olx.uz%2Fd%2Fobyavlenie%2Fsement-cement-tsement-tsiment-dostavka-m500-s-pervyh-ruk-s-vagona-ID2E8FQ.html&psig=AOvVaw21oXb23ZoTvVLQ3YdMUIsx&ust=1652592730010000&source=images&cd=vfe&ved=0CAkQjRxqFwoTCLj3te6h3vcCFQAAAAAdAAAAABAD"
    url = "https://st2.depositphotos.com/1029541/6378/i/600/depositphotos_63780727-stock-photo-bags-of-cement.jpg"
    await  call.message.answer_photo(url,caption="Sement narxi 20 000 so'm")

@dp.callback_query_handler(text="kraska")
async  def kraskanarx(call:CallbackQuery):
    idkraska = "AgACAgIAAxkBAAEPxnxif0JT2fbmTLl8-6Ok6yMGfbj3SAACGbkxG-uV-EshxmctoMO-_QEAAwIAA3MAAyQE"
    await call.message.answer_photo(idkraska, caption="25 000 so'm")

@dp.callback_query_handler(text="truba")
async  def Trubanarx(call:CallbackQuery):
    trubapng = InputFile(path_or_bytesio="photos/img.png")
    await  call.message.answer_photo(trubapng, caption="35 000 so'm")

@dp.callback_query_handler(text="mix")
async def Mixnarx(call:CallbackQuery):
    url="https://files.glotr.uz/company/000/004/049/products/2017/11/01/15095169078020-d0f566cc12d0fa8399fca4a27962fb04.jpg?_=ozbol"
    await  call.message.answer_photo(url,caption="40 000 so'm")

@dp.callback_query_handler(text="armatura")
async def Armaturanarx(call:CallbackQuery):
    photoId="AgACAgIAAxkBAAEPxoJif0Sgck3pYWcbK-7PdHtpYR0wMwACHbkxG-uV-EtfyuQIqKnqEwEAAwIAA3MAAyQE"
    await  call.message.answer_photo(photoId,caption="50 000 so'm")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
23    This handler will be called when user sends `/start` or `/help` command
24    """
    await message.answer(f"Assolomu Alaykum {message.from_user.full_name}\n {message.from_user.username}", reply_markup=kontent_keyboard)
    # await message.answer("https://t.me/JomiyStroy/1652")
    # await message.answer_location(latitude=41.34975, longitude=69.252883)

# async def voice(mess:types.Message):
#     await mess.answer("Kimning ovozi")


@dp.message_handler(content_types="document")
async def document(mess:types.Message):
    await mess.answer("Kimning Documenti")


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def contact(mess:types.Message):
    await mess.answer("Kimning Nomeri")

@dp.message_handler(content_types=types.ContentType.ANIMATION)
async def animation(mess:types.Message):
    await mess.answer("Kimning Gifi")

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def animation(mess:types.Message):
    await  mess.answer("Kimning Manzili")









@dp.message_handler(content_types=types.ContentType.PHOTO)
async def Foto(message:types.Message):
    await message.answer("Bu kimning rasmi")

# Bu fotolar bo'limi
@dp.message_handler(text="Foto")
async def foto(mes: types.Message):
    await mes.answer("Bu rasm!", reply_markup=fotolar)


# Bu videolar bolimi
@dp.message_handler(text="Video")
async def foto(mes: types.Message):
    await mes.answer("Bu Video!", reply_markup=videolar)

# Bu giflar bolimi
@dp.message_handler(text="Gif")
async def foto(mes: types.Message):
    await mes.answer("Bu Gif!", reply_markup=giflar)

# Bu Audio bolimi
@dp.message_handler(text="Audio")
async def foto(mes: types.Message):
    await mes.answer("Bu Audio!", reply_markup=Audio)

# Bu ovoz bolimi
@dp.message_handler(text="Ovoz")
async def foto(mes: types.Message):
    await mes.answer("Bu Ovoz!", reply_markup=Ovoz)

# Bu Lokatsiya bolimi
@dp.message_handler(text="Lokatsiya")
async def foto(mes: types.Message):
    await mes.answer("Bu Manzil!", reply_markup=Lokatsiya)

# Bu Contact bolimi
@dp.message_handler(text="Kontakt")
async def foto(mes: types.Message):
    await mes.answer("Bu Nomer!", reply_markup=Kontakt)




@dp.message_handler()
async def echo(message: types.Message):
    # old style:
   # await bot.send_message(message.chat.id, message.text)

   await message.answer("Bu buyruq hozircha mavjud emas!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)