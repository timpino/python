#Import module to read arguments passed to the script
from sys import argv

# takes the arguments and places them into variables.
script, filename = argv

# opens the file and passes it into the variable txt
txt = open(filename)

# prints the file witht the read function
print "Here's your file %r: " % filename
print txt.read()

#prompts for another filename
#print "Type the filename again:"
#file_again = raw_input("> ")
# open the new textfile and put it into the txt_again variable
#txt_again = open(file_again)

#print every line of the txt file
#print txt_again.read()
