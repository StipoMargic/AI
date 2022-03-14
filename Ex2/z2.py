def is_in_list(n1, n2):
  if (len(n2) == 0):
    return True
  if(n1 == n2[0]):
    return True

  return is_in_list(n1, n2[1:])

def check_is_same(num1, num2):
  if(len(num1) == 0):
    return True
  if not is_in_list(num1[0], num2):
    return False
    
  return check_is_same(num1[1:], num2)


print(check_is_same("1224", "1234")  )