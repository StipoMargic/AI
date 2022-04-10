from random import shuffle

class Card:
    card_with_pic = { 1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 11: "J", 12: "Q", 13: "K" }
    
    def __init__(self, num, zog):
        self.num = num
        self.zog = zog
    
    def __str__(self):
        return "[" +    Card.card_with_pic[self.num] + self.zog + "]"


class Cards:
    def __init__(self, cards):
        self.cards = cards
        
    def __str__(self):
        return " ".join(str(k) for k in self.cards)
    
    def add(self, k):
        self.cards += [ k ]
        
    def pullout(self, i):
        k, self.cards = self.cards[i], self.cards[:i] + self.cards[i+1:]
        return k


class Deck(Cards):
    def __init__(self):
        super().__init__([ Card(b, z) for b in [ 1, 2, 3, 4, 5, 6, 7, 11, 12, 13 ] for z in [ "D", "K", "S", "B" ] ])
        shuffle(self.cards)

    def peskaj(self):
        return self.pullout(0)    

    
deck = Deck()

    