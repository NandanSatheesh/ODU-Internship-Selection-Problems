# The answer to the problem is coded using Python 3.6 
# Get the value of N , s1 , s2 from the user

N = int(input('Enter the value of N\n').strip())

s1 = input('Enter the value of s1\n').strip()

s2 = input('Enter the value of s2\n').strip()

# All the characters in the string are converted into a matrix
l1 = []

# The final solution list
solution = []


c = 0
for i in range(N):
    temp = []
    for j in range(N):
        temp.append(s1[c % len(s1)])
        c = c + 1

    l1.append(temp)
# The nested list l1 contains the matrix


# Check row-wise for every occurrence of string s2
rowno = 0
for row in l1:

    rowstring = ''.join(row)
    # print(rowstring)
    start = 0
    if( rowstring.find(s2) != -1):
        start = 0
        while(start != -1):
            temp = rowstring.find(s2,start)
            if (temp != -1):
                solution.append(str(('(%d , %d) to (%d , %d) -> left to right '%(rowno,temp,rowno,temp+len(s2)-1))))

                start = temp + 1
            else:
                break

    rowno += 1

# The transpose of the matrix is calculated

l1 = list(map(list, zip(*l1)))

# Check column-wise for every occurrence of the string s2
colno = 0
for col in l1:

    colstring = ''.join(col)
    # print(rowstring)
    start = 0
    if( colstring.find(s2) != -1):
        start = 0
        while(start != -1):
            temp = colstring.find(s2,start)
            if (temp != -1):
                solution.append(str(('(%d , %d) to (%d , %d) -> top to bottom '%(temp,colno,temp+N-len(s2)-1,colno))))

                start = temp + 1
            else:
                break

    colno += 1
# Sort the solution list, join them using new line escape sequence and print
print('\n'.join(sorted(solution)))
