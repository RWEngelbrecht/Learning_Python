
write_file = open("getting_started/work_with_files/write_test.txt", "r+")

lines = write_file.readlines()
append = "this is line too the return with a vengeance"

# append differently depending if last line has \n or not
if "\n" in lines[len(lines)-1]:
    write_file.write(append)
else:
    write_file.write("\n"+append)

write_file.close()

write_file = open("getting_started/work_with_files/write_test1.txt", "w")  #open creates new file if doesn't exist

write_file.write("Overwrite file with this line")

write_file.close()