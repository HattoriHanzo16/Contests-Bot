from dotenv import load_dotenv
import os
import json
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

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


def test(update, context):
    update.message.reply_text(
        text=" # Hey there {first_name} How are you ?", parse_mode=telegram.ParseMode.MARKDOWN_V2)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('test', test))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
