import Image

def get_height(color, size):
    r, g, b = color
    return int(((r + g + b) * size) / 765.0)

def read_gradient(image):
 	colors = []
 	if image.size[1] == 1:
 		image_pixels = image.load()

 		for x in xrange(image.size[0]):
 			colors.append( image_pixels[x, 0] )

 	else:
 		return False

 	return colors