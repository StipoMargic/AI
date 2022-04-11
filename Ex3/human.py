from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name

    def action(self, state):
        print("Your cards are: ")
        for i  in range (len(state["hand"])):
            print(state["hand"][i])
        idx = int(input("Pick card: [0-2] "))
        while(idx > len(state["hand"]) or idx < 0):
            idx = int(input("Pick card: [0-2] "))
        
        return idx
