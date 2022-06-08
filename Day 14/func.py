from game_data import data
import random


def generate_celeb():
    '''Generates random celebrity from the game data and return it.'''
    return random.choice(data)

def display_celeb(celeb,name):
    '''Displays the celebrity info in plain english. Takes a celebrity as input'''
    print(f"Compare {name} : {celeb['name']}, a {celeb['description']}, from {celeb['country']}")


def compare_celebs(celeb_A, celeb_B):
    '''Compares both celebrity followers and returns True or False on who has more'''
    greater = {}
    if celeb_A['follower_count'] > celeb_B['follower_count']:
        greater = celeb_A
    else:
        greater = celeb_B
        
    return greater