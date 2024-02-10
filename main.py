# Python program to convert input text to its respective morse code
# This program first validates the input text to make sure it contains only valid characters
# and digits and then proceed with conversion to morse code.

# Import module for regular expression
import re

# Dictionary for available Morse code
morse_code_dict = {
    'a': '.-',     'b': '-...',  'c': '-.-.',   'd': '-..',   'e': '.',      'f': '..-.',  'g': '--.',
    'h': '....',   'i': '..',    'j': '.---',   'k': '-.-',    'l': '.-..',  'm': '--',     'n': '-.',
    'o': '---',    'p': '.--.',  'q': '--.-',   'r': '.-.',    's': '...',    't': '-',     'u': '..-',
    'v': '...-',   'w': '.--',   'x': '-..-',   'y': '-.--',    'z': '--..',  '1': '.----', '2': '..---',
    '3': '...--',  '4': '....-', '5': '.....',  '6': '-....',   '7': '--...', '8': '---..', '9': '----.',
    '0': '-----',  ' ': ' ',
}

is_special_character = True
input_str = ""

# If formatted_string contain non-Null value, it means it contains special characters.
# Loop will continue till valid input string is not given
while is_special_character:
    input_str = input("Please input the string having characters and digits only: ").lower()

    # Using regular expression, check if it contains any non-characters/digits
    # Below regular expression will check for all characters except english letters,
    # digits, white space and "."
    # Note that there is no Morse code for ".", however we are keeping it in the input string
    # as it is common to write text will full stop at the end. "." will be ignored during conversion
    # of the string to Morse code
    is_special_character = re.search(r"[^a-zA-Z0-9.\s]", input_str)

# Using list comprehension, convert each character into it's respective Morse code
# Exclude space and "." character
code_list = [morse_code_dict[char] + ' ' for char in input_str if (char != ' ' and char != '.')]

# Convert list of string to string
print("Mose code of the text is:", ''.join(code_list))

