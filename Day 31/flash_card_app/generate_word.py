import pandas
import pandas as pd
import random


try:
    data = pd.read_csv('data/words_to_learn.csv')
except:
    new_data = pd.read_csv('data/french_words.csv')
    data_dict = new_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

words_to_learn = {}


def generate_word():
    new_word = random.choice(data_dict)
    return new_word


def known_word(word_to_remove):
    global words_to_learn
    data_dict.remove(word_to_remove)
    words_to_learn = pd.DataFrame(data_dict)
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    print(len(words_to_learn))
    print("word removed")


