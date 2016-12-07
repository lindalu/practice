# variable x set to string, with 10 filled in by formatting variable
x = "There are %d types of people." % 10

# variables set to text strings
binary = "binary"
do_not = "don't"

# variable y set to text string, with the above variables filled in as well
y = "Those who know %s and those who %s." % (binary, do_not)

print ""
print ""

# prints first text string, then second text string, then repeats them
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# sets variable to value False
hilarious = False

# sets variable to text string including formatting variable
joke_evaluation = "Isn't that joke so funny?! %r"

# prints the above text string, and inserts value of 'hilarious' (False)
print joke_evaluation % hilarious

w = "This is the left side of... "
e = "a string with a right side."

# prints the above two strings on the same line
print w + e
print ""
print ""