import random 

print("Welcome to Mighty's Guess the number game !!!")
print("i am thinking of a number between 1 and 100")

number_guessed = random.randint(1,100)

difficulty = input("Choose your level of difficulty..... Type 'e' for Easy of 'h' for Hard :  ")
if difficulty == 'e':
    no_lives = 10
elif difficulty == 'h':
    no_lives = 5


guessed_right = False

while no_lives > 0 :
    user_guess = int(input("Make your guess:  "))
    
    if user_guess == number_guessed:
        print(f"Wonderful, you guessed the number correctly..!!!!\nThe number was {user_guess}")
        guessed_right = True
        no_lives = 0
    elif user_guess > number_guessed:
        print("Too High...!!!!\nGuess again")
        no_lives -= 1
    else:
        print("Too Low...!!!!\nGuess again")
        no_lives -= 1

if not guessed_right:
    print("Sorry, You're out of lives... !!! You Lost...!!!")