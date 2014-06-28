import Image
import argparse
import methods
import noise

BLACK = (0, 0, 0)

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', type=str, help="a specific name for the colormap ('colormap' is used by default)")
parser.add_argument('-g', '--gradient', type=str, help="name of the gradient file")
parser.add_argument('-n', '--noise', type=int, choices=range(1, 11), help="add a bit of variation to the colors of the colormap")
parser.add_argument("heightmap", help="location of the heightmap image")
args = parser.parse_args()

print args.heightmap

def main():
	if args.gradient:
		gradient = Image.open(args.gradient).convert("RGB")
	else:
		gradient = Image.open("gradient.png").convert("RGB")
	
	if gradient.size[1] != 1:
		print "[Error] Invalid gradient image"
		return
	heightmap = Image.open(args.heightmap).convert("RGB")
	colormap  = Image.new("RGB", (heightmap.size[0], heightmap.size[1]))

	heightmap_pixels = heightmap.load()
	colormap_pixels  = colormap.load()
	gradient_colors  = methods.read_gradient(gradient)

	for x in xrange(heightmap.size[0]):
		for y in xrange(heightmap.size[1]):
			if heightmap_pixels[x, y] != BLACK:
				colormap_pixels[x, y] = gradient_colors[ methods.get_height(heightmap_pixels[x, y], gradient.size[0]) ]
			else:
				colormap_pixels[x, y] = gradient_colors[0]

	if args.noise:
		noise.simple(colormap, args.noise)

	if args.output:
		colormap.save(args.output + ".bmp", "bmp")
	else:
		colormap.save("colormap.bmp", "bmp")

if __name__ == "__main__":
	main()