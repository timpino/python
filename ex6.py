# declares variables
x = "There are %d types of people." % 10 #builds a string adding 10 to the text
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # builds a string adding the two above variables to it.

#Prints the two aggregated strings created above
print x 
print y

#Prints the complete strings in %r formatting and '%s' formatting encapsulating the text with ''
print "I said: %r." % x
print "I also said: '%s'" % y
# declares a boolean variable and prints it with it's boolean formatting (False) %d would give 0 etc.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#prints the concattenated string.
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"

#again concatenates strings and prints them
print w + e