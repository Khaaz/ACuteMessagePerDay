import tweepy as tp
import json
import time

from TweetBot import TweetBot

configs = {}

with open('configs/config.json', 'r') as f:
    configs = json.load(f)

for distro in configs:
    print(distro)
    print(configs[distro])

# login to twitter account api
auth = tp.OAuthHandler(configs['consumer_key'], configs['consumer_secret'])
auth.set_access_token(configs['access_token'], configs['access_secret'])
api = tp.API(auth)

Bot = TweetBot(api)

Bot.start()