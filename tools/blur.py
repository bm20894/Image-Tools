from PIL import ImageFilter
from os import path

def blur(img, radius=3):
	im1 = img.filter(ImageFilter.BLUR)
	im2 = img.filter(ImageFilter.GaussianBlur(radius=radius))

	return im2
