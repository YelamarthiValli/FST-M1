numbers = input("Enter a sequence of space separated values: ").split(" ")
 
sum = 0
for number in numbers:
  sum = sum + int(number)
 
print(sum)