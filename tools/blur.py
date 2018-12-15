from PIL import ImageFilter
from os import path

def blur(img, radius=3):
	''' @params an Image object, and an optional radius kwarg for the Guassian Blur.
		@return the transformed Image object, with the applied Gaussian Blur.'''
	im1 = img.filter(ImageFilter.BLUR)
	im2 = img.filter(ImageFilter.GaussianBlur(radius=radius))

	return im2
