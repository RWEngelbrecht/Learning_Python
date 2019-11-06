# IF STATEMENTS

is_true = True
something = 3
is_hax0r = False

if not is_true or something == 2:
	print("Wait, what?")
elif is_hax0r:
	print("lolz")
else:
	print("""
	Guess
	nothing
	is
	true""")

# comparisons


def max_value(num1, num2, num3):
	if num1 >= num2 and num1 >= num3:
		print("num1")
		return num1
	elif num2 >= num1 and num2 >= num3:
		print("num2")
		return num2
	else:
		print("num3")
		return num3


print(max_value(4, 8, 7))