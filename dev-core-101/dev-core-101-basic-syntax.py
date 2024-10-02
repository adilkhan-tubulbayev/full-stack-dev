#mini calculator

num1, num2 = map(int, input("Input 2 numbers: ").split())
choice = input("What we need to do? '+','-','*' or '/' ? ")

if choice == "+": #addition
	print(f"Addition equals {num1 + num2}")
elif choice == "-": #substraction
	print(f"Substraction equals {num1 - num2}")
elif choice == "*": #multiplication
	print(f"Multiplication equals  {num1 * num2}")
elif choice == "/": #division
	print(f"Division equals {num1 / num2}")