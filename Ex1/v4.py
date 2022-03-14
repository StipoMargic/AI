highBorder = 1000
lowBorder = 0

res = input(f"Is your number correct [<,>,=]: ")

while res != "=":
  guess = (lowBorder + highBorder) // 2
  res = input(f"Is your number correct [<,>,=]: ")
  if(res == "<"):
    highBorder = guess
  elif(res == ">"):
    lowBorder = guess

  print(f"New PC guess is {guess}")

print("PC GUESSED CORRECTLY!!!")