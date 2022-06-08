alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caeser(plain_text, shift_number, caeser_direction):
    new_text = ""
    for letter in plain_text:
        if caeser_direction == "encode":
            new_pos = (alphabet.index(letter) + shift_number) % len(alphabet)
            new_text += alphabet[new_pos]
        elif caeser_direction == "decode":
            new_pos = alphabet.index(letter) - shift_number
            new_text += alphabet[new_pos]
            
    print(f"The {caeser_direction}d text is {new_text}")
        

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caeser(plain_text=text, shift_number=shift, caeser_direction=direction)