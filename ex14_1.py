# import fuction argv
from sys import argv
#get a filename
script, user_name = argv
# use the raw_input as '> ' 
prompt = '> '

# print strings and ...
print "Hi, %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "what time are you coming to pick me up %s?" % user_name
time = raw_input(prompt)

print """
Alright, so you said %r about liking me.
Nice.
I will be ready at  %r for you.
Looking forward to it. ;) 
""" % (likes, time)