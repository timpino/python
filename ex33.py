
numbers = []

def fillShit(shit,top):
    i = 0  
    while i < top:
        print "At the top i is %d" % i
        shit.append(i)
    
        i = i + 1
        print "Numbers now: ", shit
        print "At the bottom i is %d" % i

fillShit(numbers, 7)    
print "The numbers:"

for num in numbers:
    print num
    