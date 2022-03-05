from random import randint

def check(v1,  v2):
  if(v1 < v2):
    print("You guessed too low")
  else:
    print("You guessed to high!")


generatedNum = randint(0, 1000)

print(generatedNum)

val = int(input("Enter your value: "))
check(val, generatedNum)

while(val != generatedNum):
  val = int(input("Enter your value: "))
  check(val, generatedNum)

print(f"You guessed right number {generatedNum}")