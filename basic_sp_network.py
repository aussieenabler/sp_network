import time

def substitute(user_input, action_index):

    
    ascii_characters = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    substitution_characters = ",%e'O1}(9#s!QW.@{lv/E<gA)wuU\"jH3$4D:ItK?\\26ZLR`f&GkyoXbP[ThdYn;+_-Bam^]Cc>~NS8zVM57J|r=*x0ipFq"


    #assign empty list to record substutited text
    sub_return_str = ""

    #cycle thorugh user input to find match in ascii_table, when found append sub_return_list with item from sub_table
    for input_char in user_input:
        for count, ascii_char in enumerate(ascii_characters):
            if input_char == ascii_char:
                sub_return_str += substitution_characters[count]
                break 

    return sub_return_str

def permutate(substituted_input, action_index): 

    per_return_str = ""

    for count, sub_char in enumerate(substituted_input):

        n = ord(substituted_input[count])
        n ^= ord('U')

        per_return_str += chr(n)


    return per_return_str
