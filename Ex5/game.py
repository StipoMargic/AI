from stick import Stick


def minimax(game):
    if game.is_terminal():
        if game.player == "1":
            return 1000, 0
        elif game.player == "2":
            return -1000, 0
        else:
            return 0, 0

    if game.player == "2":
        max_num = -1000
        best_action = 0
        for i in range(1, 3):
            game.action(i)
            v, _ = minimax(game)
            game.undo_action(i)
            if(v > max_num):
                max_num = v
                best_action = i
        return max_num, best_action
    else:
        min_num = 1000
        best_action = 0
        for i in range(1, 3):
            game.action(i)
            m, _ = minimax(game)
            game.undo_action(i)
            if(m < min_num):
                best_action = i
                min_num = m

        return min_num, best_action

def check(num):
    return num == 1 or num == 2


if __name__ == "__main__":
    game = Stick()

    while game.is_terminal() == False:
        if(game.player == "1"):
            num = int(input("Number of sticks: "))
            while not check(num):
                num = int(input("Number of sticks:  "))
            game.action(num)
            if(game.floor < num):
                break
            print(game)
        else:
            c_num, move = minimax(game)
            game.action(move)
            print(game)

    game.change_player()
    print("Winner is ", game.player)
