import re
import csv
from Token import Token


def main():
    Token.load_dict()

    reg_list = []
    for _, val in Token.token_dict.items():
        reg_list.append(val)
    regex = '(' + '|'.join(reg_list) + ')'

    regex = re.compile(regex)
    
    code = open('sample_code.cpp').readlines()
    code = ''.join(code)
    result = regex.findall(code)

    tokens = []
    for i in result:
        tokens.append(Token(i))
    
    with open('output.txt', 'w') as out:
        for token in tokens:
            out.write(str(token) + '\n')


if __name__ == "__main__":
    main()
