#Exception is a way python handles runtime errors
#normally, python scripts terminates once it encounters an error without executing the script
#Two basic types of errors in python
# 1. syntax error - type of error we get as a result of poor usage of builtin python function
# 2. runtime errors - due to our run input or code

#try and except are two 2 python functions used in handling exception
#example

#print(5/0)
#this print code above will give the following errors

# Traceback (most recent call last):
#   File "/home/diogo/Desktop/script_tutorial/exception_handling.py", line 9, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero

#but to handle this eror suppose we do not know there is going to be an error, we use "try" and "except"
try:
    print(5/0) #this is a wrong division which is suppoed to show an error
except:
    print("There is an error") #in this except block, we have told python the error report we want printed out and also asked it to keep executing the code

#more examples
#lets say we want to read a file. we are not sure the file exists in our current directory. with try and except, python could try and look for
#the file in our currently directory and run it. but if the file is not there, instead of python to close our code with its own error, it will
#try and run the code and output our own error

try:
    file_object = open('read_text.txt', 'r')
    print(file_object.read())
    file_object.close()
except:
    print("file not found")

#another way to handle exceptions such that python outputs the error without stopping the code
try:
    file_object = open('read_text.txt', 'r')
    print(file_object.read())
    file_object.close()
except Exception as e:
    print(e)

#or
try:
    file_object = open('read_text.txt', 'r')
    print(file_object.read())
    file_object.close()
except Exception as e:
    print("This is an error:", e)

#types of runtime errors

# ZeroDivisonError
# FilenotFoundError
# ImportError
# IndexError
# ValueError
# TypeError
# NameError


#Error handling for known Exceptions

#xception handling for NameError
try:
    print(a)
except NameError:
    print("please parse a into a variable")

#exception for TypeError

try:
    print(5 + 'gel')
except TypeError:
    print("Type concatenation not compartible, 5 is an 'int' ")

#lets say you are not sure of the error type even after it has been specified like in the example above
try:
    print(5 + 'gel')
except ValueError:
    print("Type concatenation not compartible, 5 is an 'int' ")
except Exception as e: #this line will run the "except" line above and if it does not match, it will run  the "Exception" line
    print(e)

#you can also play with trying many exceptions in a block of code
try:
    print(5 + 'gel')
except NameError:
    print("Type concatenation not compartible, 5 is an 'int' ")
except ImportError:
    print("Thi is not an import case")
except FileExistsError:
    print("Not this type of error")
except FileNotFoundError:
    print("This is not it")
except IndexError:
    print("This is not an index")
except ZeroDivisionError:
    print("you are not dividing anything")
except Exception as e:
    print(e)

#another example
try:
    print("Checkout these errors")
    import cocoa #There is no module in python called cocoa. we are only trying out exception errors
    print("watch out") #this line will not exceute because of the error in the line above
except NameError:
    print("Type concatenation not compartible, 5 is an 'int' ")
except ImportError:
    print("Thi is not a python module")
except FileExistsError:
    print("Not this type of error")
except FileNotFoundError:
    print("This is not it")
except IndexError:
    print("This is not an index")
except ZeroDivisionError:
    print("you are not dividing anything")
except Exception as e:
    print(e)
finally:
    print("This line will always execute")

#when there is no error in the try block, we use "else" to excute the code
try:
    print('love ' + 'gel')
    a = 20 * 30
    print(a)
except NameError:
    print("Type concatenation not compartible, 5 is an 'int' ")
except ImportError:
    print("Thi is not an import case")
except FileExistsError:
    print("Not this type of error")
except FileNotFoundError:
    print("This is not it")
except IndexError:
    print("This is not an index")
except ZeroDivisionError:
    print("you are not dividing anything")
except Exception as e:
    print(e)
else:
    print('There is no error here')