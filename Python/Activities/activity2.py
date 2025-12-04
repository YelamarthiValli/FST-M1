number = int(input("Enter a number: "))
mod = number % 2
num = str(number)
if mod > 0:
    print("The number " + num + " is an odd number.")
else:
    print("The number " + num + " is an even number.")
