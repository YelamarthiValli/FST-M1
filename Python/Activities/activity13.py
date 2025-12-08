def calculate_sum(numbers):
	sum = 0
	for number in numbers:
		sum = sum + number
	return sum
 

numList = [30, 90, 50, 40]

result = calculate_sum(numList)

print("The sum of all the elements is: " + str(result))
