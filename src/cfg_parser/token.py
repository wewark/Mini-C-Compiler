from .global_objs import Global
from anytree import Node


class Token():
    def __init__(self, name):
        self.name = name

    @staticmethod
    def skip_comments():
        while Global.cursor < len(Global.token_stream) and \
                Global.token_stream[Global.cursor].name in ['MULTI_COMMENT', 'SINGLE_COMMENT']:
            Global.cursor += 1

    def check(self, parent_node):
        if self.name == 'NULL':
            return True
        if Global.cursor >= len(Global.token_stream):
            return False
        if Global.token_stream[Global.cursor].name == self.name:
            Global.cursor += 1
            Token.skip_comments()
            Node('%s_%s' % (self.name, Global.cursor), parent=parent_node)
            return True
        return False
