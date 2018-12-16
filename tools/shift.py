from PIL import Image

def cycle(a):
	a.append(a.pop(0))
	return a

def shift(img):
	pix = img.load()
	width, height = img.size
	for x in range(width):
		for y in range(height):
			pix[x, y] = tuple(cycle(list(pix[x, y])))
	return img
