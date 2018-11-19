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
del(data[0])

# Create a dictionary with names as key and hometown as values
name_hometownn = { row[0]+' '+row[1]:row[3] for row in data}

# Create a dictionary with names as key and class as values
name_class = { row[0]+' '+row[1]:row[4] for row in data}

# Create a dictionary with names as key and likes as values
name_likes = { row[0]+' '+row[1]:row[2] for row in data}


class_of_user = name_class.get(user)


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

    # Find the details of the classmate's name entered by the student
    if(not( name_class.get(search_element) is None)):
        if(name_class.get(search_element)==class_of_user):
            if(not(name_likes.get(search_element) is  None and name_hometown.get(search_element) is None )):
                print('System: %s is from %s and he likes %s.'%(search_element,name_hometownn.get(search_element),name_likes.get(search_element)))

        # Print a message if the required data is not found in the same section
        else:
            print('System: %s not found in Class %s. Please ask about students in your class.'%(search_element,class_of_user))
