#This is a script that is instructe to clear the entire screen of the commandline

#first import the modules to use

import os
import platform

if platform.system() == "Windows":
   os.system("cls")  #where "cls is clear command for windows"
else:
   os.system("clear")  #where clear is for linux
