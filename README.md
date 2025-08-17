# TASK-1-AND-TASK-2-Read-a-File-and-Handle-Errors-AND-Write-and-Append-Data-to-a-File

Task 1: Read a File and Handle Errors 

file1 = open("File 2", "r")
reading_file = file1.read()

print(reading_file)
file1.close()

Task 2: Write and Append Data to a File


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



