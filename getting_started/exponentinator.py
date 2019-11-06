
import math


def calc_exp(base, exp):
	ans = 1
	for i in range(exp):
		ans *= base
	return ans


prob = input("Enter what you want exponated (ie 2^2): ")

if prob.find("^"):
	base_exp = prob.split("^")

base_num = int(base_exp[0])
exp_num = int(base_exp[1])

print("using created function:	"+str(calc_exp(base_num, exp_num)))

print("""\

OR
	""")

print("using built-in math:	"+str(base_num**exp_num))
