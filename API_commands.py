from telegram.ext import Updater, CommandHandler
from API_service import fetch
import datetime


'''
TODO: 1.Get the dates formating correctly
      2.Get the duration calculation [X]
      3.Figure out how many to render at one call
      4.Sort the Fetched list according to starting dates close to current date 
'''



from bot import CUSTOM_KEYBOARD


 #Util Function
def secondstohours(seconds):
    return str(datetime.timedelta(seconds=int(seconds.split('.')[0])))


def soon(update, context):
    red_circle_emoji = '\U0001f534'
    data = [i for i in fetch('all') if i['in_24_hours']]
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} By {contest['site']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def CodeForces(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('codeforces')
    text = []
    for contest in data[:3]:
        curr = f"{red_circle_emoji} {contest['name']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def TopCoder(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('top_coder')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def AtCoder(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('at_coder')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def CodeChef(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('code_chef')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def CSAcademy(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('cs_academy')
    if len(data) == 0:
        curr = f"{red_circle_emoji} No upcoming contests are avaliable {red_circle_emoji}"
        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)
        return

    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def HackerRank(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('hacker_rank')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def HackerEarth(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('hacker_earth')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} By  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def KickStart(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('kick_start')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def LeetCode(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('leet_code')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)
