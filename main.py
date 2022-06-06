from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import logging
from aiogram.types import \
    InlineKeyboardMarkup, \
    InlineKeyboardButton, \
    CallbackQuery, \
    InputFile, ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Regexp
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
API_TOKEN = '5373327609:AAH-Ak7tDjwaUabAguKhuRRBMDUbtmT4DyA'

logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token="5333798389:AAExodDeDbcOaB_GIzrxhKHYr_-LaFRo-fQ")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Info(StatesGroup):
    name = State()  # Will be represented in storage as 'Form:name'
    age = State()  # Will be represented in storage as 'Form:age'
    phone=State()



phonefiltr = r"^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
email = r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+"
Vaqtlar=r"(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})"
Rassword=r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$"
ipadress=r"(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}"
# @dp.message_handler(Regexp(phonefiltr))
# async def regexhandler(mes: Message):
#     await mes.answer("Telefon raqamingiz qabul qilindi !")

@dp.message_handler(Regexp(email))
async def emailhandler(mes: Message):
    await mes.answer("Emailingiz qabul qilindi !")

@dp.message_handler(Regexp(Vaqtlar))
async def Vaqtlarhandler(mess:Message):
    await mess.answer("Vaqt kiritildi")

@dp.message_handler(Regexp(Rassword))
async def Rassworhandler(mess:Message):
    await mess.answer("Kod kiritildi")

@dp.message_handler(Regexp(ipadress))
async def Ipadresshandler(mess:Message):
    await mess.answer("ipadresss kiritildi")






@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.answer("Bosh menu",reply_markup=stroy_keyboard)


@dp.message_handler(commands=["aloqa"])
async def aloqaadmin(message:types.Message):
    await message.answer("Admin @Abdulfoyix777")

xaridlar = """@knaufgipsokarton  +99899 8022138  +99890 9339395"""
@dp.message_handler(commands=["xarid"])
async def xaridadmin(message:types.Message):
    await message.answer("ismingizni kiriting")
    await Info.name.set()



@dp.message_handler(state=Info.name)
async def Xaridlar(mess:Message,state:FSMContext):
    name=mess.text
    await state.update_data(name=name)
    await  mess.answer("Yoshingizni kiriting")
    await Info.next()


@dp.message_handler(state=Info.age)
async def Xaridlar(mess:Message,state:FSMContext):
    age=mess.text
    await state.update_data(age=age)
    await  mess.answer("No'merizni kiriting")
    await Info.next()



@dp.message_handler(Regexp(phonefiltr),state=Info.phone)
async def Xaridlar(mess:Message,state:FSMContext):
    phone=mess.text
    await state.update_data(phone=phone)
    data=await state.get_data()
    name=data.get("name")
    age=data.get("age")
    phone=data.get("phone")
    message=f"Siznin ma'lumotlaringiz\n{name,age,phone}"
    await mess.answer(message)
    await state.finish()


@dp.message_handler(state=[Info.name,Info.age,Info.phone])
async def xaridadmin(message:types.Message):
    await message.answer("Noto'g'ri buyrug'")









stroy_keyboard= InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Гипсокартон", callback_data="Гип"),
            InlineKeyboardButton(text="Sement", callback_data="sement")
        ],
        [
            InlineKeyboardButton(text="Kraska", callback_data="kraska"),
            InlineKeyboardButton(text="Truba", callback_data="truba")

        ],
        [
            InlineKeyboardButton(text="Armatura", callback_data="armatura"),
            InlineKeyboardButton(text="Mix", callback_data='mix')
        ],
        [
             InlineKeyboardButton(text="Drenaj membrana",callback_data="DR"),
             InlineKeyboardButton(text="Бур ЗВЕРЬ",callback_data="Zver")

        ],
        [
            InlineKeyboardButton(text="Antipas",callback_data="anti"),
            InlineKeyboardButton(text="Asbestovaya truba",callback_data="abses")

        ],

        ]
)

gipsokarton_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-gipsokarton", callback_data="1-gip"),
            InlineKeyboardButton(text="2-gipsokarton", callback_data="2-gip")
        ],
        [
            InlineKeyboardButton(text="Bosh menu", callback_data="Bosh menu")
        ]
    ]
)


sement_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-sement", callback_data="1-sem"),
            InlineKeyboardButton(text="2-sement", callback_data="2-sem")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)


kraska_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-kraska", callback_data="1-kr"),
            InlineKeyboardButton(text="2-kraska", callback_data="2-kr")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)



truba_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-truba", callback_data="1-tr"),
            InlineKeyboardButton(text="2-truba", callback_data="2-tr")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)


armatura_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-Armatura", callback_data="1-ar"),
            InlineKeyboardButton(text="2-Armatura", callback_data="2-ar")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)


mix_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-mix", callback_data="1-mx"),
            InlineKeyboardButton(text="2-mix", callback_data="2-mx")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)


Drenej_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-drej", callback_data="1-dr"),
            InlineKeyboardButton(text="2-drej", callback_data="2-dr")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)



Zver_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-zver", callback_data="1-zv"),
            InlineKeyboardButton(text="2-zver", callback_data="2-zv")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)


anti_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-antipas", callback_data="1-an"),
            InlineKeyboardButton(text="2-antipas", callback_data="2-an")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)



abses_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-abses", callback_data="1-ab"),
            InlineKeyboardButton(text="2-abses", callback_data="2-ab")
        ],
        [
            InlineKeyboardButton(text="Asosiy menu", callback_data="Bosh menu")
        ]
    ]
)










# 1. Gipsokarton bo'limi
@dp.callback_query_handler(text="Гип")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Gipsokarton bo'limi: ", reply_markup=gipsokarton_inline)

@dp.callback_query_handler(text="1-gip")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1628"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-gipsokarton 45 000 so'm", reply_markup=gipsokarton_inline)


@dp.callback_query_handler(text="2-gip")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1646"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-gipsokarton 50 000 so'm", reply_markup=gipsokarton_inline)

#Semen bo'limi
@dp.callback_query_handler(text="sement")
async def sement(call:CallbackQuery):
    await call.message.delete()
    await call.message.answer("Sementlar bolimi",reply_markup=sement_inline)

@dp.callback_query_handler(text="1-sem")
async def sement1(call:CallbackQuery):
    url="https://t.me/JomiyStroy/1645"
    await call.message.delete()
    await call.message.answer_photo(url,caption="1sement 45 000 so'm",reply_markup=sement_inline)


@dp.callback_query_handler(text="2-sem")
async  def sement2(call:CallbackQuery):
    url="https://t.me/JomiyStroy/1644"
    await call.message.delete()
    await call.message.answer_photo(url,caption="2-semen 60 000 so'm",reply_markup=sement_inline)



# 2. Sement bo'limi
@dp.callback_query_handler(text="sement")
async def Foto1(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1598"
    await call.message.delete()
    await call.message.answer("Sement bo'limi: ", reply_markup=sement_inline)




# 1. Kraska bo'limi
@dp.callback_query_handler(text="kraska")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kraska bo'limi: ", reply_markup=kraska_inline)

@dp.callback_query_handler(text="1-kr")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1353"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-Kraska 65 000 so'm", reply_markup=kraska_inline)


@dp.callback_query_handler(text="2-kr")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1326"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-Kraska 50 000 so'm", reply_markup=kraska_inline)






@dp.callback_query_handler(text="kraska")
async def Foto3(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1353"
    await call.message.delete()
    await call.message.answer_photo(url,caption="Polimax"
                                                "50 000 som")



# 1. Truba bo'limi
@dp.callback_query_handler(text="truba")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Truba bo'limi: ", reply_markup=truba_inline)

@dp.callback_query_handler(text="1-tr")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1641"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-Truba 45 000 so'm", reply_markup=truba_inline)


@dp.callback_query_handler(text="2-tr")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1642"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-Truba 80 000 so'm", reply_markup=truba_inline)



# 1. Armatura bo'limi
@dp.callback_query_handler(text="armatura")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Armatura bo'limi: ", reply_markup=armatura_inline)

@dp.callback_query_handler(text="1-ar")
async def ar1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1655"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-armatura 45 000 so'm", reply_markup=armatura_inline)


@dp.callback_query_handler(text="2-ar")
async def ar2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1656"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-armatura 40 000 so'm", reply_markup=armatura_inline)



@dp.callback_query_handler(text="armatura")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1654"
    await call.message.delete()
    await call.message.answer_photo(url,caption="fuga"
                                                "70 000 som")


# 1. Mix bo'limi
@dp.callback_query_handler(text="mix")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Mix bo'limi: ", reply_markup=mix_inline)

@dp.callback_query_handler(text="1-mx")
async def ar1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1658"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-mix 85 000 so'm", reply_markup=mix_inline)


@dp.callback_query_handler(text="2-mx")
async def ar2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1657"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-mix 66 000 so'm", reply_markup=mix_inline)



# 1. Drenej bo'limi
@dp.callback_query_handler(text="DR")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Drenej bo'limi: ", reply_markup=Drenej_inline)

@dp.callback_query_handler(text="1-dr")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1660"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-Drenej 45 000 so'm", reply_markup=Drenej_inline)


@dp.callback_query_handler(text="2-dr")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1661"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-Drej 54 000 so'm", reply_markup=Drenej_inline)


# 1. Zver  bo'limi
@dp.callback_query_handler(text="Zver")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Zver bo'limi: ", reply_markup=Zver_inline)

@dp.callback_query_handler(text="1-zv")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1662"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-Zver 75 000 so'm", reply_markup=Zver_inline)


@dp.callback_query_handler(text="2-zv")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1663"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-Zver 84 000 so'm", reply_markup=Zver_inline)


# 1. Antipas  bo'limi
@dp.callback_query_handler(text="anti")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Anti bo'limi: ", reply_markup=anti_inline)

@dp.callback_query_handler(text="1-an")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1664"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-Zver 35 000 so'm", reply_markup=anti_inline)


@dp.callback_query_handler(text="2-an")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1640"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-anti 74 000 so'm", reply_markup=anti_inline)



# 1. Abses  bo'limi
@dp.callback_query_handler(text="abses")
async def Foto1(call:types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Abses bo'limi: ", reply_markup=abses_inline)

@dp.callback_query_handler(text="1-ab")
async def gip1(call : CallbackQuery):
    url="https://t.me/JomiyStroy/1639"
    await call.message.delete()
    await call.message.answer_photo(url, caption="1-Abses 25 000 so'm", reply_markup=abses_inline)


@dp.callback_query_handler(text="2-ab")
async def gip2(call: CallbackQuery):
    url= "https://t.me/JomiyStroy/1638"
    await call.message.delete()
    await call.message.answer_photo(url, caption="2-Abses 44 000 so'm", reply_markup=abses_inline)











@dp.callback_query_handler(text="kraska")
async def Foto3(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1353"
    await call.message.answer_photo(url,caption="Polimax"
                                                "50 000 som")


@dp.callback_query_handler(text="truba")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1653"
    await call.message.answer_photo(url,caption="Pulmax"
                                                "75 000 som")



@dp.callback_query_handler(text="mix")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1308"
    await call.message.answer_photo(url,caption="Megamix"
                                                "55 000 som")

@dp.callback_query_handler(text="DR")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1650"
    await call.message.answer_photo(url,caption="Drej"
                                                "50 000 som")

@dp.callback_query_handler(text="Zver")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1651"
    await call.message.answer_photo(url,caption="Zver"
                                                "50 000 som")


@dp.callback_query_handler(text="anti")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1652"
    await call.message.answer_photo(url,caption="Anti"
                                                "66 000 som")

@dp.callback_query_handler(text="abses")
async def Foto4(call:types.CallbackQuery):
    url="https://t.me/JomiyStroy/1649"
    await call.message.answer_photo(url,caption="Abses"
                                                "77 000 som")








@dp.callback_query_handler(text="Гипсокартон")
async def Gips(call:types.CallbackQuery):
    await call.message.answer("Qurilish mollar!!!")


@dp.callback_query_handler(text="Bosh menu")
async def boshmenu(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bosh menu", reply_markup=stroy_keyboard)








@dp.message_handler()
async def echo(message: types.Message):
    # old style:
   # await bot.send_message(message.chat.id, message.text)

   await message.answer("Bu buyruq hozircha mavjud emas!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
