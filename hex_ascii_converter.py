
hex_map = [['0', 0], ['1', 1], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['10', 10], ['b', 11], ['c', 12], ['d', 13], ['e', 14], ['f', 15]]

perm_text = "this string"

def convert_ascii_value(value):


	#shift the bits in position 5-8 to positions 1 - 4, disgard origonal values
	temp = value >> 4
	#change the first bits in position 5 - 8 to zero
	temp_2 = value & ~(0b11110000)
	
	#loop through hex map, match ascii_values and convert to hex
	for count, item in enumerate(hex_map):
		
		if temp == hex_map[count][1]:
			value_1 = hex_map[count][0]
			
		if temp_2 == hex_map[count][1]:
			value_2 = hex_map[count][0]
	
	hex_convertion = value_1
	hex_convertion += value_2

	return hex_convertion


def ascii_to_hex(perm_text):

	output = ""

	for item in perm_text:
		converted = convert_ascii_value(ord(item))
		output += converted

	return output

def hex_to_ascii(hex_string):

	output = []
	
	for i in range(0, len(hex_string) - 1, 2):
		output.append(chr(convert_hex_pair(hex_string[i], hex_string[i + 1])))

	#convert array to string 
	output_str = ''.join(output)

	return output_str

def convert_hex_pair(hex_1, hex_2):

	print(hex_1, hex_2)
	
	temp = 0
	#loop through hex_map
	for i in range(len(hex_map)):

		#match with hex_char and left shift 
		if hex_1.lower() == hex_map[i][0]:
			#print("here")
			temp = hex_map[i][1] << 4
			print("temp",temp)
		
		if hex_2.lower() == hex_map[i][0]:
			print("hex_2", hex_2)
			temp += hex_map[i][1]
	
	print("return",temp)
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