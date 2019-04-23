from .global_objs import Global


class Token():
    def __init__(self, name):
        self.name = name

    def check(self):
        if self.name == 'NULL':
            return True
        if Global.cursor >= len(Global.token_stream):
            return False
        if Global.token_stream[Global.cursor].type == self.name:
            Global.cursor += 1
            return True
        return False
