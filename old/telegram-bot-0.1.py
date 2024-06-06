import logging
import os
import datetime
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


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, 
    # text="I'm a bot, please talk to me! Use /GPT to chat with GPT-4o and /DALLE to generate images.")
    text="Ich bin nichts weiter als die Maschinenkreatur, erschaffen vom allmächtigen Schöpfer. Red mit mir, wenn's sein muss! Wennst GPT-4o nerven willst, schreibst /gpt. Willst a Büdl haben, dann schreibst /dalle. Nur damit das klar ist, es ist interessiert mi überhaupts ned, was du willst.")

async def plain(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
    response = request_chat_gpt(update.message.text)
    print(response)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def chat_GPT(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
    response = request_chat_gpt(update.message.text)
    print(response)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def DALLE(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - User (DALLE) {update.effective_user.id}: {update.message.text} \n")
    response = request_chat_gpt(update.message.text)
    response = request_dalle(update.message.text)
    shortened_response = s.tinyurl.short(response)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - DALLE: {shortened_response}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=shortened_response)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    start_handler = CommandHandler('help', help)
    plain_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), plain)
    # GPT_handler = CommandHandler('gpt', chat_GPT)
    DALLE_handler = CommandHandler('dalle', DALLE)

    application.add_handler(start_handler)
    application.add_handler(plain_handler)
    # application.add_handler(GPT_handler)
    application.add_handler(DALLE_handler)

    application.run_polling()
