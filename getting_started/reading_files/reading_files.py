## PLAYING WITH READING FROM FILES

#open("test.txt", "r")   #read
#open("test.txt", "w")   #write
#open("test.txt", "r+")  #r + w
#open("test.txt", "a")   #apend

test_file = open("getting_started/reading_files/test.txt", "r")

try:
    lines = test_file.readlines()     #read() returns all lines as single string. readlines() returns array. I mean list.
    print(lines)
    for line in lines:
        if "too" in line and "boogaloo" in line:
            print(line+" (the sequel's sequel)")
        elif "too" in line:
            print(line+" (the sequel)")
        else:
            print(line)
except:
    print("nope")

test_file.close()