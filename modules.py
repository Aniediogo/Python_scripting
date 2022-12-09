# A module is a file containing Pyhton deefinitions and statements, functions, classes and variables.
# The advantage of modules is that it is resuable.

# Let's say you have a variable in a previous script that you need to use in a new script, you have to import it.
#Eg. if the variable is my_var = Egg.
#The name of the script is Script.py
#in th new script, you have to import it
#import my_var
#If you need to use the variable,
#print(script.my_var)


#python has various default modules that you can import and use

#import math

# print(math.pi)
# print(math.pow(3.5))

#To find out all the modules in your python, go to the command line and type Python3
#When it opens, type help("module")

#Types of modules
#1. Default modules
#2. third-party modules

#use pip install to install thirtparty modules

# another way To install default module

from math import *
print(pi)
print(pow(2,5))

#The * symbol calls everything within the maths modules instead of importing the math itself

#you can choose to import the exact syntax within the module instead of importing all of them
from math import pi, pow

print(pow(5,9))

#You can change the name of your module such that you will call the new name

import math as M
print(M.pow(2,2))

import platform as y
print(y.system())

#if you want to import different modules, you can choose to import them seperately in diffrent lines or import them together using coma to seperate them
import os, platform, math

#or

import os
import math
import platform


#Platform modules is used to access underlying platform's data such as hardware, operating system, and interpreter version info
#How to list all functions and variables in a module. EG platform module
print(dir(platform))

print(f"This is a {platform.system()} OS")
print(f"My python version is {platform.python_version()}")
print(platform.release())
print(platform.architecture())
print(platform.machine())
print(platform.platform())


#getpass mosule is used to prompt the prompt teh user for a password without echoing. It provides a secure way to handle password prompt
#where programs interact with the user via the terminal

#getuser is used to display the login name of the user. This function checks the enironment login-name, user, Lname, username and
#returns the value of the first non-empty string

import getpass
print(getpass.getuser())

#check pyscript.py for getpass and getuser example

#sys module provides functions and variables used to wmanipulate python runtime environment

#sys.argv   T:his module returns a list of commandline arguement passed to a python script. It captures inside your script the
#values paased in the command line. check pyscript.py

import sys
print(sys.argv)
#Note that in your commandline arguement, if you want to print the first or second or any letter passed in the arguement,
#put it in a list
import sys
print(sys.argv)
