class Colour:
	hex_value: str
	rgb = []

	def __init__(self,hex_value):
		self.hex_value = hex_value
		self.set_rgb()


	def set_rgb(self):
		red = hex_to_dec(self.hex_value[:2])
		green = hex_to_dec(self.hex_value[2:4])
		blue = hex_to_dec(self.hex_value[4:])
		self.rgb = [red,green,blue]

	def get_rgb_display(self):
		rgb = self.rgb
		output = "rgb("

		for index,val in enumerate(rgb):
			if index != 2:
				output += str(val)+ ", "
			else:
				output += str(val)
		output += ")"
		return output
	
	def get_hex_display(self):
		output = "#" + self.hex_value
		return output


def hex_to_dec(hex_value):
	decimal_value = int(hex_value,16)
	return decimal_value
	
def dec_to_hex(decimal_value):
	return hex(round(decimal_value))[2:]


def rgb_to_hex(rgb):
	red = rgb[0]; green = rgb[1]; blue = rgb[2]

	hex_value = dec_to_hex(red) + dec_to_hex(green) + dec_to_hex(blue)

	return hex_value.upper()


class Colour_list:
	colours = []

	def __init__(self,colours):
		self.colours = colours
	
	def find_average_colour(self):
		total_red = 0; total_green = 0; total_blue = 0

		for colour in self.colours:
			total_red += colour.rgb[0]
			total_green += colour.rgb[1]
			total_blue += colour.rgb[2]
		
		average_colour_rgb = [total_red/len(self.colours), total_green/len(self.colours), total_blue/len(self.colours)]
		average_hex_value = rgb_to_hex(average_colour_rgb)
		average_colour = Colour(average_hex_value)
		return average_colour

	def get_hex_value(self):
		hex_value = input("Enter hex value to covert:\n#").upper()

		if not self.validate_hex(hex_value):
			print("invalid input, try again.")
			return self.get_hex_value()
		
		hex_value = hex_value.upper()
		return hex_value

	def validate_hex(self,hex_value):
		accepted_chars = ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]
		for character in hex_value:
			if character not in accepted_chars:
				return False
		return True

def main():
	chosen_colours = Colour_list([])

	for i in range(2):
		new_hex = chosen_colours.get_hex_value()
		new_colour = Colour(new_hex)
		chosen_colours.colours.append(new_colour)

	average_colour = chosen_colours.find_average_colour()
	print(average_colour.get_hex_display(), average_colour.get_rgb_display())
main()