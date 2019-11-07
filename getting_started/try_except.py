'''
like try/catch in php. tries to execute code, catches or excepts errors
'''
try:
    num = int(input("Enter a number: "))
    print(num)
except ValueError:
    print("invalid input")

try:
    print(10/0)
except ZeroDivisionError as err:
    print(err)