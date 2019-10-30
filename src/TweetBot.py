import time
from datetime import datetime
from SentenceManager import SentenceManager

class TweetBot:
    def __init__(self, api):
        self.api = api
        self.sentenceManager = SentenceManager('configs/sentences.json')
        
    def start(self):
        self.execute()
    
    def execute(self):
        now = datetime.now()
        if now.hour == 10:
            self.postMessage(True)
        if now.hour == 19:
            self.postMessage(False)
        
        time.sleep(45 * 60)
        self.execute()

    def postMessage(self, mention):
        self.api.update_status(self.sentenceManager.get() + ' @louisonb_' if mention else '')

