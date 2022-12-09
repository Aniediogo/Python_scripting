name = "Angela"
age = 26
height = "6ft"
print(f"My name is {name}, I am {age}, My height is {height}")
print(name.upper())

my_name = "Achiever "
last_name = "Okereke"
print(my_name + " " + last_name)

fullname = 'my_name + " " + last_name'
print(fullname)

username = input("username")
pin = input("pin")

if username == "Angela" and len(pin) >= 4:
    print("Welcome Angela")
else:
    print("invalid user")

my_string = "Hello"
def exclamation(my_string):
    my_string = "!!" + my_string + "!!"
    return my_string


exclamation(my_string)
print(my_string)

string_list = ["Anakin", "Luke", "Rey", "Leia", "Vader"]
for s in string_list:
    if len(s) < 5:
        print(len(s))