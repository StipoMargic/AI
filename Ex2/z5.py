i = int(input("String len: "))

def str_con(s=""):
  if(len(s) ==  i):
    return [s]
  return str_con(s + "A") + str_con(s +"B")  + str_con(s + "C")
  
print(str_con())