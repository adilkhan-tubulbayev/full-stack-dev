import random as rand

#from C to F
temp_celsius = int(input("Input temperature in Celcius: "))
temp_fahrenheit = temp_celsius * 1.8 + 32
print(f"Temperature in Fahrenheit: {temp_fahrenheit}F")

#guess the number
num = rand.randint(0, 10)
isGuessed = True
while (isGuessed):
	guess = int(input("Guess the number from 0 to 10: "))
	if guess < num:
		print("The number is greater than your guess")
	elif guess > num:
		print("The number is less than your guess")
	elif guess == num:
		isGuessed = False
		print("You guessed it!")

#factorial
num = int(input("Input the number: "))
factorial = 1

for i in range(1, num + 1):
		factorial *= i

print(f"Factorial of the {num} is {factorial}")
