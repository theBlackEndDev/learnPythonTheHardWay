# string inside a string
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
# string inside a string
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

# this has a string inside a string
print "I said: %r." % x
# this also has a string inside a string
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# this uses concatenation
print w + e
