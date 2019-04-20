from src.parser import cursor, token_stream

class Token():
    def __init__(self, name):
        self.name = name
    
    def check(self):
        global cursor
        return token_stream[cursor] == self.name
