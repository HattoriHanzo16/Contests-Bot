from telegram.ext import Updater, CommandHandler
from API_service import fetch





from UTIL import *
from bot import CUSTOM_KEYBOARD





def reply(update,context,prefix):
    data = fetch(prefix)
    if len(data) == 0:
           curr = f"{prohibited_emoji} No upcoming contests are avaliable {prohibited_emoji}"
           update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)
           return

    for contest in data[:4]:

        curr = f"{red_circle_emoji} {contest['name']}  {red_circle_emoji} \n \n" \
               f"{clock_emoji} Duration: {secondstohours(contest['duration'])} hours \n"\
               f"{bellhop_emoji} Starting on: {startdate(contest['start_time']) }  \n \n"\
               f"CHECK IT OUT   {rocket_emoji} \n \n"\
               f"{contest['url']}" \


        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)


def soon(update, context):
    data = [i for i in fetch('all') if i['in_24_hours']]
    if len(data) == 0:
        curr = f"{prohibited_emoji} No upcoming contests are avaliable {prohibited_emoji}"
        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)
        return

    for contest in data[:4]:

        curr = f"{red_circle_emoji} {contest['name']} {red_circle_emoji} \n \n" \
               f"{clock_emoji} Duration: {secondstohours(contest['duration'])} hours \n"\
               f"{bellhop_emoji} Starting on: {startdate(contest['start_time'])}  \n \n"\
               f"CHECK IT OUT   {rocket_emoji} \n \n"\
               f"{contest['url']}" \

        update.message.reply_text(curr,reply_markup=CUSTOM_KEYBOARD)




CodeForces = lambda update,context,*_:reply(update,context,'codeforces')
TopCoder = lambda update,context,*_:reply(update,context,'top_coder')
AtCoder = lambda update,context,*_:reply(update,context,'at_coder')
CodeChef = lambda update,context,*_:reply(update,context,'code_chef')
CSAcademy = lambda update,context,*_:reply(update,context,'cs_academy')
HackerRank = lambda update,context,*_:reply(update,context,'hacker_rank')
HackerEarth = lambda update,context,*_:reply(update,context,'hacker_earth')
KickStart = lambda update,context,*_:reply(update,context,'kick_start')
LeetCode = lambda update,context,*_:reply(update,context,'leet_code')

