from dotenv import load_dotenv
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton
from API_commands import *

load_dotenv('.env')
TOKEN = os.environ['TOKEN']

#Emojis
stopwatch_emoji = '\U0001f55b'
pushpin_emoji = '\U0001F4CD'


CUSTOM_KEYBOARD = ReplyKeyboardMarkup(keyboard=[['/soon'+stopwatch_emoji],[ '/CodeForces'+pushpin_emoji,'/TopCoder'+pushpin_emoji,'/AtCoder'+pushpin_emoji],['/CodeChef'+pushpin_emoji,'/CSAcademy'+pushpin_emoji,'/HackerRank'+pushpin_emoji],['/HackerEarth'+pushpin_emoji,'/KickStart'+pushpin_emoji,'/LeetCode'+pushpin_emoji]])


def start(update, context):
    first_name = update.message.chat.first_name
    hey_emoji = '\U0001f44b'
    wink_emoji = '\U0001f609'
    text = f'Hey there {first_name} {hey_emoji}, \n' \
        f'You can select your favorite website from the given keyboard and find about any upcoming contests from me {wink_emoji} '

    update.message.reply_text(text,reply_markup=CUSTOM_KEYBOARD)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('soon', soon))
    dp.add_handler(CommandHandler('CodeForces', CodeForces))
    dp.add_handler(CommandHandler('TopCoder', TopCoder))
    dp.add_handler(CommandHandler('AtCoder', AtCoder))
    dp.add_handler(CommandHandler('CodeChef', CodeChef))
    dp.add_handler(CommandHandler('CSAcademy', CSAcademy))
    dp.add_handler(CommandHandler('HackerRank', HackerRank))
    dp.add_handler(CommandHandler('HackerEarth', HackerEarth))
    dp.add_handler(CommandHandler('KickStart', KickStart))
    dp.add_handler(CommandHandler('LeetCode', LeetCode))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()