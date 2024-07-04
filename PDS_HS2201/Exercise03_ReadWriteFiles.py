# Read and write files

# ************
# Exercise 03
# ************

# Change the solution of Exercise 02 so that the program writes the output to the file 'musicians2.txt'.
# task 3.2 instead

fh_in  = open("musicians.txt")


counter = 0
output = ''
for line in fh_in:
    if counter < 2:
        print(output+line.rstrip()+' ', end = '')
        counter +=1
    else:
        print( '(' + line.rstrip().upper() + ')')
        counter = 0
        output = ''

fh_in.close


