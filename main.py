import Image, ImageDraw
import sys
from random import randrange

args = sys.argv[1:]
variation = 3

gradient_im = Image.open("gradient.png").convert("RGB")
heightmap = Image.open(args[0]).convert("RGB")
draw = ImageDraw.Draw(heightmap)

#magic_number is basiclly x in x(255 + 255 + 255) = (image_width)
magic_number = float(gradient_im.size[0])/float(255 + 255 + 255)
gradient_colors = []

def get_height(color):
    r, g, b = color
    return int(magic_number * (r + b + g)) #Here we multiply the sum of rgb colors of a pixel
                                           #with magic_number and floor it

def noise(img):
    for x in xrange(img.size[0]):
        for y in xrange(img.size[1]):
            r, g, b = img.getpixel((x, y))
            draw.point((x, y), fill = (r+randrange(-variation, variation), g+randrange(0, variation), b+randrange(0, variation)))

for x in xrange(gradient_im.size[0]):
    r, g, b = gradient_im.getpixel((x, 0))
    gradient_colors.append((r, g, b)) #we add colors from the gradient.png to a
                                      #list with tuples containing rbg values 

for x in xrange(heightmap.size[0]):
    for y in xrange(heightmap.size[1]):
        r, g, b = heightmap.getpixel((x, y))
        draw.point((x, y), fill = gradient_colors[get_height((r, g, b))]) #get_height returns a variable which
                                                                          #used with gradient_colors  

if "-noise" in args:
    noise(heightmap)

del draw
heightmap.save("colormap.bmp", "bmp")
