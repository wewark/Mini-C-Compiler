import csv
import re


class Token:
    def __init__(self, value):
        self.name = Token.getType(value)
        self.value = value

    def __repr__(self):
        return self.name
        # return '<' + self.type + '> : ' + self.value

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
        # lines = open('dict.csv').readlines()
        # for line in lines:
        #     temp_line = line.split()
        #     Token.token_dict[temp_line[0]] = temp_line[1]
