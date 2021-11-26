
hex_map = [['0', 0], ['1', 1], ['2', 2], ['3', 3], ['4', 4], ['5', 5], ['6', 6], ['7', 7], ['8', 8], ['9', 9], ['1', 10], ['b', 11], ['c', 12], ['d', 13], ['e', 14], ['f', 15]]

perm_text = "this string"

def convert_ascii_value(value):

	hex_convertion = []

	#shift the bits in position 5-8 to positions 1 - 4, disgard origonal values
	temp = value >> 4
	#change the first bits in position 5 - 8 to zero
	temp_2 = value & ~(0b11110000)

	#loop through hex map, match ascii_values and convert to hex
	for item in hex_map:
		if temp == hex_map[item][0]:
			hex_convertion.append(hex_map[item][1])
			break
		if temp_2 == hex_map[item][1]:
			hex_convertion.append(hex_map[item][0])
			break
	return hex_convertion


def ascii_to_hex(perm_text):

	output = []

	i = 0

	for item in perm_text:
		converted = convert_ascii_value(ord(item))
		output.append(converted)
		i += 2

	return output
	""""
	#if string is odd pad with blank value (need to find a loop that will iterate by 2 and still read last item in odd string)
	even = bool(True)
	if len(perm_text) % 2 != 0:
		even = False
		perm_text += " "

	i = 0
	#iterate through perm_text, send values to converter in 2's
	while i < len(perm_text):
		output.append(convert_ascii_value(ord(perm_text[i]), ord(perm_text[i + 1])))
		i += 2
	"""