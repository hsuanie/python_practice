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

#ask user to type filename again
print "Type the filename again:"
#define file_again as the raw_input
file_again = raw_input ("> ")
#open the demand file
txt_again = open(file_again)
#print the text in the file
print txt_again.read()