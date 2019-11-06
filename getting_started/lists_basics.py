# BASIC LISTS

import math

friends = ["me", "myself", "I", "nobody"]
numbers = [42, 8, 15, 16, 23, 4]

print(friends[0])       # "me"
print(friends[-1])      # from end of index [pos [-1] == pos [3] "I"
print(friends[1:])      # from index 1 to end  ['myself', 'I', 'nobody']
print(friends[0:2])     # from index 0 to 2 non-inclusive of 2
friends[3] = "some guy"
print(friends[3])

print(sum(numbers[0:2]))    # 12

friends.extend(numbers)          # ['me', 'myself', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42]
friends.append("nobody")         # ['me', 'myself', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42, 'nobody']
friends.remove("me")              # ['myself', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42, 'nobody']
friends.insert(1, "Josef")       # ['myself', 'Josef', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42, 'nobody']
friends.pop()                    # ['myself', 'Josef', 'I', 'some guy', 4, 8, 15, 15, 16, 23, 42]
print("index pos of 'myself': "+str(friends.index("myself")))   # returns first index of param if in list
friends.insert(2, "myself")
print("amount of 'myself's: "+str(friends.count("myself")))
print(friends)
numbers.sort()
print(numbers)

randomShit = friends.copy()
print("\n")
print(randomShit)