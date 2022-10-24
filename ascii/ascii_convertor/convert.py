import sys
import numpy
from tkinter import *
import tkinter as tk
from PIL import Image


def convert_rgb_to_ascii(pixel, inv):
	density = " .:-=+*#%@"
	if inv:
		density = density[::-1]
	index = int(sum(pixel)/len(pixel))
	new_index = int((index/256)*len(density)-1)
	return density[new_index]

def create_numpy_array(image_path, compression):
	img = Image.open(image_path)
	width, height = img.size
	new_width, new_height = int(width/compression), int(height/compression)
	img = img.resize((new_width, new_height), Image.Resampling.NEAREST)
	img = numpy.array(img)
	return (img,new_width,new_height)


def convert_image(image_path, compression, inv=False):
	"""
	converts image to ascii art
	:param image: the path to the image
	:type image: str
	:return: the ascii image
	:rtype: str
	"""
	img, width, height = create_numpy_array(image_path, compression)
	ascii_art = ''
	for j in range(height):
		for i in range(width):
			ascii_art += convert_rgb_to_ascii(img[j][i], inv)
		ascii_art += ('\n')

	return ascii_art

def show_ascii(text):
	# setting up window
	root = Tk()
	root.title("Ascii.py")
	# setting up text widget
	T = Text(root, height=1920, width=1080, font=('Monocode', 1), bg="black", fg="white")
	T.pack()
	# inserting text
	T.insert("0.0", text)
	T.mainloop()


def main():
	args = sys.argv[1:]
	args = ["--todir", "examples/daniel.jpeg", 4]
	
	if not args:
		print('usage: [--todir] picture compression -inv')
		sys.exit(1)

	todir = ''
	if args[0] == '--todir':
		todir = args[0]
		filename = args[1]
		compression = args[2]
		inv = "-inv" == args[-1]	

	if todir:
		ascii_art = convert_image(filename, compression, inv)
		show_ascii(ascii_art)
		


if __name__=="__main__":
	main()