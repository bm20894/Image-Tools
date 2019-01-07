"""A module for creating pointilistic art

Public Methods:

convert -- takes an image and makes it into dots, similar to Koalas to the max
"""
from PIL import Image, ImageDraw 

def partitionRandom(rect, cap):
    """Randomly breaks given rectangle into partitions

    Partitions are all square, and have a capped size in cap.
    rect is the dimension of the rectangle."""
    pass
def partitionEven(rect, mini,maxi, padding=0):
    """Breaks a rectangle into a grid partion.

    Note: Does not maintain rectangle sizes or proprtions exactly

    Returns a list of squares in the format (leftx,topy,dimension)

    Paramters:

    rect- the width and height of the rectangle being broken in the format (width, height)
    mini- the minimum dimension of the squares
    maxi - the maximum dimension of the squares"""
    #performs a linear search to which square size drops the least pixels in the range
    size=-1
    droppedPixels=rect[0]*rect[1]
    for i in range(mini,maxi):
        shortx=rect[0]%(i)
        shorty=rect[1]%(i)
        dropped=(rect[1]*shortx+rect[0]*shorty-shortx*shorty)
        if dropped<=droppedPixels:
            size=i
            droppedPixels=dropped
    partitions=[]
    for y in range(int(rect[1]/(size))):
        for x in range(int(rect[0]/(size))):
            partitions.append((size*x+int(padding/2), size*y+int(padding/2),size-padding))
    return partitions

def dominantColor(pixels):
    """Finds the median color in pixel

    Uses median instead of mean to prevent impure/boring shades."""
    col=[0,0,0]
    for i in range(len(pixels[0])):
        arr=[p[i] for p in pixels]
        arr.sort()
        col[i]=arr[int(len(arr)/2)]
    return tuple(col)    
def pointImageEven(image, mini, maxi, background=(255,255,255),elipse=True, padding=0):
    partition=partitionEven(image.size,mini,maxi,padding=padding)
    br=partition[-1]#bottom right box
    print(br)
    size=(br[0]+br[2]+padding,br[1]+br[2]+padding)
    mode=image.mode
    if len(background)==4:
        mode="RGBA"
    img=Image.new(mode,size,color=background)#new image
    imgdraw=ImageDraw.Draw(img)
    for b in partition:
            box=b[0],b[1],b[0]+b[2],b[1]+b[2]
            pixels=[]
            for x in range(box[0],box[2]):
                for y in range(box[1],box[3]):
                    pixels.append(image.getpixel((x,y)))
            col=tuple(i for i in dominantColor(pixels))
            if elipse:
                imgdraw.ellipse(box,fill=col)
            else:
                imgdraw.rectangle(box,fill=col)
    return img
def menu(img):
    """A method for accessing module methods through command prompt"""
    print("Welcome to Sphere Tools menu!")
    action=getVal("Do you wish to exit, build rectangle, or build sphere?\n",
        str,error="Im sorry, please enter 'exit', 'rectangle', or 'sphere'.",
        accepted=lambda val:(val.lower() in (('exit','rectangle','sphere'))))
    if action.lower()=='exit':
        return img
    bound1=getVal("Smallest region size?\n",int,error="Please enter an integer")
    bound2=getVal("Largest region size?\n",int,error="Please enter an integer")
    r=getVal("Background RGB R value?\n",int,error="Please enter an integer")
    g=getVal("Background RGB G value?\n",int,error="Please enter an integer")
    b=getVal("Background RGB B value?\n",int,error="Please enter an integer")
    padding=getVal("Spacing value?\n",int,error="Please enter an integer")
    print("Calculating...")
    imNew=pointImageEven(img,min(bound1,bound2),max(bound1,bound2),background=((r,g,b)),elipse=(action.lower()=='sphere'),padding=padding)
    print("Done.")
    return imNew
def getVal(message,valClass,error="Im sorry, I didn't understand that.", accepted=lambda inp:True):
    val=None
    while val==None:
        inp=input(message)
        try:
            inp=valClass(inp)
            if accepted(inp):
                val=inp
        except:
            pass
        if val==None:
            print(error)
    return val

def test():
    menu(Image.open("tools/bin/toucan.jpg")).save("tools/bin/temporarysave.jpg")
    Image.open("tools/bin/temporarysave.jpg").show()
test()