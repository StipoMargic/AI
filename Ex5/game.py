from stick import Stick


def minimax(game):
    if(game.is_terminal()):
        if(game.player == "1"):
            return 1000
        else:
            return -1000

    if(game.player == "1"):
        max_num = 1000
        for i in range(1, 3):
            game.action(i)
            v = minimax(game)
            game.undo_action(v)
            if(v > max_num):
                max_num = v

        return max_num
    else:
        min_num = -1000
        for i in range(1, 3):
            game.action(i)
            m = minimax(game)
            game.undo_action(i)

            if(m < min_num):
                min_num = m

        return min_num

def check(num):
    return num == 1 or num == 2


if __name__ == "__main__":
    game = Stick()

    while(not game.is_terminal()):
        print(game.player)
        if(game.player == "1"):
            num = int(input("Number of sticks: "))
            while not check(num):
                num = int(input("Number of sticks:  "))
            game.action(num)
            if(game.floor < num):
                break
            print(game)
        else:
            c_num = minimax(game)
            if(game.floor < c_num):
                break
            game.action(c_num)
            print(game)
        game.change_player()

    print("Winner is ", game.player)
