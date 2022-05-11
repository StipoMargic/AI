class Stick:
    def __init__(self, init_number=11):
        self.floor = init_number
        self.player = "1"


    def __str__(self):
        return "Number of sticks in floor: " + str(self.floor) + ", player " + self.player + " is playing"


    def change_player(self):
        if(self.player == "1"):
            self.player = "2"
        else:
            self.player = "2"


    def action(self, number):
        self.floor -= number
        self.change_player()

    
    def undo_action(self, number):
        self.floor += number
        self.change_player()


    def is_terminal(self):
        return  self.floor <= 2

if __name__ == "__main__":
    stick = Stick()
