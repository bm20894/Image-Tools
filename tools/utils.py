'''
Util package for main.py
'''
import sys
from termcolor import cprint
from . import blur, shift, color_vis, gray, thermal

def error(msg):
	cprint(msg, 'red')
	sys.exit()

def transform(tool):
	'''@return: function to execute on Image object'''
	trans = {
		'blur': lambda img: blur(img),
		'shift': lambda img: shift(img),
		'lshift': lambda img: shift(img, right=False),
		'gray': lambda img: gray(img),
		'thermal': lambda img: thermal(img),
	}

	if tool in trans:
		return trans[tool]
	return error('Tool {} not found.'.format(tool))

def visualize_text(txtfile):
	with open(txtfile) as f:
		data = f.read()
	data = data.replace('.', '')
	return color_vis(data)
