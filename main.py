'''
Programmer: Miles Boswell
main.py

Take user input from cli (image file, tool to apply on image)
Display original image and transformed image side by side in window
Optional: overwrite image file with transformation
'''
import sys
from matplotlib import pyplot as plt
from PIL import Image
from utils import error, transform

def user_input():
	''' @return: dictionary with Image object as 'img',
				 file of Image as 'file', and optional tool
				 to apply '''
	if len(sys.argv) > 1:
		sys.argv.pop(0)
		data = {}
		if '-t' in sys.argv:
			tool_index = sys.argv.index('-t') + 1
			tool = sys.argv.pop(tool_index)
			data['tool'] = tool
			sys.argv.pop(tool_index - 1)
		elif '-ts' in sys.argv:
			tool_index = sys.argv.index('-ts') + 1
			tool = sys.argv.pop(tool_index)
			data['tool'] = tool
			sys.argv.pop(tool_index - 1)
			data['save'] = True
		image_file = sys.argv[0]

		try:
			img = Image.open(image_file)
		except:
			error('Could not find file: {}'.format(image_file))
		else:
			data['img'], data['file'] = img, image_file
		return data
	else:
		error('You must specify an image file.')

if __name__ == '__main__':
	data = user_input()
	# if a tool is specified, apply it to the Image and display
	img, tool = data.get('img'), data.get('tool', None)
	fileloc = data.get('file')
	save = data.get('save', False)
	if tool:
		trans = transform(tool)
		newimg = trans(img)
		newimg.show()
		if save:
			newimg.save(fileloc)
	else:
		img.show()
