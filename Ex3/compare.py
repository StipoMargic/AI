import briskula


if __name__ == "__main__":
    p1 = briskula.BriskulaPlayer("agent1")
    p2 =  briskula.BriskulaPlayer("agent2")

    i = 0
    while(i < 100):
      briskula1 = briskula.Briskula(p1, p2)
      briskula1.play_game()
      rez = briskula1.rez()
      if rez == 1:
        print("Win" + p1.name)
      elif rez == 2:
        print("Win" + p2.name)
      else:
        print("Tie")
      i += 1

    while(i < 200):
      briskula1 = briskula.Briskula(p2, p1)
      briskula1.play_game()
      rez = briskula1.rez()
      if rez == 1:
        print("Win" + p1.name)
      elif rez == 2:
        print("Win" + p2.name)
      else:
        print("Tie")
      i += 1
    