from PIL import Image

im                = Image.open("") # put your image path here
im_width          = im.width
im_height         = im.height
raw_pixels_lines  = list(im.getdata()) 
pixels_lines      = [[]]
r_brightness_coef = 0.3
g_brightness_coef = 0.6
b_brightness_coef = 0.1
max_brightness    = 255.0      # 255*r_brightness_coef + 255*g_brightness_coef + 255*b_brightness_coef
ascii_white_starting_at  = 200 # points to program from what pixel brightness to start adding emptyspaces 
ascii_characters  = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft//|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ascii_characters_asociative = []
ascii_lines = [[]]


def lines_create():                   # puts raw pixel data in order (required)

	itr = 0 
	for x in range(im_height):
		pixels_lines.append([])
		for xx in range(im_width):
			pixels_lines[x].append(raw_pixels_lines[itr])
			itr = itr + 1
	pixels_lines.pop(-1)		

def create_list():                    # puts characters with their relative brightness edge into a list (required)
	char_value = (255.0 - (255.0 - ascii_white_starting_at))/69.0
	for x in range(len(ascii_characters)-1):

		ascii_characters_asociative.append([round((char_value * (x+1)),1), ascii_characters[x]])

	ascii_characters_asociative.append([255.0,' '])

def draw_ascii():                     # returns ascii art from image
	string = ''

	for x in pixels_lines:
		for xx in x:
			brightness = xx[0]*r_brightness_coef + xx[1]*g_brightness_coef + xx[2]*b_brightness_coef
			for xxx in ascii_characters_asociative:
				is_over = False
				if brightness <= xxx[0]:
					string = string + xxx[1]
					is_over = True

				if is_over:
					break

		string = string + "\n"
	print(len(string))
	return string

def put_ascii_in_lines(ascii_string): # required to intitialise make_dwarwen() because draw_ascii() returns a single string
	ascii_lines.append([])
	i=0
	for x in range (len(ascii_string)):
		ascii_lines[i].append(ascii_string[x])
		if ascii_string[x] == '\n':
			i = i+1
			ascii_lines.append([])

	ascii_lines.pop(-1)
	ascii_lines.pop(-1)

def make_dwarwen():                   # deletes every second ascii line to make result better fit into screen, and returns string(makes sense only when width/height ~~ 1) (optional)
	string = ''
	del ascii_lines[::2]

	for x in ascii_lines:
		for xx in x:
			string = string + xx

	return string




# lines_create()
# create_list()
# print(draw_ascii())