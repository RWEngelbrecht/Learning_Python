##pig latin translator - only works for basic pl, not interested enough to make proper

p_latin = input("Give me a word in Pig latin: ")

first_index = p_latin.find("ay", len(p_latin)-3, len(p_latin))
first_letter = p_latin[first_index - 1]

print(first_letter+p_latin[:-3])
