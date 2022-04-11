import briskula
import player
import cards


if __name__ == "__main__":
    p1 = player.Player("agent1")
    p2 = player.Player("agent2")

    i = 0
    while(i < 2):
      deck = cards.Deck()
      briskula1 = briskula.Briskula(p1, p2, deck, {})
        
      briskula1.play_game()
      i += 1

    while(i < 4):
      deck = cards.Deck()
      briskula1 = briskula.Briskula(p2, p1, deck, {})
      
      briskula1.play_game()
      i += 1
    