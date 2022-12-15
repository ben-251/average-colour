from PIL import Image

input_image = Image.open("test_image2.png")

pixel_map = input_image.load()

width, height = input_image.size
test = input_image.getpixel((1,2))
# taking half of the width:
for i in range(width//2):
	for j in range(height):
		# getting the RGB pixel value.
		r, g, b, random_other_value_i_dont_understand = input_image.getpixel((i, j))

		# Apply formula of grayscale:
		grayscale = (0*r + 0*g + 0*b)

		# setting the pixel value.
		pixel_map[i, j] = (int(grayscale), int(grayscale), int(grayscale))

		# Saving the final output
		# as "grayscale.png":
		input_image.save("grayscale.png", format="png")

input_image.show()		# output screen.`