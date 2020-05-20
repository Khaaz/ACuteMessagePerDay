import time
from datetime import datetime
from Parser import Parser
from SentenceManager import SentenceManager

class TweetBot:
    api = None
    parser = None
    love_sentenceManager = None
    toMention = None

    def __init__(self, api, mention):
        self.api = api
        self.toMention = mention
        
        self.parser = Parser()
        
        self.love_sentenceManager = SentenceManager('configs/love_sentences.json', self.parser)
        
    def start(self):
        self.execute()
    
    def execute(self):
        now = datetime.now()
        if now.hour == 10:
            self.postMessage(True)
        
        time.sleep(55 * 60) # sleep 55 min
        self.execute()

    def postMessage(self, mention):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ': Posting...')
        self.api.update_status(self.love_sentenceManager.get() + ((' @' + self.toMention) if mention else ''))

