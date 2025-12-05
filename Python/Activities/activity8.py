numbers = input("Enter a sequence of space separated values: ").split(" ")

numList = numbers

print("Given list is ", numList)

firstElement = numList[0]
lastElement = numList[-1]

if (firstElement == lastElement):
  print("Is first and last number in the input list is same : True")

else:
  print("Is first and last number in the input list is same : False")
