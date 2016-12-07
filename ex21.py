print '''
'''

# defines function that adds two arguments and then displays
def addfunction(a, b):
    print "ADDING %d and %d" % (a, b)
    return float(a + b)
    
# defines function that subtracts arguments and then displays
def subtractfunction(a, b):
    print "SUBTRACTING %d from %d" % (b, a)
    return float(a - b)
    
# defines function that multiplies two arguments and then displays
def multiplyfunction(a, b):
    print "MULTIPLYING %d by %d" % (a, b)
    return float(a * b)
    
# defines function that divides two arguments and then displays
def dividefunction(a, b):
    print "DIVIDING %d by %d" % (a, b)
    return float(a / b)
    

print "Let's do some math with just functions!"
# runs function on arguments provided in parentheses
age = addfunction(30.0, 5.0)
height = subtractfunction(78.0, 4.0)
weight = multiplyfunction(80.0, 2.0)
iq = dividefunction(390.0, 2.0)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
# runs nested functions, starting with dividing iq by 2
what = addfunction(age, subtractfunction(height, multiplyfunction(
    weight, dividefunction(iq, 2.0)))
    )

print "That becomes: ", what, "Can you do it by hand?"

print '''
'''