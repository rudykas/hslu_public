# Read and write files

# ************
# Exercise 02
# ************

# Write a program that combines three lines from the file 'musicians.txt' into one each
# and outputs them as standard output using print ().

# That means:  An output line should contain the first name, the last name and the artist name ("K�nstername") or band of the artist.
# The band or artist name should be outputed in brackets and in captial letters.
# Example "Marshall Bruce Mathers III (EMINEM)"

# Brian
# Molko
# placebo
# Jim
# Morrison
# The Doors
# Ray
# Davies
# The Kinks
# Marshall Bruce
# Mathers III
# Eminem
# Andre Romelle
# Young
# Dr. Dre
# Beth
# Gibbons
# Portishead



fh = open("musicians.txt")
print(fh)
fo = open("musicians3.txt", 'w')
output = ''
counter = 0
for line in fh:
    if counter < 2:
        output = output+line.rstrip()+' '
        counter +=1
    else:
        output = output + '(' + line.rstrip().upper() + ')\n'
        fo.write(output)
        counter = 0
        output = ''


fh.close()
fo.close()
 