import random

play = True

print("Guess a number between 1 and 10!")


while play:
    try:
        user_answer = int(input('Your number: '))
    except ValueError:
        print("It\'s not a number, idiot")
    else:
        random_number = random.randrange(1, 10)
        while user_answer != random_number:
            if user_answer>random_number:
                print("Try a smaller number.")
                user_answer = int(input('Your guess: '))
            elif user_answer < random_number:
                print("Try a bigger number.")
                user_answer = int(input('Your guess: '))
        print(f"YOU\'RE A PSYCHIC! CONGRATS!!!!")



    try:
        again = str(input("Do you want to play again? Type yes or no: "))
    except ValueError:
        print('I don\'t understand.')
    else:
        if again == "no":
            play = False
            print('ok, bye then')
        elif again == "yes":
            play = True