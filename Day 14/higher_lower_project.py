from art import *
from func import * 
from game_data import *
from click import clear

#sets game end state to False
is_game_end = False

#set player score to o
player_score = 0

#generates a random celebrity
A = generate_celeb()
B = generate_celeb()


#checks to make sure we don't have same celebrities being compared
while B == A:
    B = generate_celeb()


while not is_game_end:
    clear()
    
    #displays the welcomes logo, Higher lower logo
    print(logo)

    #displays celebrity A and B information with vs logo between them
    if player_score > 0:
        print(f"You're right...!!! Current Score : {player_score}")
        
    display_celeb(A,'A')
    print(vs)
    display_celeb(B,'B')

    #Takes player answer on who has more followers
    player_answer = input("Who has more followers? TYpe 'A' or 'B' :  ").lower()
    if player_answer == 'a':
        player_choice = A
    elif player_answer == 'b':
        player_choice = B

    #compare who has more
    if compare_celebs(A, B) == player_choice:
        player_score += 1
        
        A = B
        C = generate_celeb()
        while C == A:
            C = generate_celeb()
        B = C
    else:
        is_game_end = True
        print(f"Sorry, You're wrong...!!! Final Score : {player_score}")

