#!/usr/bin/env python
# coding: utf-8

# # Rock, Paper, Scissors

# ### Libraries and static values

# In[1]:


# Bring in libraries and functions
from random import randint
from termcolor import colored

# Define static terms
throws = ['r','p','s']
throw_words = {'r':'rock','p':'paper','s':'scissors'}
def win():
    print(colored('Player wins!','green',attrs=['bold']))
def lose():
    print(colored('Computer wins!','red',attrs=['bold']))
def draw():
    print(colored('DRAW!','grey',attrs=['bold']))


# ### Game code

# In[ ]:


# Game code loop
while True:
    # Computer's choice
    chosen_num = randint(0,2)
    computer_choice = throws[chosen_num]
    
    # Player's choice
    player_choice = input('\nrock (r), paper (p) or scissors (s)?').lower()
    while player_choice not in throws:
        print('\nCome on man...')
        player_choice = input('rock (r), paper (p) or scissors (s)?').lower()

    # Print out throws
    print('\nOne, Two, Three!')
    print(f'Player throws {throw_words[player_choice]}.')
    print(f'Computer throws {throw_words[computer_choice]}.')
    
    # Determine winner and call defined print function
    if player_choice == computer_choice:
        draw()
    elif player_choice == 'r' and computer_choice == 's':
        win()
    elif player_choice == 'p' and computer_choice == 'r':
        win()
    elif player_choice == 's' and computer_choice == 'p':
        win()
    else:
        lose()

    # Ask to continue and loop or exit
    replay = input('\nPlay again? (y,n)').lower()
    while replay not in {'y','n'}:
        print('\nUgh... letter "y" or letter "n"... jeez...')
        replay = input('\nPlay again? (y,n)').lower()
    if replay == 'n':
        print('\nThanks for playing!')
        break
    if replay == 'y':
        continue


# In[ ]:





