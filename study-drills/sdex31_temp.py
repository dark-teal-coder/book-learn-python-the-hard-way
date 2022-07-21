# # Study Drills 31

# # 1. Make new parts of the game and change what decisions people can make. 
# # Expand the game out as much as you can before it gets ridiculous.
# # 2. Write a completely new game. 
# # Maybe you don't like this one, so make your own. 
# # This is your computer; do what you want.

# # Going to provide one more elif. 
# print("""You enter a dark room with 3 doors. 
# Do you go through door #1, door #2 or door #3?""")

# door = input("> ")

# if door == "1":
    # print("There's a giant bear here eating a cheese cake.")
    # print("What do you do?")
    # print("1. Take the cake.")
    # print("2. Scream at the bear.")
    
    # bear = input("> ")
   
    # if bear == "1":
        # print("The bear eats your face off. Good job!")
    # elif bear == "2":
        # print("The bear eats your legs off. Good job!")
    # else:
        # print(f"Well, doing {bear} is probably better.")
        # print("Bear runs away.")

# elif door == "2":
    # print("You stare into the endless abyss at Cthulhu's retina.")
    # print("1. Blueberries.")
    # print("2. Yellow jacket clothespins.")
    # print("3. Understanding revolvers yelling melodies.")
    
    # insanity = input("> ")
    
    # if insanity == "1" or insanity == "2":
        # print("Your body survives powered by a mind of jello.")
        # print("Good job!")
    # else: 
        # print("The insanity rots your eyes into a pool of muck.")
        # print("Good job!")

# # One more elif added 
# elif door == "3":
    # print("Well, you've escaped from the bear to a sleeping tiger!")
    # print("Are you going to run or stay?", "1. Run", "2. Stay", sep="\n")
    
    # move = input("> ")
    # if move == "1":
        # print("Ok, you're safe.")
    # else:
        # print("Oh no, the tiger is waking up and it just sees you.")

# else:
    # print("You stumble around and fall on a knife and die. Good job!")

# My new game

print("LOADING A NEW GAME".center(100, "."), 
"Welcome to the game \"Designing Your Life\"! The game is going to start now.",
"LOADING THE GAME".center(100, "."),
sep="\n")

def start():
    print("Type START to start a new game or QUIT to quit.")
    startQuit = input(">>> ").upper()
    if startQuit == "START":
        print("Welcome, you're now in the game! My name is Roxanne Saewong.\
        I'm your life coach in this game. I'll be with you through your life journey here.\
        \
        First thing first, let me ask you some questions about you!".replace("        ", "\n"))
        playerName = input("What's your name? ")
        birthplace = input("Where were you born? ")
        currentAge = int(input("How old are you now? "))
        print(f"""Alright, {playerName}, I've got some basic info about you.\
        You're born in {birthplace} and now you're {currentAge} years old.\
        \
        You must have a lot of questions about what you're doing here right now.\
        Cool! Let me tell you what you're going to do to complete this game.\
        \
        So at this point in your life, you feel like your life is screwed up.\
        You wish you'd go back to fix it.\
        What if I tell you you can time-travel back to a certain age to do so?\
        At different ages, you'll be put in the corresponding life stages.\
        E.g. If you choose to go back to the time when you're in school, you'll become a student again.\
        \
        Let's do it now!""".replace("        ", "\n"))
        chooseNewAge(currentAge)
    elif startQuit == "QUIT":
        print("It's sad to see you go. I hope you'll come back to me again. Good luck!")
    else:
        print("Please follow the instruction!")
        start()

# Functions are reusable: to be recalled when not 0 <= newAge < currentAge. 
def chooseNewAge(currentAge):
    # Better add exception handling to prevent the user from enter a non-interger.
    newAge = int(input("At what age would you like to go back? "))
    play(newAge, currentAge)

def continueOrQuit(currentAge):
    continuation = input("Would you like to CONTINUE or QUIT playing? ").upper()
    if continuation == "CONTINUE":
        chooseNewAge(currentAge)
    else:
        print("I hate seeing you go...")

def play(newAge, currentAge):
    collegeDecision = ""
    doBusiness = ""
    if newAge < 0:
        print("You can't go back to when you're not born yet. ")
        continueOrQuit(currentAge)
        
    elif newAge == currentAge:
        print("You're at this point/age in your life right now. ",
        "Therefore, it's pointless to go on the spaceship. I'll let you do this again. ", 
        sep="\n")
        continueOrQuit(currentAge)
    elif newAge > currentAge:
        print("Sorry, our spaceship can't take you to the future just yet. ",
        "We're currently working on this new feature of our spaceship. ", 
        "Please come back again in the near future to see if it'll be available then. ", 
        "As for now, please choose another point in your past. ", 
        sep="\n")
        continueOrQuit(currentAge)
    else:
        print("Alright, your journey is about to begin! ", 
        "Get a seat behind your captain! That's me by the way. ", 
        "Buckle up! Ready? The spaceship is taking off... ", 
        "Finally, we've arrived at our destination safely. ", 
        sep="\n")
        if 0 <= newAge < 5:
            print("Well, you've landed in the period of your early childhood. ", 
            "You don't get to choose what to do with your life at this stage. ", 
            "Your parents will help you decide. ", 
            sep="\n")
        elif 5 <= newAge < 10:
            print("You're now in elementary school. ", 
            "Are you going to finish your elementary school? ", 
            sep="\n")
            elementarySchool = input("YES or NO? ").upper()
            if elementarySchool == "YES":
                print("That's a good decision! ", 
                "It's too early for you to jump out of school at this stage. ",
                sep="\n")
            else:
                print("That's not a wise decision! ",
                "It's too early for you to jump out of school at this stage. ",
                "You should get the basic education. ",
                sep="\n")
        elif 10 <= newAge < 14:
            print("You've come back to your middle school. ", 
            "Are you going to finish your middle school? ", 
            sep="\n")
            middleSchool = input("YES or NO? ").upper()
            if middleSchool == "YES":
                print("That's a good decision! You're learning a lot! Keep going!. ")
            else:
                print("You shouldn't quit at this point.", 
                "You're in the middle of learning. ",
                "Get the basic education! ",
                sep="\n")
        elif 14 <= newAge < 18:
            print("You're now in high school. ", 
            "Are you going to finish your high school? ", 
            sep="\n")
            highSchool = input("YES or NO? ").upper()
            if highSchool == "YES":
                print("That's a wise decision! ", 
                "If you go further, you'll see more options in your life. ",
                sep="\n")
            else:
                print("I know you're fed up with the boring school system. ", 
                "And you may want to start earning at this stage. ",
                "But you won't be earning much unless your parents are feeding you. ", 
                "You'll get to decide if you want to go to college when you finish high school. ",
                sep="\n")
        # A problem with 18 <= newAge <= 22:
        elif newAge == 18:
            print("You've just graduated from your high school. ", 
            "Are you going to go to college? ", 
            sep="\n")
            collegeDecision = input("YES or NO? ").upper()
            if collegeDecision == "YES":
                print("Great! Congratulations! ")
            else:
                print("Are you going to do business then? ")
                doBusiness = input("YES or NO? ").upper()
                if doBusiness == "YES":
                    print("Not bad! You start earning early in your life. ")
                else: 
                    print("That's an unwise decision! ")
        elif 18 < newAge <= 22 and collegeDecision == "YES":
            print("You're in college. ", 
            "It's not too long before you can obtain a professional job. ",
            "Don't give up yet! ", 
            sep="\n")
        elif 18 < newAge <= 22 and collegeDecision == "NO":
            if doBusiness == "YES":
                print("Your business has just started. ")
            else:
                print("You're not doing so well at this stage of your life. ")
        elif 22 < newAge <= 59:
            print("You're working hard to make a living in your life...\
            It's the period when people can make the most money in their life.\
            Don't overspend! Remember to save some for your retirement.\
            It's also best to learn how to invest part of your money.\
            So you can use your money to generate more money.".replace(".            ", ".\n"))
        elif 60 <= newAge <= 69:
            print("It's time for you to consider retirement. ")
        else:
            print("Quit your job and retire if you haven't. \
            Enjoy the life without work! ".replace("            ", ""))

start()

print("\(OO)/".center(100, "."))
print("You're approaching the end of the game. The purpose of this game is \
to stimulate you to think about what you'd have done better if given a second chance. \
But you can't be reborn. So make wise decisions as you go. \
All the best in your life journey!")
print("END OF THE GAME".center(100, "."))
