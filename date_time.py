#datetime module is used to import date and time to scripts

import datetime
print(datetime.datetime.now()) #used to find out the current time

print(datetime.datetime.today())



print(datetime.datetime.now().year)
print(datetime.datetime.now().weekday())
print(datetime.datetime.now().month)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
print(datetime.datetime.now().microsecond)

#when you are writing python script using datetime module, you can visit this site  strftime.org to find the commands

#if you check the datetime module, we input datetime.datetime before our actual commands. when importing your dattetime module, import it this way


from datetime import datetime
print(datetime.now())

import datetime as x
print(x.datetime.now())

#to check for more functions with your datetime module
print(dir(datetime))

#python script to find all the files which are older than a certain number of days
