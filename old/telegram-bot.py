import logging
import os
import datetime
import webbrowser
import pyshorteners

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)
from chatgpt_client import request_chat_gpt
from dalle_client import request_dalle

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
s = pyshorteners.Shortener()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in [117207120, 242737658, 6907698061]:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="get the hell outta here.")
    else:
        response = request_chat_gpt(update.message.text)
        # print(context.chat_data)
        print(update.message.text)
        with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
        response = request_chat_gpt(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        print(response)
        with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
        # response = request_dalle(update.message.text)
        # shortened_response = s.tinyurl.short(response)
        # await context.bot.send_message(chat_id=update.effective_chat.id, text=shortened_response)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)

    application.run_polling()