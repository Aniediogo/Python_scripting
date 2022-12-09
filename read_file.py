#you can use python to create a new file 'w'
# ad content to an existing file 'a'
# and read a file 'r'

#usually, to work with a file, you first have to name the file through a variable
# open the file and close it to save automatically afterwards.
#in between the open and close is where you
#work on the file, either to write to the file or to append, read.

#eg
file = open('new_file.txt', 'w' )

file.close()  #observer that when you run this, the process ends with zero without any other output. this shows that the file has been created.

#to check if file is in read mode after you have declared it to a write mode
file = open('new_file.txt', 'w' )
print(file.mode)
file.close()

file = open('new_file.txt', 'w' )
print(file.readable()) # the output will be false since the file is not in read mode
file.close()

file = open('new_file.txt', 'w' )
print(file.writable()) #the output is true since the file is in write mode
file.close()

#to add content to our file
file = open('new_file.txt', 'w' )
file.write("This is what i just wrote")
file.close()

#to add more contents to the file
file = open('new_file.txt', 'w' )
file.write("This is what i just wrote\n")
file.write("This is another content")
file.write("\nThis is the last line")
file.close()

#note, when you create a file in write mode, even if the file name already exists, python will recreate the file with the same name

#nstead of duplicating the file.write in different lines, you can write it in a straigth line
#but you have to put the items in a list either in a variable or within the clause

#the example below will is for variable
va_ri_able = ["This is my new line\n", "You can see that this write mode is working\n", "keep learning python, it will help you"]
file = open('new_fille.txt', 'w' )
file.writelines(va_ri_able)
file.close()

#it can still be written using a for loop

#to do this, create a variable with a list, create(open) a new file and set it to write mode

my_content = ["This is my python", "I love python", "Python is great"]
example = open("another_var.txt", "w")
for each in my_content:
    example.write(each + "\n")
example.close()

#another example, since we already have our file with content as in the example above but we only want to add just a little more data to it without ruining the initial one

my_content = ["This is my python project", "I really likepython", "Python is lovely"]
example = open("another_var.txt", "a")
for each in my_content:
    example.write(each + "\n")
example.close()
#if you run this script, it will be clear that another_var.txt was edited.
#also note, in read, write and append, if you do not close your script, your file may currupt

#read file
read_file = open("another_var.txt", "r") #to display the content of the file in your read,
print(read_file.read())
read_file.close()

#to read the content of the file in a line by line
read_file = open("another_var.txt", "r")
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
print(read_file.readline())
read_file.close()


