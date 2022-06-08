from art import logo
import random
from click import clear


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game_status = True

game = {
            "user cards" : [],
            'user score' : 0,
            'computer cards' : [],
            'computer score' : 0,
        }

def draw_cards(number):
    card_drawn = []
    for x in range(0,number):
        card = random.choice(cards)
        card_drawn.append(card)
    return card_drawn

def show_results(game_name):
    print(f"Your cards: {game_name['user cards']}. Your score: {game_name['user score']}")
    print(f"Computer's card: {game_name['computer cards']}. Computer Score: {game_name['computer score']}")

def score_calculator(cards):
    score = sum(cards)
    return score

def update_cards():
    game['user score'] = score_calculator(game['user cards'])
    game['computer score'] = score_calculator(game['computer cards'])
    
    
# def game_status(player_cards):
#     if game[player_cards] > 21 :
#         print(f"Sorry, you got over 21. You loose !!!")
#     elif game[player_cards] == 21:
#         print(f"Yessssssss. You won!!!")
#     else:
        
        
def play_game():
    game['user cards'] = draw_cards(2)
    game['computer cards'] = draw_cards(1)
    
    update_cards()
    print(logo)
    
    
    show_results(game)
    draw_status = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_status == 'y':
        user_new_draw = draw_cards(1)
        game['user cards'].extend(user_new_draw)
        player = "user cards"
    elif draw_status == 'n':
        player = "computer cards"
        computer_new_draw = draw_cards(1)
        game['computer cards'].extend(computer_new_draw)
        if game['computer score'] < 17:
            computer_new_draw = draw_cards(1)
            game['computer cards'].extend(computer_new_draw)
    
    update_cards()
    
    show_results(game)
        
        

status = input("Do you want to play a game of Black Jack? Type 'y' for yes or 'n' for no: ")
if status == 'y':
    play_game()
elif status == 'n':
    clear()
