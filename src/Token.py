import csv
import re


class Token:
    def __init__(self, value):
        self.type = Token.getType(value)
        self.value = value

    def __repr__(self):
        return '<' + self.type + '> : ' + self.value

    @staticmethod
    def getType(value):
        for key, val in Token.token_dict.items():
            regex = '^' + val + '$'
            if re.match(regex, value):
                return key
        return 'ERROR'

    token_dict = {}

    @staticmethod
    def load_dict():
        with open('dict.csv') as f:
            reader = csv.reader(f, delimiter=' ')
            for row in reader:
                Token.token_dict[row[0]] = row[1]
