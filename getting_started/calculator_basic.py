
## BASIC CALCULATOR

def calculate(num1, num2, op):
	if op == "+":
		return num1 + num2
	elif op == "-":
		return num1 - num2
	elif op == "*":
		return num1 * num2
	elif op == "/":
		return num1 / num2
	elif op == "%":
		return num1 % num2


input_string = input("Welcome to ShittyPythonCalculator! Please input whatever:\n")

nb1, opr, nb2 = input_string.split()
answer = calculate(int(nb1), int(nb2), opr)

print(answer)