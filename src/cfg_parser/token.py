from . import cursor, token_stream


class Token():
    def __init__(self, name):
        self.name = name

    def check(self):
        global cursor
        global token_stream
        if self.name == 'NULL':
            return True
        if cursor[0] >= len(token_stream):
            return False
        if token_stream[cursor[0]].type == self.name:
            cursor[0] += 1
            return True
        return False
