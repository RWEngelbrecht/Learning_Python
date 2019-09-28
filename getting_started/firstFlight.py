##STRINGS

# thing = "suck a duck"
# another_thing = "dumb-shit"
# experiment = "this is this is this is this"

# print(thing.upper() + " " + another_thing)
# print("thing.isupper(): ")
# print(thing.isupper())
# print(("thing.upper().isupper(): ").capitalize())
# print(thing.upper().isupper())
# print("(thing.upper() + " " + another_thing).isalnum():")
# print((thing.upper() + " " + another_thing).isalnum())
# print(thing[0])			#indexing in strings
# print(thing.index("d", 3)) #return index of specified str
# print(len(thing))		#string len
# print(experiment.replace("is", "was", 1))
# print(experiment, thing, another_thing.replace('-', ' '), end="\n\n\n")

# NUMBERS

# from math import * #sqrt, ceil, floor, etc

# my_num = 42
# num_str = "42"

# print(42)
# print(my_num)
# print("my new favourite number is " + str(my_num))
# print(round(42 - 42.4224 * (37 + 2) / 52 % 3))
# print(42 / int(num_str))

# BASIC INPUT

# name = input("Enter Name: ")
# age = input("Enter birth year: ")
# print("HELLO, " + name + "!\n" + "You are " + str(2019 - int(age)) + " years old.")

# BASIC CALCULATOR

# from math import sqrt
#
# num1 = input("Enter first num: ")
# num2 = input("Enter second num: ")
# res = float(num1) + float(num2)
# print(sqrt(int(res)))

# MAD LIBS

# colour = input("Enter colour: ")
# noun = input("Enter plural noun: ")
# expletive = input("Enter expletive: ")
#
# print("Roses are " + colour)
# print(noun + " are blue")
# print("This is actually a limerick")
# print("woop-dee " + expletive + " doo")

# BASIC LISTS

# from math import *
#
# friends = ["me", "myself", "I", "nobody"]
# numbers = [42, 8, 15, 16, 23, 4]
#
# print(friends[0])       # "me"
# print(friends[-1])      # from end of index [pos [-1] == pos [3] "I"
# print(friends[1:])      # from index 1 to end  ['myself', 'I', 'nobody']
# print(friends[0:2])     # from index 0 to 2 non-inclusive of 2
# friends[3] = "some guy"
# print(friends[3])
#
# print(sum(numbers[0:2]))    # 12
#
# friends.extend(numbers)          # ['me', 'myself', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42]
# friends.append("nobody")         # ['me', 'myself', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42, 'nobody']
# friends.remove("me")              # ['myself', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42, 'nobody']
# friends.insert(1, "Josef")       # ['myself', 'Josef', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42, 'nobody']
# friends.pop()                    # ['myself', 'Josef', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42]
# print("index pos of 'myself': "+str(friends.index("myself")))   # returns first index of param if in list
# friends.insert(2, "myself")
# print("amount of 'myself's: "+str(friends.count("myself")))
# print(friends)
# numbers.sort()
# print(numbers)
#
# randomShit = friends.copy()
# print("\n")
# print(randomShit)

# TUPLE  #like lists, can't be changed (i.e. immutable)

# coordinates = [(4, 5), (5, 5), (4, 3)]
#
# print(coordinates[0])

# print("print"
#       "this"
#       "like"
#       "this")
# print("""\
# Usage: thing [options]
#     -h
#     -H hostname
# """)
#
# print("na" * 50 + "\n"
#      + "na" * 80 + "\n"
#     + "na" * 700 + "\n"
#       + "BATMAN!")
#
# print("\n"+str(len(coordinates)))

# FUNCTIONS

# What Should I Watch

# import random
#
#
# def make_choice(possibilities):
#     secure_random = random.SystemRandom()
#     print(secure_random.choice(secure_random.choice(possibilities)))
#
#
# def make_choices(possibilities, amount):
#     secure_random = random.SystemRandom()
#     option = secure_random.choice(possibilities)
#     print(", ".join(secure_random.sample(option, amount)))
#
#
# shows = ["Mad Men", "Naruto", "American Vandal"]
# tutorials = ["Python", "CTF", "Networks"]
# misc = ["random youtube videos", "pr0n", "read a book, dammit"]
# options = (shows, tutorials, misc)
#
# # make_choice(options)
# make_choices(options, 2)

# RETURN STATEMENTS

#
# def cube(num):
# 	return num * num * num
#
#
# result = cube(3)
# print(result)
#

# IF STATEMENTS

# is_true = True
# something = 3
# is_hax0r = False
#
# if not is_true or something == 2:
# 	print("Wait, what?")
# elif is_hax0r:
# 	print("lolz")
# else:
# 	print("""
# 	Guess
# 	nothing
# 	is
# 	true""")

# comparisons


# def max_value(num1, num2, num3):
# 	if num1 >= num2 and num1 >= num3:
# 		print("num1")
# 		return num1
# 	elif num2 >= num1 and num2 >= num3:
# 		print("num2")
# 		return num2
# 	else:
# 		print("num3")
# 		return num3
#
#
# print(max_value(4, 7, 7))

# def calculate(num1, num2, op):
# 	if op == "+":
# 		return num1 + num2
# 	elif op == "-":
# 		return num1 - num2
# 	elif op == "*":
# 		return num1 * num2
# 	elif op == "/":
# 		return num1 / num2
# 	elif op == "%":
# 		return num1 % num2
#
#
# print()
#
# input_string = input("Welcome to ShittyPythonCalculator! Please input whatever:\n")
#
# nb1, opr, nb2 = input_string.split()
# answer = calculate(int(nb1), int(nb2), opr)
#
# # arr = input_string.split()
# # answer = calculate(int(arr[1]))
#
# print(answer)
#
# # answer = calculate(num1, num2, op)

