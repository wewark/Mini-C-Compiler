import re
import csv
from Token import Token


def main():
    Token.load_dict()

    reg_list = [val for _, val in Token.token_dict.items()]
    regex = '(' + '|'.join(reg_list) + ')'

    regex = re.compile(regex)
    
    code = open('sample_code.cpp').readlines()
    code = ''.join(code)
    result = regex.findall(code)

    tokens = [Token(i) for i in result]
    
    with open('output.txt', 'w') as out:
        for token in tokens:
            out.write(str(token) + '\n')


if __name__ == "__main__":
    main()
