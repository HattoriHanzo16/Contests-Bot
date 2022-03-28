
#Emojis
red_circle_emoji = '\U0001f534'
bellhop_emoji = '\U0001f6CE'
clock_emoji = '\U0001F567'
rocket_emoji = '\U0001F680'
prohibited_emoji = '\U0001F6Ab'
stopwatch_emoji = '\U0001f55b'
pushpin_emoji = '\U0001F4CD'
hey_emoji = '\U0001f44b'
wink_emoji = '\U0001f609'


#Util Functions for data processing

import datetime

def secondstohours(seconds):
    return str(datetime.timedelta(seconds=int(seconds.split('.')[0])))

def startdate(date):
    try:
        d = datetime.datetime.fromisoformat(date[:-1]).astimezone(datetime.timezone.utc)
        return d.strftime('%Y-%m-%d %H:%M:%S') + ' UTC'
    except:
        return date




