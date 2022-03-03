from telegram.ext import Updater, CommandHandler
from API_service import fetch
from datetime import datetime


'''
TODO: 1.Get the dates formating correctly
      2.Get the duration calculation
      3.Figure out how many to render at one call
      4.Sort the Fetched list according to starting dates close to current date 
'''


def secondstohours(seconds):
    return 123


def soon(update, context):
    red_circle_emoji = '\U0001f534'
    data = [i for i in fetch('all') if i['in_24_hours']]
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} By {contest['site']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def CodeForces(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('codeforces')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def TopCoder(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('top_coder')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def AtCoder(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('at_coder')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def CodeChef(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('code_chef')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def CSAcademy(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('cs_academy')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def HackerRank(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('hacker_rank')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def HackerEarth(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('hacker_earth')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']} By  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def KickStart(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('kick_start')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)


def LeetCode(update, context):
    red_circle_emoji = '\U0001f534'
    data = fetch('leet_code')
    text = []
    for contest in data[:3]:

        curr = f"{red_circle_emoji} {contest['name']}  \n" \
               f"duration: {secondstohours(contest['duration'])} hours \n"\
               f"CHECK IT OUT ON {contest['url']}"

        update.message.reply_text(curr)
