#JSON - Javascript Object Notation is a data format used to represent structured data

#It is best used to transfer files from client to server or from server to web application

#Both JSON and XML are used for server-client transfer. where XML is majorly used for transfering complex data and JSON for simpler data
#in python, json format is represented in dictionary data type because of its key value pair structure while
#in json, it is known as object

#to read or convert a json file in python
#create a file with .json exension and set it to write  'w'

json_file = open('first_json_file.json', 'w')
json_file.write("this is my json file") #if the json content is a simple file, you can paste into the arguement on this line
json_file.close() #if not, open your json file in an editor and paste it within

#reading a json file
#the first thing to do is to import json module and specify the name of the file you want to read if you are in the same directory.
#if not, specify the file name with the path

import json

file_name = 'second_json_file.json'  #open the file in read mode
file_object = open(file_name, 'r') #to read the file in its json format
print(file_object.read())
file_object.close()

#To read a json file in python format
file_name = 'second_json_file.json'
file_object = open(file_name, 'r') #use json.load to parse the data
print(json.load(file_object)) #this loads the file object in a dict type
file_object.close()
print(type(file_object))

#to get a particular value from the from the json file
file_name = 'second_json_file.json'
file_object = open(file_name, 'r')
print(json.load(file_object).get('quiz'))
file_object.close()


#how to create a json file using python dictionary
#first is to create a python list and parse it through a variable
#secondly is to create a json file and open it in write mode

my_dict = {'name': 'Angela', 'skills':['python','DevOps','DevSecOps','Cybersecurity','Writing','Administration'], 'Ages': [12, 24, 26]}
required_file = 'pytho_to_json.json'
new_file = open(required_file, 'w') #use json dump to push the file from python to json with respect to the variable "new_file"
json.dump(my_dict, new_file, indent = 6) #the indentation is to make the file look appropirately like json file
new_file.close()
#note: you can indent to any number you choose


#To read the file we just created in json format
read_file = open('pytho_to_json.json', 'r')
print(read_file.read())
read_file.close()