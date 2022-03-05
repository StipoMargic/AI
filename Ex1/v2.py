def areArrayEqual(a1, a2):
  for i in a1:
    if i not in a2:
      return False
  return True
  
def numberToArray(num):
  return [i for i in str(num)]

num = 123456
num2 = 54321

num1array = numberToArray(num)
num2array = numberToArray(num2)


print(areArrayEqual(num1array, num2array))