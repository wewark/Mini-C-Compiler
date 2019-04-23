from .rule import Rule
from .token import Token
from .global_objs import Global
from anytree import Node, RenderTree
from anytree.exporter import DotExporter


class Parser():
    def __init__(self, rules_file, tokens_file):
        Parser.__parse_grammar(rules_file, tokens_file)

    @staticmethod
    def __parse_grammar(rules_file, tokens_file):
        Parser.__parse_rules(rules_file)
        Parser.__parse_tokens(tokens_file)

    @staticmethod
    def __parse_rules(rules_file):
        """Parse rules in grammar file and put them in `code_objs`."""
        lines = ''
        with open(rules_file, 'r') as f:
            lines = f.readlines()
            lines = ''.join(lines).split()

        idx = 0
        while idx < len(lines):
            rule_name = lines[idx]
            rule = Rule(rule_name)
            idx += 1
            while lines[idx] != '---':
                idx += 1
                obj_list = []
                while lines[idx] not in ['|', '---']:
                    obj_list.append(lines[idx])
                    idx += 1
                rule.add_choice(obj_list)

            Global.code_objs[rule_name] = rule
            idx += 1

    @staticmethod
    def __parse_tokens(tokens_file):
        with open(tokens_file, 'r') as f:
            for line in f.readlines():
                token_name = line.split()[0]
                Global.code_objs[token_name] = Token(token_name)

    def generate_parse_tree(self, tokens):
        Global.token_stream[:] = tokens
        Global.cursor = 0
        tree_root = Node('program')
        print(Global.code_objs['decl_list'].check(tree_root))
        print(RenderTree(tree_root))
        DotExporter(tree_root).to_picture('../parse_tree.png')
