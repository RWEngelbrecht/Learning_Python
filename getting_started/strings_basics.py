##STRINGS

thing = "suck a duck"
another_thing = "dummy"
experiment = "this is this is this is this"

print(thing.upper() + " " + another_thing)
print("thing.isupper(): ")
print(thing.isupper())
print(("thing.upper().isupper(): ").capitalize())
print(thing.upper().isupper())
print("(thing.upper() + " " + another_thing).isalnum():")
print((thing.upper() + " " + another_thing).isalnum())
print(thing[0])			#indexing in strings
print(thing.index("d", 3)) #return index of specified str
print(len(thing))		#string len
print(experiment.replace("is", "was", 1))
print(experiment, thing, another_thing.replace('-', ' '), end="\n\n\n")