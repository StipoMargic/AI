def predikat(i):
  if i > 0:
    return True
  return False

def count_iter(lst, function):
  sum = 0
  for element in lst:
    res = function(element)
    if res == True:
      sum += element

  return sum

def count_rec(lst, func, i=0):
  sum = 0
  if len(lst) == i:
    return sum
  res = func(lst[i])
  if res == True:
    sum += lst[i]
  return sum + count_rec(lst,func, i +1)

print(count_rec([1,2,-1,-2], predikat))
