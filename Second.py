# #Conditional statement 'IF'. 'If' is called simple conditional statement. It is used to control the exectution of set of lines or block of code
#
a = input('what is your name? ')
if a == 'Angela':
    print('Welcome Angela, \nPlease make yourself comfortable')
    b = input('Are you with your Laptop? ')
    if b == 'yes':
        print("Thank you for coming with your laptop, Angela. \nLet's get started")
    else:
        print('Please go home!')
else:
    print('You are not Angela')

#ELIF   majorly used wen there are many conditions
ur_number = eval(input('What is your number? '))
b = eval(input('What is your second number? '))

if ur_number <= b:
    print('You are in order')
elif ur_number < b:
    print('You are in order')
elif ur_number == b:
    print('Your are in order')
else:
    print('Invalid number')