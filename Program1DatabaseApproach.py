import pymysql
# Import the required SQL driver to connect to the Database

# Establish a working connection to the database
try:
    conn = pymysql.connect(host='localhost',user='root',passwd='',db='ODUIP')
except:
    print('Error! Can\'t connect to the Database at the moment ')
    exit()

# Get the cursor object
cursor = conn.cursor()



user = input('System: Hello, What\'s your name?\nUser: ')

prompt = 'System: Whose information would you like to know ' + user + '?'

print(prompt)

# Get the first name and the last name
fname , lname = user.split(" ")

# SQL Query to find the class of the user
sqlstring = " SELECT CLASS FROM STUDENTDATA WHERE FIRST_NAME = '%s'  AND LAST_NAME = '%s' "%(fname,lname)

# Execute the Query
cursor.execute(sqlstring)

# Convert it as a string for ease of usage
cls  = ''.join(list(cursor.fetchone()))

# This loop stops when the user enters 'Exit'

while(True):

    # Get the name that has to be searched
    search_element = input('User: ')


    # Break the loop if the input is 'Exit'
    if (search_element == 'Exit'):
        print('System: Bye.')
        exit()

    try:
        # Split the search name into it's first name and last name
        sfname , slname = search_element.split(" ")
        sqlstring = """
            SELECT * FROM STUDENTDATA 
            WHERE FIRST_NAME = '%s' AND LAST_NAME = '%s' 
            AND CLASS = ( SELECT CLASS FROM STUDENTDATA WHERE FIRST_NAME = '%s'  AND LAST_NAME = '%s' )     
        """ %(sfname,slname,fname,lname)

        cursor.execute(sqlstring)

        result = cursor.fetchone()

        # Check if the result object is empty and perform a set of actions accordingly
        if(result==None):

            print('System:',search_element,'not found in Class',cls,'. Please ask about students in your class.')

        else:
            result = list(result)
            print('System: %s %s is from %s and he likes %s.' %(result[0] , result[1] , result[3] , result[2]))

    except:

        print('Error! Can\'t connect to database at the moment')

# Close the connection which was made to access the database
conn.close()
