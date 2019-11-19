import re

class Parser:
    emotes = {}
    regexp = re.compile('{{(.*?)}}')

    def __init__(self):
        self.emotes = {
            'love': '🥰',
            'heart': '❤️',
            'heart_eyes': '😍',
            'kiss': '😘',
            'smirk': '😏',
        }

    def match(self, sentence):
        return re.findall(self.regexp, sentence)

    def replace(self, sentence, toReplace):
        for match in toReplace:
            sentence = sentence.replace('{{' + match + '}}', self.emotes.get(match, ''))
        return sentence

    def parse(self, sentence):
        toReplace = self.match(sentence)
        return self.replace(sentence, toReplace)
