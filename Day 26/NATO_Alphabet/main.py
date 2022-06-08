import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
my_data = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet = {row.letter: row.code for (index, row) in my_data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
invalid_entry = True

# # using while loops
# while invalid_entry:
#     user_input = input('Enter the word you want to translate : ').upper()
#     try:
#         for word in user_input:
#             nato_alphabet[word]
#     except KeyError:
#         print("Please enter only words in the alphabet\n")
#     else:
#         invalid_entry = False
#         translated_word = [nato_alphabet[word] for word in user_input if word in nato_alphabet.keys()]
#
# print(translated_word)


# using recursive functions
def phonetizer():
    user_input = input('Enter the word you want to translate : ').upper()
    try:
        for word in user_input:
            nato_alphabet[word]
    except KeyError:
        print("Please enter only words in the alphabet\n")
        phonetizer()
    else:
        translated_word = [nato_alphabet[word] for word in user_input if word in nato_alphabet.keys()]
        print(translated_word)

phonetizer()