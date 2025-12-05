list1 = [1, 5, 6, 7, 9, 10]
list2 = [2, 8, 3, 6, 9, 12]

print("First line: ", list1)
print("second line: ", list2)

newlist = []

for num in list1:
    if num %2 != 0:
       newlist.append(num)
for num in list2:
   if num % 2 == 0:
      newlist.append(num)

print("new list: ", newlist)