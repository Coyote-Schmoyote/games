import random

play = True

dice1 = random.randrange(1, 6)
dice2 = random.randrange(1, 6)
roll = input("Ready to roll the dice? ")

while play:

    if roll == "yes" or "yep" or "yeah" or "sure":
        print (dice1, dice2)
        again = str(input("One more time? "))
        if again == "no":
            play = False
            print("alrighty then.")
        elif again == "yes" or "yep" or "yeah" or "sure":
            play = True
    elif roll == "no" or "nah" or "nope":
        play = False
        print ('nevermind')
