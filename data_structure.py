#Data structure  - this is used to hold multiple variables. Data structures are used to store a collection of data
#the collection of data may be a combination of strings, integers, floats, boleans
#there are four built-in data structures in python. they are - lists[], Tuple(), Dictionary{} with value pair and set{}

#List - Defining a list

my_list = []
my_list1 = [1,2,3,'python',2.8]

#In using lists, the first thing to do is to convert your list to boolean
#To covert the first list which is an empty list to boolean

my_list0 = []
print(bool(my_list0))

#the output is false since the boolean is empty

print(bool(my_list1))

#The output will return true there are values within the list
#working with a list

print(my_list1,type(my_list1))

#To print the indentation of lists, Python indentation starts from zero, you can count from zero to the number you want to print

print(my_list1[2])
print(my_list1[3])
print(my_list1[0])
print(my_list1[1])
print(my_list1[-1])

#Lets say there is a st ring in your list, and you want to get the index of the string as in 'y' in python [1,2,'python',2]
#First count from zero and find the number of python in the list, and find the index of that letter within python and print it this way
print(my_list1[3][1])
#The output will be y

my_list2 = [1,3,10,'Python is good', 2.3,0.1]
print(my_list2[3][7])
#The output will be 'i'

#if you want to print the list in another way with out using print(my_list2) you can do it this way
print(my_list2[:])

#if you want to print from tan index to the last value,count the number of index starting from zero
print(my_list2[2:])
#The output will count from '10' which is the index i indicated with '2'

#To print between an index to an index, count the number of the first index to the number where you want to stop

print(my_list2[2:5])

#If you want to change a value in your list, lets say I want to change the '1' in my_list1 above to '45'

my_list1[0] = 45
print(my_list1)
#The zero in the bracket is the index of '1' i wanted to change

#lists are mutable which means they can be changed or modified like we did above while strings are not

#you can also do a 'dir' of your list to find how you can edit it
print(dir(my_list1))

#Using index
my_list3 = [1,2,5,7,10,15,2,6,7,9,8,7]
print(my_list3.index(7))

#in the case of the list above where '7' appeared 2 or multiple times, have to call the number twice and seperate it
#with a coma
print(my_list3.index(7,7))

#count - Tis counts how many times a number appeared in the list
print(my_list3.count(7))

#Working with Tuple()
#Tuple are just like lists in parenthensis

my_tuple = ()
my_tuple1 = (1,2,3,4)
print(my_tuple)
print(my_tuple1)

#The first will print an empty tuple while the second will print a list


#you can also embed a list within a tuple and vice versa

my_tuple3 = (1,4,6,4,[3,6,8,1],8,10)
print(my_tuple3)

#Note that for the my_tuple3, the entire list in that bracket is seen by python as one element
print(my_tuple3[4])

#to find the index of the list within the tuple

print(my_tuple3[4][2])

#Tuples are immutable which means that you cannot modify the characters within it

print(len(my_tuple3))

#Note, that print(my_tuple3[4]) and print(my_tuple3.index(4)) will give you different results
print(my_tuple3[:6])
print(my_tuple3[2:6])
print(my_tuple3[:])
print(my_tuple3[0:])
print(my_tuple3[4:])

#Tuple can still be put in this way. the result below will output the data type to tuple
h = 5,6,7
print(h,type(h))

i = 5,
print(i,type(i))

#If you dont put coma, it will become an integer

#DICTIONARY{}        when writing dictionaries, you have to write it with a key and its value pair
my_dict = {}
print(my_dict,type(my_dict))

#to signify the value pair, use the colon:
#if the dictionary is a string, use quotation mark but if an integar or float, write them without quotation marks

my_dict1 = {'apple':'pawpaw','mango':'guava', 1:'one', 2: 'two'}
my_dict2 = {1:2,3:5,10:4,7:8}
print(my_dict1)
print(my_dict2)

#to print the value of a key in dictionary
print(my_dict1['apple'])
print(my_dict1.get('mango'))
#Note that the secind syntax will output 'none' instead of an error when you try to print a vlaue that is not in the dictionary
#note that the first syntax above will give an error instead of none
print(my_dict1.get('carbon'))

print(len(my_dict1))

#To add more keys to your dictionary
my_dict1['animal'] = 'goat'
print(my_dict1)

#you can modify keys by assigning a new value to an existing key pair
my_dict2[1] = 3
print(my_dict2)

my_dict1['animal'] = 80
print(my_dict1)

#To print all keys or values
print(my_dict1.keys())
print(my_dict1.values())

#to get the key and it value cicled as one items
print(my_dict2.items())
print(my_dict1.items())

#copy is used to assign a newname or value to your dictionary. the implicaton is that it assigns a new mwmory to your dictionary
f = my_dict1.copy()
print(f)

#to check and confirm the memory 'y' and 'my-dict1' stored their variable
print(id(f), id(my_dict1))

#to add 2 dictionaries together, use "update. Note that this operation does not delete the initial dictionar values.
my_dict1.update(my_dict2)
print(my_dict1)

#pop is used to remove a key value pair represenation
my_dict1.pop('apple')
print(my_dict1)

#to remove key value pair randomly, use 'popitem
my_dict2.popitem()
print(my_dict2)


#SET{} data structure
#set uses curly braces like dictionary but it lists its variables.
my_set = {1,2,3,5,6}
print(my_set,type(my_set))
print(my_set)

#to avoid outputting dict when you want to find the type of data structure with set
my_set1 = set({})
print(my_set1,type(my_set1))

