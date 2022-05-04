from player import Player

class Human(Player):
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.winned = []
    def action(self, state):
        print("Your cards are: ")
        for i  in range (len(state["hand"])):
            print(state["hand"][i])
        print("Cards on table:")
        for x in range(len(state["table"])):
            print(state["table"][x])
        if(len(state["winned_cards"]) > 0):
            print("Your winned cards:")
            for w in range(len(state["winned_cards"])):
                print(state["winned_cards"][w], end=" ")
        if(len(state["opponent_winned"]) > 0):
            print("Your opponent winned cards:")    
            for l in range(len(state["opponent_winned"])):
                print(state["opponent_winned"][l], end=" ")
        idx = int(input("Pick card: [0-2] "))
        while(idx > len(state["hand"]) or idx < 0):
            idx = int(input("Pick card: [0-2] "))
        
        return idx
