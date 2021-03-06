import time

def substitute(user_input, first_string, second_string):

    #define ascii characters
    ascii_characters = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
    #define substutied ascii characters
    substitution_character = ",%e'O1}(9#s!QW.@{lv/E<gA)wuU\"jH3$4D:ItK?\\26ZLR`f&GkyoXbP[ThdYn;+_-Bam^]Cc>~NS8zVM57J|r=*x0ipFq"

    #assign empty list to record substutited text
    sub_return_str = ""

    for input_char in user_input:
        for i in range(len(ascii_characters)):
            if input_char == first_string[i]:
                sub_return_str += second_string[i]
                break

    """#cycle thorugh user input to find match in ascii_table, when found append sub_return_list with item from sub_table
    for input_char in user_input:
        for count, ascii_char in enumerate(first_string):
            if input_char == ascii_char:
                sub_return_str += second_string[count]
                break
    """
    return sub_return_str

def permutate(substituted_input): 

    per_return_str = ""

    for count, sub_char in enumerate(substituted_input):

        n = ord(substituted_input[count])
        n ^= ord('U')

        per_return_str += chr(n)

    return per_return_str
