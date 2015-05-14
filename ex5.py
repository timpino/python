name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
in_to_m = 0.0254
lbs_to_kg = 0.453592

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "That is %2.2f meters tall." % (height * in_to_m)
print "He's %d pounds heavy." % weight
print "That is %6.1f kg heavy. " % (weight * lbs_to_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teet are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)

