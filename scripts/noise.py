import Image
from random import randint

def simple(image, variation): #Not to be confused with simplex noise
	if image.size[0] == image.size[1]: 
		size = image.size[0]
	else:
		return False

	image_pixels = image.load()

	for x in xrange(size):
		for y in xrange(size):
			r, g, b = image_pixels[x, y]
			col = randint(-variation, variation)
			image_pixels[x, y] = (r + col, g + col, b + col)

	return image