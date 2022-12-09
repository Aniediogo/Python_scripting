#OS Module enables scripts interact with the operating system from the server-side

#This module is used to interact with the system to automate tasks like, changing directory, removing directory, identifying current directory, etc.

import os
print(os.sep) # the seperator is / that seperates different paths in any operating system. see example of path in the name of this file below

print("/home/diogo/Desktop/script_tutorial/venv/bin/python /home/diogo/Desktop/script_tutorial/os_module.py") #in case of Windows Os, use 2 slashes (//)

#To find out your current working directory, use os.getcwd
print(os.getcwd()) #getcwd is a combination of cd and pwd

#you can parse the os.getcwd and other OS parameters within a vairiable
get = os.getcwd()
print(get)

#To change a directory in the commandline
print(os.chdir("/home/diogo/Desktop/"))

#To list directory
print(os.listdir())

print(os.getcwd())

#To create a directory
# print(os.mkdir("New_Directory"))
# print(os.listdir())

# #To create a folder recursively into different folders
# print(os.mkdir("Gelia, girla, ferlia"))
# print(os.chdir("/home/diogo/Desktop/Gelia/"))
#
# print(os.listdir())

#To remove path
#print(os.remove()) #Copy the path and paste it into the remove bracket

#To remove directory
#print(os.rmdir()) #Specify the name of the directory within the bracket

#To know your enviroment where you are working on
print(os.environ)

#To get the userid
print(os.getuid())

#To get the group id
print(os.getgid())

#to get the process id
print(os.getpid())

#To find/see more you can do with your OS module
print(dir(os))

#OS.path module is used to work on path
print(os.path)
print(os.path.sep)


#OS.system() - The purpose of this module is to execute the operating system commands
#with this, you can parse normal operating system commands in a function

print(os.system("pwd"))

#Finding path using os.walk() - this path outputs directory in form of an id
path = "/home/diogo/Desktop/script_tutorial/venv/bin/python /home/diogo/Desktop/script_tutorial/os_module.py"
print(os.walk(path))

