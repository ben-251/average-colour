import random
import colorama

def get_random_message(state):
	happy_choices = ["niceeeee!", "good job!!", "yassssssssssss!", "LETS GOOOOO!", "whoop whoop!"]
	sad_choices = ["oooops,","arghh oh well,","something's not quite right","uhhhhhh","ummmmmmm","hmmmmm..","uhh... sure?"]
	if state == "pass":
		choice = random.choice(happy_choices)
	elif state == "fail":
		choice = random.choice(sad_choices)
	else:
		raise Exception("????????")
	return choice

def get_colour(state):
	if state == "fail":
		colour = colorama.Fore.RED
	elif state == "pass":
		colour = colorama.Fore.GREEN
	return colour
	
def display_message(state, actual, expected):
	random_celebration = get_random_message(state)
	colour = get_colour(state)
	clear = colorama.Fore.RESET
	green = colorama.Fore.GREEN
	print(f"{colour}{random_celebration}{clear}\nresult:{colour}\n{actual}{clear}\nexpected:\n{green}{expected}\n{clear}")

def assert_equals(actual,expected):
	if actual != expected:
		display_message("fail", actual, expected)
		exit()
	else:
		display_message("pass",actual, expected)
	return