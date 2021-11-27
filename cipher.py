
import basic_sp_network
from user_input import get_user_input
import hex_ascii_converter

#define user options
usage_message = "To ENCRYPT enter '1', to DECRYPT enter '2': "
user_choice = int(0)
#array to hold user options
action = ["Encrypt", "Decrypt"]

#get valid input from user
while True:
    try:
        user_choice = int(get_user_input(usage_message))
        if user_choice < 3 and user_choice > 0:
            if isinstance(user_choice, int) == True:
                break
    except ValueError: 
        print("Input must be an integer between 1 - 2!")

#allow user input to index into action[]
action_index = user_choice - 1

print(f"What would you like to {action[action_index]}?")
#get encrypt/decrypt string from user
user_input = get_user_input("INPUT: ")

#start encryption 
if action[0] == action[action_index]:

    #substitute each character in user input
    sub_text = basic_sp_network.substitute(user_input, 'ascii_characters', 'substitution_character')

    perm_text = basic_sp_network.permutate(sub_text)
    
    output = hex_ascii_converter.ascii_to_hex(perm_text)

else:
    #convert input from hex to ascii
    ascii_text = hex_ascii_converter.hex_to_ascii(user_input)
    print(ascii_text)
    #permutate ascii_text
    perm_text = basic_sp_network.permutate(ascii_text)
    print(perm_text)
    #reverse substutite premutated text
    output = basic_sp_network.substitute(perm_text, 'substitution_character', 'ascii_characters')


print(output)

"""
#functions to loop thorugh
functions = [basic_sp_network.substitute, basic_sp_network.permutate, hex_ascii_converter.ascii_to_hex]

#hold user_input as it is changed
dynamic_value = user_input

#check if encryptin
if action[0] == action[action_index]:
    #loop thorugh functions for encryption
    for function in functions:
        print(function)
        dynamic_value = function(dynamic_value, action_index)

#else decrypt
else:
    #reverse loop for decryption
    for function in reversed(functions):
        print(function)
        dynamic_value = function(dynamic_value, action_index)

print(dynamic_value)
"""