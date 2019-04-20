from . import token_stream, code_objs
from rule import Rule


class Parser():
    def __init__(self, grammar_file, tokens):
        global token_stream
        token_stream = tokens
        Parser.__parse_grammar(grammar_file)
    
    @staticmethod
    def __parse_grammar(grammar_file):
        """Parse rules in grammar file and put them in `code_objs`."""
        lines = ''
        with open(grammar_file, 'r') as f:
            lines = f.readlines()
            lines = ''.join(lines).split()
        
        idx = 0
        while idx < len(lines):
            rule = Rule()
            idx += 1
            while lines[idx] != '---':
                idx += 1
                obj_list = []
                while lines[idx] not in ['|', '---']:
                    obj_list.append(lines[idx])
                    idx += 1
                rule.add_choice(obj_list)
            
            rule_name = lines[idx]
            code_objs[rule_name] = rule
            idx += 1



