from sys import argv

script, input_file = argv

# defines function to read and print the file named in the call
def print_all(f):
    print f.read()
    
# defines function to go back to first line after reading (?)
def rewind(f):
    f.seek(0)
  
# defines function to print the line number named in the call,
# from the file named in the command line  
def print_a_line(line_count, f):
    print line_count, f.readline()

# means when current_file is said, it should open the file named in
# the original command line    
current_file = open(input_file)

print '''
'''

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"

rewind(current_file)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

print '''
'''