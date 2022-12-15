import main
import test_backend as test

def get_color_from_file(filepath,expected):
	avg = main.get_color_from_file(filepath).get_hex_display()
	test.assert_equals(avg,expected)


get_color_from_file("images/purplesquare.png","#800080")
get_color_from_file("images/half.png","#7D7D7D")
get_color_from_file("images/cropsky.png","#838056")
get_color_from_file("images/peach.png","#FF9E5E")
get_color_from_file("images/flower.jpg","#838056")




def average_colour():
	chosen_colours = main.Colour_list([])
	chosen_colours.colours.extend([main.Colour("ffffff"),main.Colour("ff000000")])
	average_colour = chosen_colours.find_average_colour()
	test.assert_equals(average_colour.get_hex_display(),"#FF8080")
average_colour()