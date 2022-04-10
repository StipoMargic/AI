from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name

    def action(self, state):
        print("Your cards are: ", str(state["hand"]))
        idx = int(input("Pick card: [0-2] "))
        while(idx > len(state["hand"]) or idx < 0):
            idx = int(input("Pick card: [0-2] "))
        
        for key, value in state.items():
            if(key == "hand"):
                card = value.pop(idx)
                return card
