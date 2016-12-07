# Gets info from command line arguments
from sys import argv

# Sets the names of the variables that will get values from the command line
script, filename = argv

# Opens filename entered as argument on command line, when txt is printed
txt = open(filename)

print"""
"""

# Message about printing
print "Here's your file %r:" % filename
# Uses read command on txt with no parameters
print txt.read()
txt.close()

# Switches to user input to run the same command on a filename
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()

print"""
"""