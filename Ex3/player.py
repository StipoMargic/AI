from random import randint


class Player:
    def __init__(self, name):
        self.name = name

    def action(self, state):
        idx = randint(0, len(state["hand"] ) - 1)
        for key, value in state.items():
            if(key == "hand"):
                card = value[idx]
                value.pop(idx)
                return card
        

    