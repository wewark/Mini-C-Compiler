import re
import csv
from .Token import Token


class LexicalAnalyzer():
    def __init__(self):
        Token.load_dict()

        reg_list = [val for _, val in Token.token_dict.items()]
        self.regex = '(' + '|'.join(reg_list) + ')'
        self.regex = re.compile(self.regex)

    def analyze(self, code_file_name):
        """Analyze code and return a stream of tokens."""
        code = open(code_file_name).readlines()
        code = ''.join(code)
        result = self.regex.findall(code)

        tokens = [Token(i) for i in result]

        with open('tokens.txt', 'w') as out:
            for token in tokens:
                out.write(str(token) + '\n')
        return tokens
