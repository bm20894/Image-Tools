from PIL import Image

def cycle(a, right=True):
	a.append(a.pop(0))
	if not right:
		a.append(a.pop(0))
	return a

def shift(img, right=True):
	pix = img.load()
	width, height = img.size
	for x in range(width):
		for y in range(height):
			pix[x, y] = tuple(cycle(list(pix[x, y]), right=right))
	return img
