def areArrayEqual(a1, a2):
  for i in a1:
    if i not in a2:
      return False
    for i in a2:
      if i not in a1:
        return False
  return True
  
def numberToArray(num):
  return [i for i in str(num)]

num = 1224
num2 = 1234

num1array = numberToArray(num)
num2array = numberToArray(num2)


print(areArrayEqual(num1array, num2array))