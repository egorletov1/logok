import os

from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

TOKEN = os.getenv("TOKEN")
bot = AsyncTeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    text_message = message.text
    text_message = text_message.lower()
    if "дела" in text_message or "настроение" in text_message:
        await bot.reply_to(message, "Хорошо, а у тебя?" or "Нормально")
    elif "погода" in text_message:
        await bot.reply_to(message, "Отличная" or "Плохая")
    elif "привет" in text_message:
        await bot.reply_to(message, "Привет" or "Здравствуй")
    else:
        await bot.reply_to(message, "Извините, я вас не понял")

@bot.message_handler(commands={"start"})
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, "Приветствую тебя,новый пользователь", disable_notification=True, protect_content=True)

import asyncio
asyncio.run(bot.polling())