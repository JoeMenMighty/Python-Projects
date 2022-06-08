from ast import Break
from art import logo
from click import clear
from func import *


game_play_status = input("Press 'y' to play Black or Press 'n' to quit.........\n")

def checker():
    answer = True
    show_results()
    if game['computer score'] != 0:
        if (game['player score'] <= 21) and (game['computer score'] <= 21):
            if game['player score'] == game['computer score']:
                print("\nIt's a Draw")
            elif game['computer score'] > game['player score']:
                print("\nComputer wins ......!!!!!!")
            else:
                print("\nYou win ......!!!!")
    elif game['computer score'] == 0:
        if game['player score'] > 21:
            answer = False
            print("You loose...... !!!!! Should not be more than 21 ....")
    return answer
        
def play_game():
    print("Welcome to Mighty's Black Jack Game!!!!")
    print(logo)
    
    draw_status_answer = input("\nIt's your turn to draw your cards..................\nShuffling cards ........\nPress 'y' to draw or 'p' to pass :  ")
    if draw_status_answer == 'y':
        draw_status = True
        
    while draw_status:
        draw_card("player")
        if checker() == True:    
            draw_status_answer = input("\nDo you want to draw another card..................\nShuffling cards ........\nPress 'y' to draw or 'p' to pass :  ")
            if draw_status_answer == 'n':
                draw_status = False
        elif checker() == False:
            draw_status = False
            
    if draw_status_answer == 'n':       
        draw_card("computer")
        checker()

if game_play_status == 'y':
    play_game()
elif game_play_status == 'n':
    clear()
    