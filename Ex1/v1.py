results = []

for x in range(100, -100, -1):
  for y in range (100, -100, -1):
    for z in range(100, -100, -1):
      if (y + x != 0 and z + x != 0 and z + y != 0):
        equation = z / (y + x)  + y / (z +x) + x / (z + y)
        if(equation == 4):
          results.append((x,y,z))


print(results)