# #loops are used to execute a bloc of code many times
# #Types of loops - While loop & for loop
# #FOR LOOP
# #For loop is useful to repeat each block of code multiple times over a sequence which could be lists[], turple(), or string""
# # given this example:
# for each_item in [3, 4, 6]:
#     print(each_item) #This is called an iteration. it simply tells python to run the items in this list one at a time a time.
#
# #It is still possicle to substitiute the value in the list with another value as would be provided in the print. Eg
#
# for each_item in [3, 4, 6]:
#     print("This is my home")
#
# #another example using turple
#
# for x in (3, 4, 6):
#     print("__________________")
#     print("God is the greatest")
#     print("**********")
#
# #another example using string
# for this_string in "Python":
#     print("hi")  #what will happen in this string is that python will exectute this line of code as many times as the number of letters in the string
#
# #if you want to print the exact character in the list or turple or string together with the item or variable specified in the print,
# for characters in "Python":
#     print("hi", characters,) #You can add more items in the print per your choice
#
# #a script to sieve out even numbers in a list
# numbers = [2, 5, 8, 7, 6, 12, 14, 17, 68, 30, 55]
# for even_numbers in numbers:
#     remainder = even_numbers % 2 #what this means is that in even numbers, divisions does not output any remainders
#     if remainder == 0: #we are trying to be sure that if any of those numbers in our list does not have any remainder before we can ascertain
#         print(f"This number, {even_numbers} is an even number")
#     else:
#         print(f"this number, {even_numbers} is an odd number")
# print("Loop execution is successful")
#
# #For loop example to return but an input and items in a loop
#
# take_the_input = input("What string do you want?")
# variable = "would win"
# for each_string in take_the_input:
#     print(f"{each_string} --><-- {take_the_input} --><-- {variable}")
#
# #if you want to modify the script above to have an incremental number as per the number of characters in the string or list provided in the vairable
#
# take_the_input = input("What string do you want? ")
# variable = "would win"
# number = 1
# for each_string in take_the_input:
#     number = number + 2  # You can add the numbers or multiply as you want
#     print(f"{each_string} --><-- {take_the_input} --><-- {variable} {number}")
# #in line 54, the variable "number" is passed into a variable "number" to enable python perform the code incrementally but the variable changes, the number will remain constant
# #watch
# take_the_input = input("What string do you want? ")
# variable = "would win"
# number = 1
# for each_string in take_the_input:
#     incremental = number + 2  # You can add the numbers or multiply as you want
#     print(f"{each_string} --><-- {take_the_input} --><-- {variable} {number}")


#While lopp is used to execute a bloc of code repeatedly as long as a block of code is true
#example
import time
while False: #if set to true, the code will keep ruuning nonstop
    print("Let love lead")

while False: #if you set this condition to True, this block of code will iterate to an infinite number of time
    print("Logs failed")
    print("exit")
    time.sleep(3)

value = 4
while False: #if set to true, the code will run unending
    value = value + 2365
    print(value)

# you can set your while loop to run in condition such that when that condition is met, the loop will stop
#example: using this example below

# value = 9
# while value <= 10000:
#     value = value + 450
#     print(value)

#Another example
maggi = 2 #first, we are assigning maggi to a number 2
while maggi <= 10: #again, we want maggi to run but not exceed 10 times
    maggi = maggi + 1 #we want to increase the output of maggi by 1. meaning that 2+1+1+1+1+1+1+1
    print("hello maggi") #if "hello maggi" were to be an integer, the output would have been incremental, hence the output came out 9 times

#while loop is also used when we do not know beforehand the number of times a code will iterate

#Loop control statement - used to control the iteration part of the loop. the commands used for control is Break and Continue
#break is used to stop the iteration of your loop. EG:

for each in [3,2,92,849,3,"shj"]: #here, we have given python a list of the loop we want to run
    print(each) #python is supposed to print the first item on the list, go back & print another item, then print another item until the last
    break #with this break, python will stop after it as printed the first item on the list and then go out of this block of code to print the next thing
print("loop broken")

#if we have a list like in the example above, but we want to print some of the values in the list but not all
for angel in [2, "god", 5, 3, 6, 2, "bin", 7, 89, 6, 9]:
    print(angel)
    if angel == 89: #here, we ask the loop to execute the first item, second until the 7th which happens to be 7 and break out of the block
        break
print("loop successfully broken")