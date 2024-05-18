import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram import F
from aiogram.types import Message,CallbackQuery,InputFile,FSInputFile
import io
from removebg import remove_bg
from inlinebuttons import colors_button

TOKEN = "7083075969:AAGXj8oUQ_PVxwONVZ47chbiA4xlg-bYtgE"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    full_name = message.from_user.full_name
    text = f"Assalomu alaykum, {full_name}\nBu bot rasm orga fonni o'chirib beradi. Botdan foydalanish uchun rasm yuborilgan!!!"
    await message.reply(text=text)

@dp.message(F.photo)
async def name(message: Message):
    file_id = message.photo[-1].file_id
    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    global photos_url
    photos_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    
    await message.answer_photo(photo=file_id,reply_markup=colors_button)
    # await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png")) await message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"))

@dp.callback_query(F.data=="black")
async def black_handler(callback:CallbackQuery):
    await callback.answer("Bu qora")
    # await callback.message.answer("Qorani bosdingiz")
    rasm = remove_bg(photos_url,"black")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()

@dp.callback_query(F.data=="white")
async def white_handler(callback:CallbackQuery):
    await callback.answer("Bu oq")
    # await callback.message.answer("Qorani bosdingiz")
    rasm = remove_bg(photos_url,"white")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()
    
@dp.callback_query(F.data=="yellow")
async def white_handler(callback:CallbackQuery):
    await callback.answer("Bu sariq")
    # await callback.message.answer("Qorani bosdingiz")
    rasm = remove_bg(photos_url,"yellow")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()
    
@dp.callback_query(F.data=="red")
async def white_handler(callback:CallbackQuery):
    await callback.answer("Bu qizil")
    # await callback.message.answer("Qorani bosdingiz")
    rasm = remove_bg(photos_url,"red")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()
    
@dp.callback_query(F.data=="blue")
async def white_handler(callback:CallbackQuery):
    await callback.answer("Bu ko'k")
    # await callback.message.answer("Qorani bosdingiz")
    rasm = remove_bg(photos_url,"blue")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()
    
@dp.callback_query(F.data=="green")
async def white_handler(callback:CallbackQuery):
    await callback.answer("Bu yashil")
    # await callback.message.answer("Qorani bosdingiz")
    rasm = remove_bg(photos_url,"green")
    await callback.message.answer_photo(photo=types.input_file.BufferedInputFile(rasm,filename="no-bg.png"),reply_markup=colors_button)
    await callback.message.delete()

@dp.startup()
async def bot_start():
    await bot.send_message(1245143580,"Botimiz ishga tushdi")

@dp.shutdown()
async def bot_stop():
    await bot.send_message(1245143580,"Xayr")


async def main() -> None:
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

