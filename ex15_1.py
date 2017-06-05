# import function argv
from sys import argv
#get a filename
script, filename = argv
#open a file called the filename put in raw_input
txt = open(filename)
#print string includes filename(from raw_input)
print "Here's your file %r:" % filename
# print read and print out  text in the filename
print txt.read()
