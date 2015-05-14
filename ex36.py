from sys import exit

def bedroom():
    print """
    Your eyes open.
    You grunt.
    There is no escaping the fact that you are...
    MASSIVELY hungover.
    The room is gently spinning to the tune of the throbbing in you head.
    To your left is an exit leading to a kitchen.
    What do you do?"""
    
    choice = raw_input("> ")
    if "look" in choice:
        print """
        You look around the room, 
        There are flowers on the blankets.
        There is a crack the size of grand canyon on the gently spinning ceiling.
        You are definitely naked but there are no clothes in here.
        On your arm you find a gently snoring girl.
        She is vaguely familiar...
        Yes, that's definitely your Ex.
        You know the one who wasn't quite the looker. 
        But loved you more even than she loved Nutella.
        - You are a despicable creature.
        Now What do you do?"""
        choice = raw_input("> ")
        if "arm" in choice:
            print """
            You attempt to gently pry your arm away from your shame...
            - You really are worthless, aren't you?
            She takes a big drag, and you freeze mid movement.
            But she is still asleep and your arm is now free.
            Oh joy. Be so very proud.
            Now what?"""
            choice = raw_input("> ")
            if "left" in choice:
                kitchen()
            else:
                die("You die from a headache turn haematoma.")
        else:
            die("You awoke your ex, and she wants sexytime without rubber...\n18 years of custody to pay.")
    else:
        die("Midstep you are attacked from behind and die from shock.")
        
        
def die(why):
    print "\n"
    print why, "\nFucking idiot."
    print "="*14
    exit(0)
    
def kitchen():
    print """
    Having escaped the bedroom you, our mighty hero,
    stumble into the kitchen.
    Your head is throbbing something fiercly.
    Spots of color is dancing in front of your eyes.
    To your right lies the living room.
    """
    
    aspirin = False
    choice = raw_input("> ")
    if "look" in choice:
        print """
        There is a foul butt print in the grime on the kitchen counter.
        You see a used condom on the floor.
        4 empty bottles of cheap red wine are in the sink.
        Only two dirty wine glasses are on the counter.
        - You must be a special kind of idiot.
        - The kind that are not allowed to be called 'special'
        You notice a canister of Aspirin
        Your head is trying to implode on itself.
        Now what?"""
        while True:
            choice = raw_input("> ")
            if "aspirin" in choice and not aspirin:
                print """
                You grab the canister of aspirin.
                Quickly you down 5 pills.
                The headache subsides to a mild 'humm'
                there is no more risk of sudden haematoma.
                Good for you.
                Let's get the fuck out of here.
                Where to?"""
                aspirin = True
            elif "aspirin" in choice and aspirin:
                die("You overdose on aspirin like 14 year old girl. Real manly.")
            elif "right" in choice and aspirin:
                living_room_L() 
            elif "condom" in choice:
                die("You get Lupus and die horribly.\nAlso your brain explodes.\nAnd you shit yourself.")
            elif aspirin:
                die("Confusion kills even the brightest. And you are a...") 
            else:
                die("Your brain implodes on itself. Blood pours out of your eyes.")
        
    else:
        die("A sudden stroke kills you where you stand. Try to drink beer next time.")
    
    
def living_room_L():
    print """
    You enter the Living room.
    You feel the runs are fighting with your bowels.
    You are also completely naked.
    To your left is the entrance.
    To your right is a continuation of the living room.
    You notice your shirt laying on the floor.
    There is also a girl blouse on the floor.
    What do you do?
    """
    shirt = False
    pants = False
    while True:
        choice = raw_input("> ")
        if "shirt" in choice and not shirt:
            print """
            You quickly grab your shirt.
            You put it on with one button askew.
            You almost feel like a god.
            Of misery.
            Now what you stylish piece of shit?
            """
            shirt = True
        elif "shirt" in choice and shirt:
            die("You put on a girl blouse atop your shirt. Not even hipsters are that stupid...")
        elif "blouse" in choice:
            die("Going tranny?")
        elif "right" in choice:
            pants = living_room_R()
            print """
            You are back and on a mission. Pants almost make you whole!
            To your left is the entrance.
            - Make the right decision for fucks sake...
            Where to now you manly beast?"""
        elif "left" in choice:
            entrance(shirt, pants)
        else:
            die("Your sphincter can no longer hold against the pressure.\nYour diarrhea explodes down your leg leaving a puddle on the floor.\nYour ex wakes up and finds you laying in a pool of liquid shit.")

def living_room_R():
    print """
    You move into the living room and notice your pants on the couch.
    There is also a pair of XXL panties with a used maxi pad in them on the couch.
    Time is of the essence.
    Your ass is seriously complaining about yesterdays diet.
    Now what?
    """
    choice = raw_input("> ")
    if "pants" in choice:
        print """
        You grab your pants quickly and hurry back.
        You feel the diarrhea pressing against your poop shoot.
        You are so in control of this.
        - I'm almost proud.
        """
        return True
    elif "panties" in choice:
        die("Stopping to smell a used maxi pad is not a wise time investment.\nYour bowels can't take it anymore.\nYour diarrhea sprays the couch and the stench makes you barf.\nYour ex wakes up to find you in a pool of excrement and vomit.")
    else:
        die("Your bowels explode all over your pants. You have to move in with your ex now.")

def entrance(shirt, pants):
    print shirt, pants
    print """
    The entrance is small, there are plastic bags covering the floor.
    The smell of wet clothes is heavy in the air.
    On the floor you notice your shoes.
    Ahead is the door out and freedom.
    To your right is the toilet.
    Freedom is so close... Where to?
    """
    bowels = False
    shoes = False
    while True:
        choice = raw_input("> ")
        if "right" in choice and not bowels:
            bowels = toilet()
            print "With your bowels emptied all you need to do is get the fuck out"
            print "Preferably soon rather than late"
        elif "shoes" in choice and not bowels and not pants:
            die("As you bend down to pick up your shoes\nYour ass sprays the wall with diarrhea")
        elif "shoes" in choice and not bowels:
            die("As you bend down you sphincter gives way.\nYour pants fill with warm diarrhea running down your leg.")
        elif "shoes" in choice and bowels:
            print "You bend down to pick up your shoes"
            shoes = True
        elif "open door" in choice:
            print "Freedom!"
            if not bowels:
                die("As you step out of the door your pants get warm and sticky with poo.")
            elif not pants:
                die("Your member freezes like a popsicle.\nRecognizing that life is not worth living without a dick you break it off\nand stab yourself to death with your frozen dick.")
            elif not shirt:
                die("You may look like a god but you freeze to death like a goldfish in the freezer.")
            elif not shoes:
                die("You get halfway home before your feet freeze and you die.")
            else:
                win()
        else:
            if bowels:
                die("Your ex wakes up, now you have to marry her.")
            else:
                die("It hits the fan...\nYou shit yourself, ruining your shoes on the floor.")
        
    
def toilet():
    print """
    You enter the toilet.
    You notice your pale pasty face in the mirror.
    You look awful.
    You notice two used condoms floating in the toilet.
    There is no way to wash your hands.
    The entrance is to your left.
    What do you do?
    """
    choice = raw_input("> ")
    if "shit" in choice:
        print """
        You plop your ass down on the shitty toilet.
        As you lighten your mental grip on your sphincter your ass explodes.
        It is violent.
        You feel raped.
        Sweat beads on your forehead.
        The noise could wake a bear.
        The stink could kill a fly.
        But.
        Your ass is no longer trying to explode.
        You know after that noise you don't have long before your ex awakens.
        You have to wipe effectively but not use up the toilet paper.
        """
        sheets = 15
        used = 0
        clean = 12
        
        for i in range(1, 4):
            print "How many sheets do you use for the #%d wipe?" % i
            choice = raw_input("> ")
            try:
                int(choice)
            except ValueError:
                die("You die of an infected asshole since you cannot wipe")
            if int(choice) <= 0:
                die("Putting used toilet paper back on the roll is really smart...")
            used += int(choice)
            if used > sheets:
                die("There is not enough paper on the roll.\nYou Franticly scramble around looking for more TP.\nYour Ex Wakes up. This is bad.")
            if 0 < int(choice) < 3:
                die("The paper breaks while you wipe smearing shit all over your hand.\nYou scream out in anger waking the ex.\nYou now have a wife.")
            else:
                print "You make a nice wipe without smearing too much shit on your hand."
        print used
        if clean <= used <= sheets:
            print "You could eat off that asshole!"
            print "Come to think of it, you got a rimjob last night. - Good for you!"
            print "You hurry out into the entrance"
            return True
        else:
            die("Your ass is still splattered with shit and your ex wakes up.\nNow you have a wife.")
    elif "condom" in choice:
        die("Touching the condom gives you Super-AIDS, you die instantly.\nAfter release your bowels.")
    else:
        die("You know the drill.\nPoo everywhere.\nWife.\nKids.\nSuicide the only option!")
    
    
    
def win():
    print """
    Congratulations, you escaped your ex.
    You should be mildly proud.
    You still disgust me.
    She will wake up and wonder if it was all a dream.
    The only keepsake she has of you is the
    steaming diarrhea you left in the unflushed toilet.
    Expect her to call.
    Fucking. Idiot.
    """
    exit(0)

def start():
    # write a description of how to play the game.
    print """
    Welcome to the horrible escape from the clutches of evil!
    Facing you will be horrors unimaginable!
    Only your slight wits can help you on this quest.
    Also these words are helpful:
    shit, condom, blouse, shirt, shoes, 
    pants, left, arm, look, aspirin, right, 
    panties, open door
    
    It's dangerous to go alone. Bye.
    """
    raw_input("> ")
    bedroom()



start()