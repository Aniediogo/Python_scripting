 #Python Operators
# #Operators are pillars of any language and without operators, you can not write a good python logic
# #Operators are like symbol which is resposible for the operation between two operands.
i = 1
j = 2
result = i + j
print(result)
# #in the code above, '+' is an operator while the variables 'i' and 'j' are called operands
#
# #Types of operators
# #Arithmetic operators
# #Identify Operators
# #Membershp Operators
# #Comparism Operators
# #Assignment Operators
# #logical operators
# #Bitwise operators
#
# #Arithmetic operators - they include - addition+, subtraction -, multiplication*, modulo %, division /, exponential **, floor division //
# #exponential is raised to power
a = 2
b = 6
ab = a**b
print(ab)

# #modulo is used to find the remained of a division
c = 7
t = 2
ct = c%t
print(ct)

# #floor division - this is lke divide but the opposite of modulo instead of printing the supposed remainder, it prints the
# #the the whole number
c = 7
t = 2
ct = c//t
print(ct)
#
'''
Assgnment operators - Assinging an expresssion to a variable using = (equal sign)
'''

val = 2+6
print(val)

# #Comparism operators are used to find the relationship  between two operands.
# #It deals with greater than signs and the output is true or false
a = 3
b = 6 > a
print(b)

# #Types of operators     > greater than, > less than, == equal, != Not equal to, >= greater than or equal to
# #<= less than all equal to

 print(4 <= 4)
# #this means that 4 maybe less than or may be equal to 4. anyone. It can also work with strings as well
 print( 3 <= 4 )
# #the answer is true cos 3 is less than 4
#
# print('a' > '-')
# #The operation above with string uses an underground numbering called ASCII code
print(ord('a'))
print(ord('b'))
print(ord('t'))
print(ord('z'))
print(ord('x'))
print(ord('#'))
print(ord('-'))
print(ord('%'))

# #you can also find the ASCII code for alphabest uses

print(chr(200))
print(chr(200))
#
# #Logical operators are used to combine multiple conditions. there are three tyes of logical operators in Python
# #there are 'and' 'or' 'not operators
#
# #For AND operator, The result returns True if both operators are the sameand False if they are not the same.
a = 3 > 1
b = 1 in [3,4,5]
c = a and b
print(c)

j = 5 < 1
k = 7 < 10
l = 8 > 12
p = j and k and l
print(p)

j = 5 > 1
k = 7 < 10
l = 8 < 12
p = j and k and l
print(p)

# #Instead of using AND in multiple places like we did above, We use ALL([]) and list the the values within the bracket
r = all([5>1,7>10,12<8,10>2])
print(r)

j = 5 > 1
k = 7 < 10
l = 8 < 12
print(all([j,k,l]))

# #Using OR operator The result outputs True if any one of the operands are true
j = 5 < 1
k = 7 < 10
l = 8 > 12
p = j or k or l
print(p)

j = 5 > 1
k = 7 < 10
l = 8 < 12
p = j or k or l
print(p)
#
# #Instead of using OR in multiple places like we did above, We use ANY([]) and list the the values within the bracket
r = any([5>1,7>10,12<8,10>2])
print(r)

j = 5 > 1
k = 7 < 10
l = 8 > 12
print(any([j,k,l]))
#
# #With the NOT operator, if the statment is true, the not will make it foalse and vice versa
q = 3 > 1
print(not q)
# #NOT of True ==> False, NOT of False ==> True
