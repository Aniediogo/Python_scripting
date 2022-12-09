namer = input("what is your name?\n")
ager = input("What is your age?\n")
heighter = input("What is your height?\n")

a = eval(input("What is your number 2"))
b = eval(input("what is your number 1"))
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
elif b < a:
    print("b is less than a")
else:
    print("no not needed")

is_hot = False
is_cold = True

if is_hot:
    print("Grab some ice-cold")
elif is_cold:
    print("Grab some coffee")
else:
    print("Lovely day")
print("Enjoy your day regardless")

price = 1000000
has_good_credit = False

if has_good_credit:
    down_payment = price / 10
else:
    down_payment = price / 20
print(f"Down payment equals to: {down_payment}")

# Logical operators with And. This sets a rule that 2 conditions must be met before python can print our output

high_income = True
good_credit = False

if high_income and good_credit:
    print("You are eligible for loan")
else:
    print("Ineligible")

# OR logic: sets that one of the conditions must be met before python can print our statement

high_income = False
good_credit = False

if high_income and good_credit:
    print("You are eligible for loan")
elif high_income or good_credit:
    print("You are eligible for loan")
else:
    print("Ineligible")

# NOT logic: it converts any boolean given to the opposite

high_income = True
criminal_record = False

if high_income and not criminal_record:
    print("You are eligible for loan")
else:
    print("Ineligible")

# Nested if Statements#
#
# A cool feature of conditional statements is that we can nest them. This means that there could be an if statement inside another!
#
# Hence, we can use nesting to make complex conditions in our program:

num = 63

if num >= 0 and num <= 100:
    if num >= 50 and num <= 75:
        if num >= 60 and num <= 70:
            print("The number is in the 60-70 range")

# Creating and Editing Values #
#
# In a conditional statement, we can edit the values of our variables.
#
# Furthermore, we can create new variables.

num = 10
if num > 5:
    num = 20  # Assigning a new value to num
    new_num = num * 5  # Creating a new value called newNum

# The if condition ends, but the changes made inside it remain
print(num)
print(new_num)

light = "Red"

if light == "Green":
    print("Go")

elif light == "Yellow":
    print("Caution")

elif light == "Red":
    print("Stop")

else:
    print("Incorrect light signal")

#Multiple elif
num = 5

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")

# An important thing to keep in mind is that an if-elif-else or if-elif statement is not the same as multiple if statements. if statements act independently.
#
# If the conditions of two successive ifs are True, both statements will be executed.
#
# On the other hand, in if-elif-else, when a condition evaluates to True, the rest of the statement’s conditions are not evaluated.
#
# We’ll understand this better through an example:
num = 10

if num > 5:
    print("The number is greater than 5")

if num % 2 == 0:
    print("The number is even")

if not num % 2 == 0:
    print("The number is odd")

