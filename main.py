# name = True
# print(name,type(name))
#string formatting
a = 15
b = 10
c = "my name"
print(" {} {} {} ". format(a, b, c))

#to get the values of the variable in multiple lines
a = 15
b = 10
c = "my name"
print("{} \n{} \n{} ". format(a, b, c))

#it is possible to change the sequence of output as in the code above
a = 15
b = 10
c = "my name"
print("{} {} {} ". format(c, a, b))

#you can also print it this way
a = 15
b = 10
c = "my name"
print(f"{a} {b} {c}")

#you can also ad text description to it
a = 15
b = 10
c = "my name"
print(f"The 'a' value is: {a} \nThe 'y' value is: {b} \nThe 'c' is: {c}")

a = 15
b = 10
c = "my name"
my_required_output = f"The 'a' value is: {a} \nThe 'y' value is: {b} \nThe 'c' is: {c}"
print(my_required_output)

#dir outputs a lot of commands that you can add to your print function. Run the followig code to see them.
d = "mine"
print(dir(d))

#boolean operations python strings
my_strings = "Python"
print(my_strings.startswith('P'))

#join_center_zfill OPerations on strings
#this is usually done when you want to fromat your python text
#To do this, use the join() command after you have declared a variable

x = "Python"
print(' '.join(x))

x = "Python"
print('..'.join(x))

y = "Jesus"
print('*'.join(y))
#you can use any character that you want

d = "Home is good"
print(' '.join(d))

x = "Python"
print('\n'.join(x))

x = "Python"
print('\t'.join(x))

#centre(20)
#sometimes. you have some multiple strings and you want to print all strings at the centre of your terminal
#the number of indentation given will determine the center result
a = "Python is good"
b = "God is love"
c = "Greater me"
print(f"{a.center(30)}\n{b.center(20)}\n{c.center(30)}")

#zfill also mean zerofill
#this counts your letter and fills the remain characters with zero
my_str = "Python"
print(my_str.zfill(20))

my_str = "Python"
print(my_str.zfill(10))
#python substracts the number in your variable and autofills the remaing fill zeros


# strip and split in python
#the strip removes by default spaces that may have been mistakenly put in a variable
x = " Python  "
print(x)
#The command above will print and there will be no space at the begining of python. Lets add stripe and see
x = " Python  "
print(x.strip())

#Strip can also be used to remove characters at the starting or ending sides
x = "Python"
print(x.strip('P'))

x = "Python"
print(x.strip('n'))
#You can also use strip to remove the first or last words in a sentence
x = "Python script is easy"
print(x.strip('easy'))

x = "Python script is easy"
print(x.strip('Python'))

#strip can also remove words or character from both sides at once if they are the same word or character
x = "Python script is easy Python"
print(x.strip('Python'))

#If you want to remove the one at the right or left, use rstrip or lstrip
x = "Python script is easy Python"
print(x.lstrip('Python'))

# to use strip to remove characters sequentially
x = "Python script is easy"
print(x.strip('easy').strip('Python'))
#You can apply a combination of lstrip, strip, rstrip. any two of them together in a sequence like we did above

#split  - This is used to break words or sentences into different partitions and outputs it in a format called a list
x = "Python script is easy"
print(x.split())

#in split, you can remove from any part of the sentence. what this will do is to split the sentence into a list and the
#number of list will go according to how many times the word you removed appeared in the sentence.
x = "Python script is easy and it is very popular"
print(x.split('is'))
#from the output, we got 3 lists

#count, index and find operations
#count checks how many times a character or word is apearing in a given string
x = "Python is easy an is a popular language"
print(x.count('is'))

#index is the number of a particular character in a string as in 0,1,2,3
x = "Python is easy an is a popular language"
print(x.index('P'))

#if you dont want to count from the begining, you can manually check the number with your fingers and specify it with a coma
#you can also use this coma version to output characetrs especially when there are morethan one in a sentence or word
x = "python is easy an is a popular language"
print(x.index('p',0))

x = "Python is easy an is a popular language"
print(x.index('y',4))

x = "Python is easy an is a popular language"
print(x.index('p',10))

#find is also like index
x = "python is easy an is a popular language"
print(x.find('p',0))

x = "Python is easy an is a popular language"
print(x.find('y'))

x = "Python is easy an is a popular language"
print(x.find('p',10))

#You can use find to do word
x = "Python is easy an is a popular language"
print(x.find('Python'))

