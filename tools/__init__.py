import Polytools
import os
def poly(img):
    if(img.size[0]*img.size[1])>10000:
        while(True):
            inp=input("Large images can take long to process. Continue? (y/n)")
            if inp=='y':
                print("Continuing.")
                break
            elif inp=='n':
                print("Exiting tool.")
                return
            else:
                print('y or n')
    Polytools.runTracker(img)
    Polytools.alter(img)
    return Polytools.polyImage(img)
def gray(img):
    return img.convert('LA')
    #convert('LA') puts it in black and white, but for use in some other functions there must be three bands
def testPoly():
	from PIL import Image 
	from os import path
	folder = path.dirname(__file__)
	filepath = path.join(folder, 'bin/test.jpg')
	img=gray(Image.open(filepath))
	img.show()
	poly(img)
testPoly()
