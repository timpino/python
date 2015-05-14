the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes throguh a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of the type %s" % fruit

# also we can go through mixed lists too
# notisce we have to use %r since we do not know what is in it.
for i in change:
    print "I got %r" % i

#we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 coutns
#for i in range(1, 99):
#    print "Adding %d to the list." % i
    #append is a function that lists understand
#    elements.append(i)
elements.extend(range(1,99,9))
# now we can print them out too
for i in elements:
    print "Element was: %d" % i