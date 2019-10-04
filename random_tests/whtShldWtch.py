# What Should I Watch

import random

# def make_choice(possibilities):
#     secure_random = random.SystemRandom()
#     print(secure_random.choice(secure_random.choice(possibilities)))


def make_choices(possibilities, amount):
    secure_random = random.SystemRandom()
    option = possibilities[secure_random.randint(1, 3)]
    for i in range(0, amount):
        print(option[secure_random.randint(1, 3)])


shows = {
    1: "Mad Men",
    2: "Naruto",
    3: "American Vandal",
}

tutorials = {
    1: "Python",
    2: "CTF",
    3: "Networks",
}

misc = {
    1: "random youtube videos",
    2: "pr0n",
    3: "read a book, dammit",
}

options = {
    1: shows,
    2: tutorials,
    3: misc,
}

# make_choice(options)
make_choices(options, 5)
