
hex_map = [['0', 0], ['1', 1], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['1', 10], ['b', 11], ['c', 12], ['d', 13], ['e', 14], ['f', 15]]

perm_text = "this string"

def convert_ascii_value(value):

	hex_convertion = ""

	#shift the bits in position 5-8 to positions 1 - 4, disgard origonal values
	temp = value >> 4
	print(f"temp - {temp}")

	#change the first bits in position 5 - 8 to zero
	temp_2 = value & ~(0b11110000)

	#loop through hex map, match ascii_values and convert to hex
	for count, item in enumerate(hex_map):
		if temp == hex_map[count][1]:
			hex_convertion += hex_map[count][0]
			

		if temp_2 == hex_map[count][1]:
			hex_convertion += hex_map[count][0]
			break
	
	return hex_convertion


def ascii_to_hex(perm_text):

	output = ""

	for item in perm_text:
		converted = convert_ascii_value(ord(item))
		output += converted

	return output

def hex_to_ascii(hex_string):

	output = []
	
	i = 0

	#loop through pairs of characters in hex string
	for item in list(hex_string):
		#convert two hex characters into a single ASCII character
		output.append(convert_hex_pair(hex_string[i], hex_string[i + 1]))

		i += 2

def convert_hex_pair(hex_1, hex_2):

	#loop through hex_map
	#ßfor item, count in enumerate(hex_map):

	for i in range(len(hex_map)):

		if hex_1.lower() == hex_map[i][0]:
			hex_1 = hex_map[i][1]
		
		if hex_2.lower() == hex_map[i][0]:
			hex_2 = hex_map[i][1]

		temp = hex_1 << 4
		temp += hex_2

		print(f"temp {temp}")
		return temp 

"""
def hex_to_ascii_to_hex(user_input, action):

	if action == 'encrypt':
		value = ascii_to_hex(user_input)
		return value

	else:
		value = hex_to_ascii(user_input)
		return value
#srz, ABFKQVWX
"""