import Image, ImageDraw
import sys

args = sys.argv[1:]

gradient_im = Image.open("gradient.png")
gradient_im = gradient_im.convert("RGB")

heightmap = Image.open(args[0])
heightmap = heightmap.convert("RGB")
draw = ImageDraw.Draw(heightmap)


magic_number = float(gradient_im.size[0])/float(255 + 255 + 255)
gradient_colors = []

def get_height(color):
    r, g, b = color
    return int(magic_number * (r + b + g))

for x in range(gradient_im.size[0]):
    r, g, b = gradient_im.getpixel((x, 0))
    gradient_colors.append((r, g, b))

print gradient_colors

for x in range(heightmap.size[0]):
    for y in range(heightmap.size[1]):
        r, g, b = heightmap.getpixel((x, y))
        draw.point((x, y), fill = gradient_colors[get_height((r, g, b))])

del draw
heightmap.save("colormap.bmp", "bmp")
