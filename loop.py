import random

 random_number = random.randint(0,10)
 guess = -1

 while guess != random_number:
     user_guess = input("guess the number i have in mind between 0 and 10: ")
     converted_user_guess = int(user_guess)
     if random_number == converted_user_guess:
         print("Babe, it matched correctly")
     else:
         print("Try again!")



name = 'Achiever'
user_guess = ""

while name != user_guess:
    response = input("Enter your username: ")
    if response == name:
        print("Yes! access granted")
    else:
        print("wrong, try again")
        break

import random
#ask the user to enter any number & store in the user_guess  variable
user_guess = input("Guess the number i have in mind ")
# convert input user_guess to integer
convert_user_guess = int(user_guess)
#create random number
rando_number = random.randint(0,2)
#check if random number matches with user's guessed number
if rando_number == convert_user_guess:
    print("Babe! it matched correctly")
else:
    print("Try again")


