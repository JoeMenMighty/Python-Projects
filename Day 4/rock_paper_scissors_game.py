'''
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding variable: rock, paper, and scissors. This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the game on the World Rock Paper Scissors Association website.
'''
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
options = [rock, paper, scissors]

#Accept user choice
user_num = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_num < 3 :
    #display user choice
    print("You Chose: \n")
    user_choice = options[user_num]
    print(user_choice)

    #display computer choice
    print("Computer Chose: \n")
    computer_choice = random.choice(options)
    print(computer_choice)


    #check who won
    if computer_choice == user_choice :
        print("It's a draw!!!")
    elif ((computer_choice == rock) and (user_choice == scissors))or ((computer_choice == paper) and (user_choice == rock)) or ((computer_choice == scissors) and (user_choice == paper)):
        print("Computer Wins!!!.\nYou loooseee!!!. Call Dede Ayew for an excuse to use.")
    else:
        print("You won!!! You may be better than the Black Stars..")
else:
    print("Don't be like oliver twist!!! Choose 0, 1 0r 2. Your head like konko.")