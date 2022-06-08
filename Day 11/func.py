import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game = {
            "player cards" : [],
            'player score' : 0,
            'computer cards' : [],
            'computer score' : 0,
        }

def show_results():
    print(f"Your cards: {game['player cards']}. Your score: {game['player score']}")
    print(f"Computer's card: {game['computer cards']}. Computer Score: {game['computer score']}")
        
def draw_card(drawer):
    '''draws card and adds score to game'''
    cards_drawn = []
    if drawer == 'player':
        new_card = random.choice(cards)
        if (new_card == 11) and (sum(game['player cards']) + new_card > 21):
                new_card = 1
        cards_drawn.append(new_card)
        game['player cards'].extend(cards_drawn)   
        game['player score'] = sum(game['player cards'])
        
    elif drawer == 'computer':
        while sum(cards_drawn) < 17 :
            new_card = random.choice(cards)
            if (new_card == 11) and (sum(game['computer cards']) + new_card > 21):
                new_card = 1
            cards_drawn.append(new_card) 
        game['computer cards'].extend(cards_drawn)
        game['computer score'] = sum(game['computer cards'])
        
    print(f"{drawer.title()} draws {cards_drawn}")
    

    