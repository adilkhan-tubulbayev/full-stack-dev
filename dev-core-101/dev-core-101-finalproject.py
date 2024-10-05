import math
# calculator

num1, num2 = map(int, input("Please, input 2 numbers: ").split())
choice = input("What we need to do? '+','-','*', '/' or ^ ??? ")

if choice == "+":  # addition
    print(f"Addition equals {num1 + num2}")
elif choice == "-":  # subtraction
    print(f"Subtraction equals {num1 - num2}")
elif choice == "*":  # multiplication
    print(f"Multiplication equals {num1 * num2}")
elif choice == "/":  # division
    if num2 != 0:
        print(f"Division equals {num1 / num2}")
    else:
        print("Can't divide by zero!") 
elif choice == "^":  # exponentiation
    print(f"{num1}^{num2} = {math.pow(num1, num2)}")
else:
    print("Invalid operation")
