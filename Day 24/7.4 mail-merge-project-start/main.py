#TODO: Create a letter using starting_letter.docx
WORD = '[Name]'
all_names = []

# get all names
with open('./Input/Names/invited_names.txt') as file:
    content = file.readlines()
    for name in content:
        new_name = name.strip('\n')
        all_names.append(new_name)

with open('./Input/Letters/starting_letter.txt', mode='r') as file2:
    starting_letter = file2.read()
    for name in all_names:
        new_letter = starting_letter.replace(WORD, name)
        name_of_file = f'./Output/ReadyToSend/letter_for_{name}.docx'
        with open(name_of_file, mode='w') as letter_to_send:
            letter_to_send.write(new_letter)


