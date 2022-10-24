import sys
import numpy
from PIL import Image

def convert_rgb_to_ascii(pixel):
	density = " .:-=+*#%@"
	index = int(sum(pixel)/len(pixel))
	new_index = int((index/256)*len(density)-1)
	return density[new_index]*2

def convert_image(numpy_array, compression):
	"""
	converts image to ascii art
	:param image: the path to the image
	:type image: str
	:return: the ascii image
	:rtype: str
	"""
	numpy_array = numpy_array[::compression, ::compression]
	height = int(len(numpy_array))
	width = int(len(numpy_array[0]))
	ascii_art = ''
	for j in range(height):
		for i in range(width):
			ascii_art += convert_rgb_to_ascii(numpy_array[j][i])
		ascii_art += ('\n')

	return ascii_art