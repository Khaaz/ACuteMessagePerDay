import tweepy as tp
import json
import time

from TweetBot import TweetBot

configs = {}

with open('configs/config.json', 'r') as f:
    configs = json.load(f)

# login to twitter account api
print('Load KEYS...')
auth = tp.OAuthHandler(configs['consumer_key'], configs['consumer_secret'])
auth.set_access_token(configs['access_token'], configs['access_secret'])
api = tp.API(auth)

print('Instanciate Bot...')
Bot = TweetBot(api, configs['mention'])

print('Start Bot...')
Bot.start()