#To replace the value of pages or data in the memory, swipping is used manipulate the data files

a=10
b=20
print(a,b)
a,b=b,a
#what happened here is that the value of a now goes to b  and the value of be has been reassigned to a
print("this is the value of a",a)
print("this is the value of b",b)

i = 5             # a whole number int type                  
f = 3.1415926      # a floating point number    Value of Pi          
string = "Python Course"    # a string Variable

print(i)
print(f)
print(string)

Concatenation = string + " " + string #here as you can see we add to strings together
print(Concatenation)

sum = f + f #sum of the float point numbers
print(sum)

'''
we have several variables (i,f,String) which are of different data types. Later in the program we create more variables (Concatenation, sum).
Variables can be defined anywhere in the program. Variable names can be one to n letters.
'''
t=38
d=67
c=59
x=90
print(t,d,c,x)
t,d,c,x=x,c,d,t
print(t,d,c,x)
