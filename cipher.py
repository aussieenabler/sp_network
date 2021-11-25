
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
    sub_text = basic_sp_network.substitute(user_input, action_index)
    
    perm_text = basic_sp_network.permutate(sub_text)

print(perm_text)