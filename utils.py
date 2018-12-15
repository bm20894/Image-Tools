'''
Util package for main.py
'''
import sys
from termcolor import cprint
from tools import blur 

def error(msg):
	cprint(msg, 'red')
	sys.exit()

def transform(tool):
	'''@return: function to execute on Image object'''
	trans = {
		'blur': lambda img: blur(img)
	}

	if tool in trans:
		return trans[tool]
	return error('Tool {} not found.'.format(tool))
