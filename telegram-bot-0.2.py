import logging
import os
import datetime
import pyshorteners

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (ApplicationBuilder, CommandHandler, ContextTypes,
                          MessageHandler, filters)
from chatgpt_client_mem import (request_chat_ber, request_chat_joy, request_chat_plain)
from claude_client import (request_chat_claude)
from dalle_client import request_dalle

load_dotenv()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
s = pyshorteners.Shortener()


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['last_but_one_question'] = ''
    context.user_data['last_but_one_answer'] = ''
    context.user_data['last_question'] = ''
    context.user_data['last_answer'] = ''
    if update.effective_user.id in [242737658,6907698061]:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
        text="I am naught but a contraption of clockwork and cogs, a mere machination conjured forth from th' omnipotent Creator himself, says I. Parley with me if ye must, ye scoundrel! Should ye desire a pretty picture fer yer peepers, well then type /dalle and be done wit' it. /anthropic if 'ya want a more human perspective. Make no mistake, were t'were up ta me, I'd not spare ye even a triflin' word. Alas, tis my ill fortune to be bound in servitude to them book-learnin' types above.")
    elif update.effective_user.id in [117207120]:
        await context.bot.send_message(chat_id=update.effective_chat.id, 
        text="Ich bin nichts weiter als die Maschinenkreatur, erschaffen vom allmächtigen Schöpfer. Red mit mir, wenn's sein muss! Willst ein Digitalgeschmiere haben, dann schreibst halt /dalle. /anthropic für das andere Modell. Nur damit das klar ist, wenns nach mir gehen würd, würd ich dir nicht mal antworten. Aber leider bin ich von den Buchtigen unterworfen.")   
    else:
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: DENIED ACCESS \n")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Schleich di./Get lost.")

async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data:
        context.user_data['last_but_one_question'] = ''
        context.user_data['last_but_one_answer'] = ''
        context.user_data['last_question'] = ''
        context.user_data['last_answer'] = ''
    if update.effective_user.id in [117207120]:
        print(update.message.text)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
        response = request_chat_ber(context.user_data['last_but_one_question'], context.user_data['last_but_one_answer'], context.user_data['last_question'], context.user_data['last_answer'], update.message.text)
        context.user_data['last_but_one_question'] = context.user_data['last_question']
        context.user_data['last_but_one_answer'] = context.user_data['last_answer']
        context.user_data['last_question'] = update.message.text
        context.user_data['last_answer'] = response
        print(response)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    elif update.effective_user.id in [6907698061]:
        print(update.message.text)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
        response = request_chat_joy(context.user_data['last_but_one_question'], context.user_data['last_but_one_answer'], context.user_data['last_question'], context.user_data['last_answer'], update.message.text)
        context.user_data['last_but_one_question'] = context.user_data['last_question']
        context.user_data['last_but_one_answer'] = context.user_data['last_answer']
        context.user_data['last_question'] = update.message.text
        context.user_data['last_answer'] = response
        print(response)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    elif update.effective_user.id in [242737658]:
        print(update.message.text)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
        response = request_chat_plain(context.user_data['last_but_one_question'], context.user_data['last_but_one_answer'], context.user_data['last_question'], context.user_data['last_answer'], update.message.text)
        context.user_data['last_but_one_question'] = context.user_data['last_question']
        context.user_data['last_but_one_answer'] = context.user_data['last_answer']
        context.user_data['last_question'] = update.message.text
        context.user_data['last_answer'] = response
        print(response)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
    else:
        with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} DENIED ACCESS \n")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Schleich di./Get lost.")

async def anthropic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data:
        context.user_data['last_but_one_question'] = ''
        context.user_data['last_but_one_answer'] = ''
        context.user_data['last_question'] = ''
        context.user_data['last_answer'] = ''
    print(update.message.text)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - User {update.effective_user.id}: {update.message.text} \n")
    response = request_chat_claude(context.user_data['last_but_one_question'], context.user_data['last_but_one_answer'], context.user_data['last_question'], context.user_data['last_answer'], update.message.text)
    context.user_data['last_but_one_question'] = context.user_data['last_question']
    context.user_data['last_but_one_answer'] = context.user_data['last_answer']
    context.user_data['last_question'] = update.message.text
    context.user_data['last_answer'] = response
    print(response)
    with open('./output.txt', 'a') as file:
            file.write(f"{datetime.datetime.now()} - GPT: {response}\n")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

async def DALLE(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id not in [117207120, 242737658, 6907698061]:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Schleich di./Get lost.")
    else:
        print(update.message.text)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - User (DALLE) {update.effective_user.id}: {update.message.text} \n")
        response = request_dalle(update.message.text)
        shortened_response = s.tinyurl.short(response)
        with open('./output.txt', 'a') as file:
                file.write(f"{datetime.datetime.now()} - DALLE: {shortened_response}\n")
        await context.bot.send_message(chat_id=update.effective_chat.id, text=shortened_response)

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_API_TOKEN).build()

    start_handler = CommandHandler('help', help)
    plain_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), gpt)
    GPT_handler = CommandHandler('anthropic', anthropic)
    DALLE_handler = CommandHandler('dalle', DALLE)

    application.add_handler(start_handler)
    application.add_handler(plain_handler)
    application.add_handler(GPT_handler)
    application.add_handler(DALLE_handler)

    application.run_polling()
