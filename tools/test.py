from os import path
from PIL import Image

folder = path.dirname(__file__)
filepath = path.join(folder, 'bin/test.jpg')

print(filepath)

img = Image.open(filepath)
print(img)
img.show()
