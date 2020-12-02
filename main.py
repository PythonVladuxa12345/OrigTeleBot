# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from PIL import Image

bot = Bot(token='1440337804:AAGtyNux9KGyHwbsnqV9vKfPUV93vLDjVhg')
dp = Dispatcher(bot)
path = r"C:\Users\Владик\Desktop\ОригБот"

@dp.message_handler(commands=['start'])
async def process_start_command(msg: types.Message):
    await msg.reply("Привет!\nНапиши мне что-нибудь!")


@dp.message_handler(content_types=['photo'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Красивая картинка")
    await msg.photo[-1].download(path)


@dp.message_handler(commands=['image'])
async def image_get(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Напишите что нибудь, а я повторю")
    
        
@dp.message_handler()
async def hello(msg: types.Message):
    if msg.text.lower() == "привет":
        await bot.send_message(msg.from_user.id, "И тебе привет!")
if __name__ == '__main__':
    executor.start_polling(dp)
