# #Functions helps us not to repeat code

def name(namer, time):
    print(f"hi {len(namer)}, you are {time}mins late")
#
# ###################################################################

def three(var1, var2):
    if var1 > var2:
        print("highest number is", var1)
    else:
        print("highest number", var2)
three(34, 1)
#
# #########################################################################

name("Angela", 20)

amount1 = eval(input("How much? "))
amount2 = eval(input("How many? "))

def total():
    print(f"The total amount is {amount2 * amount1}")
total()



def minimum(first, second):
    if (first < second):
        print(first)
    else:
        print(second)


num1 = 10
num2 = 20

minimum(num1, num2)


    #RETURN
# To return something from a function, we must use the return keyword.
# Keep in mind that once the return statement is executed, the compiler ends the function.
# Any remaining lines of code after the return statement will not be executed.
#
# Let’s refactor the minimum() method to return the smaller value instead of printing it.
# Now, it’ll work just like the built-in min() function with two parameters:

def minimum(first, second):
    if (first < second):
        return first
    return second


num1 = 10
num2 = 20

result = minimum(num1, num2)  # Storing the value returned by the function
print(result)


string1 = "Learn Python {version} at {cname}".format(version = 3, cname = "Educative")
string2 = "Learn Python {0} at {1}".format(3, "Educative")
string3 = "Learn Python {} at {}".format(3, "Educative")

print(string1)
print(string2)
print(string3)

#Lambdas are defined using the lambda keyword. Since they return data, it is a good practice to assign them to a variable.
triple = lambda num : num * 3  # Assigning the lambda to a variable

print(triple(10))  # Calling the lambda and giving it a parameter

# Here’s a simple lambda that concatenates the first characters of three strings together:
concat_strings = lambda a, b, c: a[0] + b[0] + c[0]

print(concat_strings("World", "Wide", "Web"))

################################################################
my_func = lambda num: "High" if num > 50 else "Low"

print(my_func(60))

#Range Functions in python
#This is a built-in function in python used to generate only integers as a list by breaking down the number into component
#to achieve this, you will output the range with a list or tuple

var1 = range(20)
print(list(var1))

var1 = range(20)
print(tuple(var1))




