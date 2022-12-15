from PIL import Image


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
	hex_value = hex(round(decimal_value))[2:]
	if len(hex_value) == 1:
		return hex_value+hex_value
	return hex_value


def rgb_to_hex(rgb):
	red = rgb[0]; green = rgb[1]; blue = rgb[2]

	hex_value = dec_to_hex(red) + dec_to_hex(green) + dec_to_hex(blue)

	return hex_value.upper()


class Colour_list():
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

def get_pixel_hexs(filepath):
	hexs = []
	input_image = Image.open(filepath)
	pixel_map = input_image.load()

	width, height = input_image.size
	for i in range(width):
		for j in range(height):
			color = input_image.getpixel((i, j))
			r,g,b = color[0],color[1],color[2]
			hexs.append(rgb_to_hex((r,g,b)))
	return hexs


def get_color_from_file(filepath):
	pixels = Colour_list([])
	pixel_hex_values = get_pixel_hexs(filepath)
	for index, pixel_hex in enumerate(pixel_hex_values):
		pixels.colours.append(Colour(pixel_hex))

	avg = pixels.find_average_colour()
	return avg
