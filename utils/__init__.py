'''
Util package for main.py
'''
import sys
from termcolor import cprint
import tools

def error(msg):
	cprint(msg, 'red')
	sys.exit()

def transform(tool):
	'''@return: function to execute on Image object'''
	return lambda img: img.show()
