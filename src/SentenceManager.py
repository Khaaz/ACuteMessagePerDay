import copy
import random
import json

class SentenceManager:
    all_sentences = []
    cur_sentences = []
    parser = None

    def __init__(self, path, parser):
        with open(path, 'r') as f:
            self.all_sentences = json.load(f)
        
        self.parser = parser
        self.cur_sentences = copy.copy(self.all_sentences)

    def get(self):
        if len(self.cur_sentences) == 0:
            self.cur_sentences = copy.copy(self.all_sentences)

        index = random.randrange(0, len(self.cur_sentences))

        return self.parser.parse(self.cur_sentences.pop(index))
