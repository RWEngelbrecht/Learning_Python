import random

mm_in_km = 1 * 10**6
inch_in_nautMile = 72913.4

def get_file_extens(filename):
    ext = filename[filename.index(".") + 1:]
    return ext


def roll(die):
    try:
        throw = 0
        di = die.split("d")
        amnt = int(di[0])
        sides = int(di[1])
        for _ in range(0, amnt):            #can use single underscore for unused variable
            throw += random.randint(1, sides)
        return throw
    except:
        print("Invalid die. eg: 1d6")

