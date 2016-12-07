print'''
'''

# defines the function name and its arguments, then what it does
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
# provides values right from the command line
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# uses variables to assign values
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# gives values by having python do some math
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# gives values by having python retrieve the values of the variables
# and then doing math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese - 5, amount_of_crackers + 1000)

print '''
'''