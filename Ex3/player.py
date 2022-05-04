from random import randint


class Player:
    def __init__(self, name):
        self.name = name

    def action(self, state):
        if (len(state["hand"]) >= 1):
             return randint(0, len(state["hand"] ) - 1)
        return 0