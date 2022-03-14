def merge(list1, list2):
    if list1 == [] and list2 == []:
       return list1
    if list1 != [] and list2 == []:
       return  list1
    if list1 == [] and list2 != []:
       return list2
    if list1 != [] and list2 != []:
       if list1[0] <= list2[0]:
          return [list1[0]] +  merge(list1[1:], list2)
       if list1[0] > list2[0]:
          return [list2[0]] + merge(list1, list2[1:])

print(merge([1,2,4], [-2,3,8]))