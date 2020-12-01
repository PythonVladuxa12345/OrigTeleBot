# -*- coding: utf-8 -*-
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from PIL import Image

bot = Bot(token='1440337804:AAGtyNux0KGyHwbskqV3vKfPUV31vLDjVhg')
dp = Dispatcher(bot)


@dp.message_handler(commands=['help'])
async def process_start_command(msg: types.Message):
    await msg.reply("Привет!\nБот создан для получения оригинала картинки.\nПришли мне картинку, и я попробую найти оригинал этой картинки!")


@dp.message_handler(content_types=['photo'])
async def process_help_command(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Красивая картинка")
    
@dp.message_handler()
async def echo_message(msg: types.Message):
    if msg.text.lower() == "привет":
        await bot.send_message(msg.from_user.id, "И тебе привет!")


if __name__ == '__main__':
    executor.start_polling(dp)
