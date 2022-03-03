from dotenv import load_dotenv
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from API_commands import *


load_dotenv('.env')
TOKEN = os.environ['TOKEN']


def start(update, context):
    first_name = update.message.chat.first_name
    hey_emoji = '\U0001f44b'
    wink_emoji = '\U0001f609'
    text = f'Hey there {first_name} {hey_emoji}, \n' \
        '\n' \
        'Here are the list of the avaliable commands: \n' \
        '\n' \
        '/soon - Get all of the upcoming contests which will start in 24 hours \n' \
        '\n' \
        '/CodeForces - Get all of the upcoming contests from CodeForces \n' \
        '\n' \
        '/TopCoder - Get all of the upcoming contests from TopCoder \n' \
        '\n' \
        '/AtCoder - Get all of the upcoming contests from AtCoder \n' \
        '\n' \
        '/CodeChef - Get all of the upcoming contests from CodeChef \n' \
        '\n' \
        '/CSAcademy - Get all of the upcoming contests from CS Academy \n' \
        '\n' \
        '/HackerRank - Get all of the upcoming contests from CS HackerRank \n' \
        '\n' \
        '/HackerEarth - Get all of the upcoming contests from CS HackerEarth \n' \
        '\n' \
        '/KickStart - Get all of the upcoming contests from Kick Start \n' \
        '\n' \
        '/LeetCode - Get all of the upcoming contests from LeetCode \n' \
        '\n' \
        f'If you forget any of the commands,just type   /help  {wink_emoji} '

    update.message.reply_text(text)


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
