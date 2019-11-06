## GUESS

import random

secret_words = ["one", "two", "three", "four"]

word = random.choice(secret_words)

guess = ""

tries = 0

while word != guess and tries < 3:
	guess = input("Enter your guess: ")
	tries += 1

if tries == 3:
	print("loser!")
else:
	print("you win!")