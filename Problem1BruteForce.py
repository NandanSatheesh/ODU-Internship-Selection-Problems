
import csv
# This module is used for reading and writing CSV files

user = input('System: Hello, What\'s your name?\nUser: ')
# Get the input from the user

file = open('data.csv')
# Open the file containing the data

#Read CSV file and split on ','
csv_file = csv.reader(file,delimiter=',')
# A _csv.reader object is created for handling the data

# Get the all the data stored in the file
data = [row for row in csv_file]

# Delete the first row as it contains the column headers
del(data[0])

# Get the Class to which the user belongs
cls = None

class_of_user = None
# Unpack the data as lists
for row in data:

    name = str(row[0]+' '+row[1])
    # Combine the first name and last name

    if(name==user):
        class_of_user = row[4]

# Prompt string which will be displayed once
prompt = 'System: Whose information would you like to know ' + user + '?'
print(prompt)

# A loop which halts when 'Exit' is typed
while(True):

    # Get the name that has to be searched
    search_element = input('User: ')

    # Break the loop if the input is 'Exit'
    if(search_element == 'Exit'):
        print('System: Bye.')
        exit()

    flag = 0
    for row in data:

        # Form the name string
        name = str(row[0] + ' ' + row[1])

        # Search for the name and print a success message if found
        if(search_element==name and row[4]==class_of_user):
            print('System:',str(row[0]+' '+row[1]+' is from '+row[3]+' and he likes '+row[2]+'.'))
            flag = 1
            break

    # In case of an unsuccessful search, this message will be displayed
    if( flag == 0):
        print('System:',search_element,'not found in Class A. Please ask about students in your class.')
