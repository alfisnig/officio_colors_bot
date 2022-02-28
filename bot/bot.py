"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from constants import LOG_FILE_PATH
from aiogram import Bot, Dispatcher, executor, types
from .config import API_TOKEN


logging.getLogger(LOG_FILE_PATH)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


def start_bot():
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logging.error("Ошибка: ", exc_info=True)


def stop_bot():
    dp.stop_polling()


if __name__ == '__main__':
    start_bot()
