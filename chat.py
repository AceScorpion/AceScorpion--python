from .round import Round

class Chat(object):

    def __init__(self, r):
        self.content = []
        self.round = r

    def update_chat(self, msg):
        return self.content.append(msg)

    def __len(self):
        return len(self.content)

    def __str__(self):
        return "".join(self.content)

    def __repr__(self):
        return str(self)