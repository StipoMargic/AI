import cards
import human
import player


class Briskula:
    power = {
        "1": 1,
        "3": 2,
        "13": 3,
        "12": 4,
        "11": 5
    }

    scores = {
        "1": 11,
        "3": 10,
        "13": 4,
        "12": 3,
        "11": 2
    }

    def __init__(self, p1, p2, deck, state):
        self.p1 = p1
        self.p2 = p2
        self.state = state
        self.state["table"] = deck


    def __str__(self):
        return "Cards: " + self.state["table"].cards,\
            "\nZog: " + str(self.state["zog"]), \
            "\Table: " + str(self.state["table"]), \
            "\nCards " + self.p1.name + ": " + str(self.state["hand"])

    
    def check_card(self, card):
        if(str(card.num) in self.scores):
            return self.scores[str(card.num)]
        
        return 0

    def check_card_strength(self, h_card, c_karta, zog):
        if(h_card.zog == zog.zog and c_karta.zog == zog.zog):
            if((str(h_card.num) not in self.power) and (str(c_karta.num) not in self.power)):
                if(h_card.num > c_karta.num):
                    return True
                else:
                    return False  
            elif((str(h_card.num) in self.power) and (str(c_karta.num) not in self.power)):
                return True
            else:
                return True
        elif(h_card.zog != zog.zog and c_karta.zog == zog.zog):
            return False
        elif(h_card.zog == zog.zog and c_karta.zog != zog.zog):
            return True
        elif(h_card.zog != zog.zog and c_karta.zog != zog.zog):
            if(h_card.zog == c_karta.zog):
                if(str(h_card.num) in self.power and str(c_karta.num) not in self.power):
                    return True
                elif(str(h_card.num) not in self.power and str(c_karta.num) not in self.power):
                    return h_card.num > c_karta.num
                elif(str(h_card.num) not in self.power and str(c_karta.num) in self.power):
                    return False
                if(self.power[str(h_card.num)] > self.power[str(c_karta.num)]):
                    return True
                else:
                    return False
            else:
                if(str(h_card.num) in self.power and str(c_karta.num) not in self.power):
                    return True
                elif(str(h_card.num) not in self.power and str(c_karta.num) in self.power):
                    return False
                else:
                    return h_card.num > c_karta.num
    

    def rez(self):
        c_score = 0
        h_score = 0

        for key, value in self.state.items():
            if(key == "winned_card"):
                for el in value:
                    h_score += self.check_card(el)
                if(h_score > 60):
                    print(self.p1.name, " have ", h_score, " score")
                    print(self.p2.name, " have ", c_score, " score")
                    return 1
            if(key == "opponent_winned"):
                for el in value:
                    c_score +=  self.check_card(el)
                if(c_score > 60):
                    print(self.p2.name, " have ", c_score, " score")
                    print(self.p1.name, " have ", h_score, " score")
                    return 2 

        print(self.p1.name, " have ", h_score)
        print(self.p2.name, " have ", c_score)
        return 0


    def statefn(self):
        hand_len = len(self.state["hand"])
        if(len(self.state["table"].cards) > 0):
            while(hand_len < 3):
                card = self.state["table"].peskaj()
                self.state["hand"].append(card)
                hand_len += 1
                
        return self.state


    def play_game(self):
        self.state["hand"] = []
        self.state["winned_card"] = []
        self.state["opponent_winned"] = []
        self.state["zog"] = self.state["table"].peskaj()
        self.state.update({"table": self.state["table"]})
        self.state["table"].add(self.state["zog"])

        while(len(self.state["table"].cards)):
            self.state = self.statefn()
            h_card, c_karta = self.play_hand()
            peska = []
            peska.append(h_card)
            peska.append(c_karta)
            if(self.check_card_strength(h_card, c_karta, self.state["zog"])):
                self.state["winned_card"].extend(peska)
            else:
                self.state["opponent_winned"].extend(peska)


        if(len(self.state["hand"]) > 0):
            h_card, c_karta = self.play_hand()
            if(self.check_card_strength(h_card, c_karta, self.state["zog"])):
                peska = []
                peska.append(h_card)
                peska.append(c_karta)
                self.state["winned_card"].extend(peska)
            else:
                peska = []
                peska.append(h_card)
                peska.append(c_karta)
                self.state["opponent_winned"].extend(peska)

        p1 = self.rez()

        if(p1 == 1):
            print(self.p1.name, "WON")
        elif(p1 == 2):
            print(self.p2.name, "WON")
        elif(p1 == 0):
            print("TIED")


    def play_hand(self):
        h_idx = self.p1.action(self.state)
        h_card = self.state["hand"].pop(h_idx)
        c_idx = self.p2.action(self.state)
        self.state = self.statefn()


        c_card = self.state["hand"].pop(c_idx)

        return h_card, c_card

if __name__ == "__main__":
    p1 = human.Human("p1")
    p2 = player.Player("p2")

    num_games = 5

    while(num_games > 0):
        deck = cards.Deck()
        briskula = Briskula(p1, p2, deck, {})
        briskula.play_game()
        num_games -= 1
        print(num_games)