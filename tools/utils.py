'''
Programmer: Miles Boswell

Util package for main script
'''
import sys
from . import blur, shift, color_vis, gray, thermal,spheres

def error(msg):
	print(msg)
	sys.exit()

def transform(tool):
	'''@return: function to execute on Image object'''
	trans = {
		'blur': lambda img: blur(img),
		'shift': lambda img: shift(img),
		'lshift': lambda img: shift(img, right=False),
		'gray': lambda img: gray(img),
		'thermal': lambda img: thermal(img),
		'sphere': lambda img: spheres.menu(img),
	}

	if tool in trans:
		return trans[tool]
	return error('Tool {} not found.'.format(tool))

def visualize_text(txtfile):
	with open(txtfile) as f:
		data = f.read()
	data = data.replace('.', '')
	return color_vis(data)
