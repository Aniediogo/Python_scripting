#csv files are comma seperated values used to share files between a system ad a database.

#reading a csv file
#you have to open the file and specify the path

#since we do not have a csv file already to use for this, we can write a new one

write_a_new_csv_file = ['s/no,name,age,skill,job', '1,Mgbeke,30,security,no', '2,Nwafor,28,hr,yes', '3,Aku,26,cashier,yes,', '4,Akwaugo,21,student,no']
file_object = open('csv_file.csv', 'w')
for each_item in write_a_new_csv_file:
    file_object.write(each_item + '\n')
file_object.close()

#to read the csv file
#first, you have to import csv module and specify the name of the file together with the file path
import csv

csv_path = 'csv_file.csv' #the next step is to open the script
read_csv = open(csv_path, 'r') #assign a new variable to read_csv
read_content = read_csv.read()
read_csv.close()
print(read_content)

#another method to read the file line by line
csv_path = 'csv_file.csv'
read_csv = open(csv_path, 'r')
read_content = read_csv.readlines()
read_csv.close()
for each in read_content:
    print(each)

#csv files output in a tabular form. to show your output, in tabular or column form, this is where our csv module comes to play
csv_path = 'csv_file.csv'
read_csv = open(csv_path, 'r') #next line is to use the csv reader in cvs module to read the file in a csv format, to do that, we have to parse a new variable to the cvs reader
read_data = csv.reader(read_csv) #use a for loop to print the lines seperately
for each_line in read_data:
    print(each_line) #The output or result will be show seperate the values in our csv file with spaces to show their different values
read_csv.close()
