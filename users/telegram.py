from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

TOKEN = '7118061424:AAHCdRyEZ2k7L98fBaxfYfYDzg1enKuBizE'

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Yaxshimisiz Tasdiqlash kodini olish uchun email manzilingizni kiriting.')

def send_verification_code(update: Update, context: CallbackContext):
    email = update.message.text
    code = ''.join(random.choices('0123456789', k=6))

    update.message.reply_text(f"Sizning tasdiqlash kodingiz: {code} {email}")


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, send_verification_code))

updater.start_polling()
updater.idle()























# import requests
# from telegram import Bot
# import asyncio

# def get_chat_id(bot_token):
#     url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
#     response=requests.get(url)

#     if response.status_code==200:
#         data=response.json()
#         if data['result']:

#             chat_id=data['result'][0]['message']['chat']['id']
#             return chat_id
#         else:
#             print("no updates found")
#     else:
#         print(f"error code:{response.status_code}")

# async def send_message(bot_token,chat_id,text):
#     bot=Bot(token=bot_token)
#     await bot.send_message(chat_id=chat_id,text=text)

# chat_id=get_chat_id('7118061424:AAHCdRyEZ2k7L98fBaxfYfYDzg1enKuBizE')


# async def main(text):
#     await send_message('7118061424:AAHCdRyEZ2k7L98fBaxfYfYDzg1enKuBizE',chat_id,text)
