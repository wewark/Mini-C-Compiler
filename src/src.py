
from lexical_analyzer.lexical_analyzer import LexicalAnalyzer
from cfg_parser.parser import Parser

def main():
    code_file = 'sample_code.cpp'
    rules_file = 'grammar.txt'
    tokens_file = 'dict.csv'

    lex = LexicalAnalyzer()
    tokens = lex.analyze(code_file)
    parser = Parser(rules_file, tokens_file)
    parser.generate_parse_tree(tokens)


if __name__ == "__main__":
    main()
