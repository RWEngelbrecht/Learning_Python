# FUNCTIONS

#What Should I Watch

import random


def make_choice(possibilities):
    secure_random = random.SystemRandom()
    print(secure_random.choice(secure_random.choice(possibilities)))


def make_choices(possibilities, amount):
    secure_random = random.SystemRandom()
    option = secure_random.choice(possibilities)
    print(", ".join(secure_random.sample(option, amount)))


shows = ["Mad Men", "Naruto", "American Vandal"]
tutorials = ["Python", "CTF", "Networks"]
misc = ["random youtube videos", "pr0n", "read a book, dammit"]
options = (shows, tutorials, misc)

# make_choice(options)
make_choices(options, 2)