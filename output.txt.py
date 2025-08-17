
file1 = open("File3", "w")
writing_file = file1.write("Hello, python!")
print(writing_file)
file1.close()


file1 = open("File3", "r")
reading_file = file1.read()
print(reading_file)
file1.close()

file1 = open("File3", "a")
appending_file = file1.write(" Learning file handling in python.")
print(appending_file)
file1.close()

file1 = open("File3", "r")
reading_file = file1.read()
print(reading_file)
file1.close()


