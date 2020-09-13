
import sys
import time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        time.sleep(.1)

play = True

while play:
    print_slow(f'Once upon a time, there was a brave person, who volunteered to save the planet from eternal darkness.'
          f'\n By the way, what\'s your name, pal?\n')
    name = input ('My name is ')
    print_slow(f'So, as I was saying, the name of that brave heart was {name}.'
           f'\n And {name} courageously went to the Spooky Forest of Horrible Things to find the source of darkness, '
           f'\n which humans left there a thousand years ago and forgot about it.')
    print_slow(f'\n However, the source of darkness is consuming the world, because it was left unattended.'
           f'\n Our hero {name}, we are forever grateful that you will be sacrificing your life for the humanity! Ahahaha.')
    print_slow(f'\nNow go, {name}, go.')

    choices1 = ['Go to the Spooky Forest of Horrible Things', 'Go back Home', 'Start crying']


    print_slow(f'You enter the forest, and soon the darkness from the tall pine trees consumes you.'
                    '\n You hear weird sounds around you, and a very dim greenish light far away from you.')
