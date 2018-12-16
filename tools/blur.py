from PIL import ImageFilter
from os import path

def blur(img, radius=3):
	''' @params an Image object, and an optional radius kwarg for the Guassian Blur.
		@return the transformed Image object, with the applied Gaussian Blur.'''
	return img.filter(ImageFilter.GaussianBlur(radius=radius))
