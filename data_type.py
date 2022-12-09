#python function

no_of_hours = 24
name_of_time = "hours"

def calculate_all():
    print(f"20 days have {20 * no_of_hours} {name_of_time}")
    print("It is all good")

calculate_all()

#in any case where you want to print that function fir different days, instead of writing them manually, you can do it this way

no_of_hours = 24
name_of_time = "hours"

#assign a new variable to the function and when you want to call it, add the number in the bracket
def calculate_all(no_of_days):
    print(f"{no_of_days} days have {no_of_days * no_of_hours} hours")
    print("It is all good")

calculate_all(20)
calculate_all(36)
calculate_all(50)
calculate_all(80)

#lets say you do not the second prnt function to be the same with all the values. you want them to change per the value.
#you can do this by parsing another input in the function variable
#you can add multiple values anyhow you want, just seperate it with a coma like so

no_of_hours = 24
name_of_time = "hours"

#assign a new variable to the function and when you want to call it, add the number in the bracket
def calculate_all(no_of_days, custom_message, greetings):
    print(f"{no_of_days} days have {no_of_days * no_of_hours} {name_of_time}")
    print(custom_message)
    print(greetings)

calculate_all(30, "Hello", "Welcome")
calculate_all(36, "Hey", "Stay tight")
calculate_all(70, "Hi Love", "Thank You!")
calculate_all(80, "dearest", "Enjoy your stay")


#variable scope in function
#variable scope means where is that variable called in the function defined?
#it is defined globally if the variable is not within the function like we have in our number_of_days
#it is defined locally if it lies with the function like we have in the custom_message
#it is defined within the a function block
#if you define another function within this code, you can print the number of days but cannot call the custom_message
#try it and see if you will not get an error

no_of_hours = 24
name_of_time = "hours"

#assign a new variable to the function and when you want to call it, add the number in the bracket
def calculate_all(no_of_days):
    my_fuction_variable = "Lovely girl"
    print(f"{no_of_days} days have {no_of_days * no_of_hours} hours")
    print("It is all good")
    print(my_fuction_variable)

calculate_all(20)
calculate_all(36)
calculate_all(50)
calculate_all(80)

#input