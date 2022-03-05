from random import randint

guess = randint(0,1000)

print(f"PC guess is {guess}")
res = input(f"Is your number correct [<,>,=]: ")

while res != "=":
  res = input(f"Is your number correct [<,>,=]: ")
  if(res == "<"):
    newGuess = randint(0, guess)
  elif(res == ">"):
    newGuess = randint(guess, guess * 2)
  guess = newGuess
  print(f"New PC guess is {newGuess}")

print("PC GUESSED CORRECTLY!!!")