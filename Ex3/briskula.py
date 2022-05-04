import cards
from human import Human
from player import Player

class Briskula:
    scores = {1: 11, 2: 0, 3: 10, 4: 0, 5: 0, 6: 0, 7: 0, 11: 2, 12: 3, 13: 4}
    power = {1: 13, 2: 4, 3: 12, 4: 5, 5: 6, 6: 7, 7: 8, 11: 9, 12: 10, 13: 11}
    
    turn = 1

    def __init__(self, player1, player2):
        self.p1 = player1
        self.p2 = player2
        self.deck = cards.Deck()
        self.briskula = self.deck.peskaj()
        self.deck.cards.append(self.briskula)
        self.cards_on_table = []
        for i in range(6):
            if i < 3:
                self.p1.hand.append(self.deck.peskaj())
            else:
                self.p2.hand.append(self.deck.peskaj())
        print("Briskula is:" + str(self.briskula))

    def check_card_strength(self, h_card, c_card, zog):
        if(h_card.zog == zog and c_card.zog == zog):
            if((str(h_card.num) not in self.power) and (str(c_card.num) not in self.power)):
                if(h_card.num > c_card.num):
                    return True
                else:
                    return False  
            elif((str(h_card.num) in self.power) and (str(c_card.num) not in self.power)):
                return True
            else:
                return True
        elif(h_card.zog != zog and c_card.zog == zog):
            return False
        elif(h_card.zog == zog and c_card.zog != zog):
            return True
        elif(h_card.zog != zog and c_card.zog != zog):
            if(h_card.zog == c_card.zog):
                if(str(h_card.num) in self.power and str(c_card.num) not in self.power):
                    return True
                elif(str(h_card.num) not in self.power and str(c_card.num) not in self.power):
                    return h_card.num > c_card.num
                elif(str(h_card.num) not in self.power and str(c_card.num) in self.power):
                    return False
                if(self.power[str(h_card.num)] > self.power[str(c_card.num)]):
                    return True
                else:
                    return False
            else:
                if(str(h_card.num) in self.power and str(c_card.num) not in self.power):
                    return True
                elif(str(h_card.num) not in self.power and str(c_card.num) in self.power):
                    return False
                else:
                    return h_card.num > c_card.num
    

    def rez(self):
        c_score = 0
        h_score = 0

        for card in self.p1.winned:
            h_score += self.scores[card.num]

        for card in self.p2.winned:
            c_score += self.scores[card.num]

        if h_score > c_score:
            return 1
        elif h_score < c_score:
            return 2
        else:
            return 0


    def statefn(self):
        if self.turn == 1:
            return {"briskula": self.briskula, "hand": self.p1.hand, "table": self.cards_on_table, "winned_cards": self.p1.winned, "opponent_winned": self.p2.winned}
            
        return {"briskula": self.briskula, "hand": self.p2.hand, "table": self.cards_on_table, "winned_cards": self.p2.winned, "opponent_winned": self.p1.winned}

    def play_game(self):
        while True:
            len_p1_hand = len(self.p1.hand)
            len_p2_hand = len(self.p2.hand)
            len_deck = len(self.deck.cards)
            if len_deck >= 2 and len_p1_hand > 0 and len_p2_hand > 0:
                self.play_hand()
                if self.turn == 1:
                    self.p1.hand.append(self.deck.peskaj())
                    self.p2.hand.append(self.deck.peskaj())
                elif self.turn == 2:
                    self.p2.hand.append(self.deck.peskaj())
                    self.p1.hand.append(self.deck.peskaj())
            elif len_deck == 0 and len_p1_hand > 0 and len_p2_hand > 0:
                self.play_hand()
            else: 
                break

    def play_hand(self):
        if self.turn == 1:
            h_idx = self.p1.action(self.statefn())
            h_card = self.p1.hand[h_idx]
            self.cards_on_table.append(h_card)
            self.p1.hand.pop(h_idx)

            c_idx = self.p2.action(self.statefn())
            c_card = self.p2.hand[c_idx]
            self.cards_on_table.append(c_card)
            self.p2.hand.pop(c_idx)

            winned = self.check_card_strength(h_card, c_card, self.briskula.zog)
            if winned:
                self.p1.winned.append(self.cards_on_table[0])
                self.p1.winned.append(self.cards_on_table[1])
                self.turn = 1
            else: 
                self.p2.winned.append(self.cards_on_table[0])
                self.p2.winned.append(self.cards_on_table[1])
                self.turn = 2

            self.cards_on_table.clear()
        else:
            h_idx = self.p2.action(self.statefn())
            h_card = self.p2.hand[h_idx]
            self.cards_on_table.append(h_card)
            self.p2.hand.pop(h_idx)

            c_idx = self.p1.action(self.statefn())
            c_card = self.p1.hand[c_idx]
            self.cards_on_table.append(c_card)
            self.p1.hand.pop(h_idx)

            winned = self.check_card_strength(h_card, c_card, self.briskula.zog)
            if winned:
                self.p2.winned.append(self.cards_on_table[0])
                self.p2.winned.append(self.cards_on_table[1])
                self.turn = 2
            else: 
                self.p1.winned.append(self.cards_on_table[0])
                self.p1.winned.append(self.cards_on_table[1])
                self.turn = 1

            self.cards_on_table.clear()

class BriskulaPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.hand = []
        self.winned = []

if __name__ == "__main__":
    p1 = Human("p1")
    p2 = BriskulaPlayer("p2")

    num_games = 5

    while(num_games > 0):
        briskula1 = Briskula(p1, p2)
        briskula1.play_game()
        rez = briskula1.rez()
        if rez == 1:
            print("Win" + p1.name)
        elif rez == 2:
            print("Win" + p2.name)
        else:
            print("Tie")
        num_games -= 1  
        print(rez)