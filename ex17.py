from sys import argv
from os.path import exists

script, from_file, to_file = argv

print"""
"""

# we could do these two on one line, how?

do_it = open(from_file).read()
# contents = do_it.read()

print "The input file is %d bytes long" % len(do_it)

print "Does the output file exist? %r" % exists(to_file)


out_file = open(to_file, 'w')
out_file.write(do_it)

print "Alright, all done."

out_file.close()
# do_it.close()

print"""
"""