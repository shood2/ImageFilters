from PIL import Image, ImageDraw, ImageFont


################################
###### Image Loading ###########
################################

#takes a filename
#returns an image type

def load_img(filename):
	img = Image.open(filename)
	return img

#takes an image type
#displays image

def show_img(im):
	im.show()

#takes image type and a filename
#saves image to filename

def save_img(im, filename):
	im.save(filename, "jpeg")
	show_img(im)

#takes an image and pixel list
#returns new image from pixels of size image

def list_to_image(im, new_pixels):
	newim = Image.new("RGB", im.size)
	newim.putdata(new_pixels)
	return newim

def write_words(image, word):
	image = expand_image(image)
	draw = ImageDraw.Draw(image)
	width = image.size[0] - 20
	height = image.size[1] - int(image.size[1] / 1.45)

	font = ImageFont.truetype("GROBOLD.ttf", 800)
	fontsize = 800
	while(font.getsize(word)[0] > width):
		fontsize -= 1
		font = ImageFont.truetype("GROBOLD.ttf", fontsize)

	draw.text((10, (int(image.size[1] / 1.4) + int(0.15 * font.getsize(word)[1]))), word, font=font)
	return image

def expand_image(im):
	newim = Image.new("RGB", (im.size[0], im.size[1] + int(0.30*im.size[1])))
	newim.putdata(im.getdata())
	return newim

################################
###     Helper Functions     ###
################################

def average(tup):
	sum1 = 0
	for p in tup:
		sum1 += p
	return int(sum1/3)

def setAll(val):
	tup = tuple((val, val, val))
	return tup

def get_user_info(filter_info):
	f = input("What file would you like to filter?")
	#print(filename)
	if(not("jpeg" in f) and not("png" in f) and not("jpg" in f)):
		print("Error: Incorrect file format")
		exit()
	else:
		im = load_img(f)

	print("Here is your image!")
	show_img(im)

	print("Would you like to add some text?")
	answer = input(" ")
	if('y' in answer):
		display_text = input("What do you want it to say?")
		im = write_words(im, display_text)

		print("This is your new image, let's add a filter!")
		show_img(im)

	print("###   Filter Types to Choose From    ###")

	for f1 in filter_info:
		print(f1)

	filter_type = input("What filter would you like to apply?")
	newim = Image.new("RGB", im.size)

	if("all" in filter_type.lower() and "black" in filter_type.lower()):
		newim = allBlack(im)
		show_img(newim)
	elif("black" in filter_type.lower() and "white" in filter_type.lower()):
		newim = black_and_white(im)
		show_img(newim)
	elif("invert" in filter_type.lower()):
		newim = invert_image(im)
		show_img(newim)
	elif("reduce" in filter_type.lower() and "red" in filter_type.lower()):
		newim = reduce_redness(im)
		show_img(newim)
	elif("sepia" in filter_type.lower()):
		newim = sepia(im)
		show_img(newim)
	elif("NU" in filter_type.upper()):
		newim = NUCon(im)
		show_img(newim)
	else:
		print("Error: unfortunately, we do not have that filter avaliable right now")

	save = input("Would you like to save your creation? \n")
	if("y" in save.lower()):
		save_img(newim, "new_image.jpeg")


################################
####       Filters         #####
################################
filter_info = ["All Black - a filter that takes an image and returns a black image of the same size", "Black and White - a filter that takes an image and turns it grey scale", "Invert - a filter that takes an image and inverts all the colors", "Reduce Redness - a filter that reduces the redness in a picture by 25%", "Sepia - a filter that increases the yellow present in an image", "NU - a filter that takes an image and returns a purple verion of it"]


def allBlack(im):
	pixels = im.getdata()
	new_pixels = []

	black = (0,0,0)

	new_pixels.append(black)
	return list_to_image(im, new_pixels)

def black_and_white(im):
	pixels = im.getdata()
	new_pixels = []

	for p in pixels:
		new_pixels.append(tuple((average(p), average(p), average(p))))

	return list_to_image(im, new_pixels)

def invert_image(im):
	pixels = im.getdata()
	new_pixels = []

	for p in pixels:
		new_pixels.append(tuple((255-p[0], 255-p[1], 255-p[2])))

	return list_to_image(im, new_pixels)

def reduce_redness(im):
	pixels = im.getdata()
	new_pixels = []

	for p in pixels:
		new_pixels.append(tuple((int(p[0] * 0.25), p[1], p[2])))

	return list_to_image(im, new_pixels)

def sepia(im):
	pixels = im.getdata()
	new_pixels = []

	yellow = tuple((-5, -5, -100))
	for p in pixels:
		new_pixels.append(tuple((p[0] + yellow[0], p[1] + yellow[1], p[2] + yellow[2])))

	return list_to_image(im, new_pixels)

def NUCon(im):
	pixels = im.getdata()
	new_pixels = []

	dark_purple = (30, 0, 30)
	mid_dark_purple = (70, 0, 70)
	mid_purple = (130, 0, 130)
	mid_light_purple = (200, 0, 200)
	light_purple = (255, 255, 255)

	for p in pixels:
		intensity = p[0] + p[1] + p[2]
		if(intensity < 153):
			new_pixels.append(dark_purple)
		elif(intensity < 306):
			new_pixels.append(mid_dark_purple)
		elif(intensity < 459):
			new_pixels.append(mid_purple)
		elif(intensity < 612):
			new_pixels.append(mid_light_purple)
		else:
			new_pixels.append(light_purple)

	return list_to_image(im, new_pixels)

################################
		 # main #
################################

def main():
	get_user_info(filter_info)

#	im = load_img("n.png")
#	nim = expand_image(im)
	#show_img(im)
	#nim2 = NUCon(im)
	#show_img(nim2)
#	write_words(nim, "Kitty 2020")
#	nim2 = NUCon(nim)
#	show_img(nim2)
	#while(True):
	#	x = 1

main()
