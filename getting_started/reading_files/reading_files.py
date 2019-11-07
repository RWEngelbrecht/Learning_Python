#open("test.txt", "r")   #read
#open("test.txt", "w")   #write
#open("test.txt", "r+")  #r + w
#open("test.txt", "a")   #apend

test_file = open("reading_files/test.txt", "r")

try:
    print(test_file.readline())
except:
    print("nope")

test_file.close()