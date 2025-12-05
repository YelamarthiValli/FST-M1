numbers_tuple = tuple(map(int, input("Enter the numbers separated by space: ").split(" ")))

print("input is", numbers_tuple)

print("Elements that are divisible by 5: ")

for num in numbers_tuple:
    if (num % 5 == 0):
        print(num)