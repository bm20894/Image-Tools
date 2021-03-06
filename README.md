# 1-4 Performace Task
### Client 4: Developer

## Installation
To use, `$ pip install Toucan-Tools`. From there, all of the command-line tools will be available for use anywhere on your machine.

## Usage 
A main script (run from terminal) processes an image with a library of image tools. To run: `$ toucan imagefile.jpg -t blur`. This will display a window showing the image with the applied tool.

### Tools to start out with
* Grayscale Coloring 
* Circle/polygon Packing
* Thermal Coloring
* Number Visualization (colored mosaic)

### Conventions
All transformation tools are located somewhere in the tools package, and can all be called on from the root of the package. To follow the zen of python package structure: the less dots the better.

### Egan's Tasks
* [x] Polygon Packing
	1. Function Name: `poly(image)`
	1. Clean Up Code and optimize
	1. Improve Smoothing
* [x] Grayscale Coloring
	* Function Name: `gray(image)`
	* Usage: `$ toucan tools/bin/toucan.jpg -t gray`
	* Original vs Gray:

		![toucan](tools/bin/toucan.jpg) ![toucan gray](tools/bin/toucan_gray.jpg)

* [x] Thermal Coloring
	* Function Name: `thermal(image)`
	* Usage: `$ toucan tools/bin/toucan.jpg -t thermal`
	* Thermal toucan.jpg:

		![toucan thermal](tools/bin/toucan_thermal.jpg)

### Miles's Tasks
* [x] Create Package Structure
* [x] main.py file
	1. [x] Takes user input (image file, tool to apply)
	1. [x] Displays output of applied tool
	1. [x] If user wants to overwrite the image file to be transformed, overwrite the file.
* [x] Blur
	* Function name: `blur(image)`
	* Usage: `$ toucan tools/bin/toucan.jpg -t blur`
	* Blur toucan.jpg:
		
		![toucan blur](tools/bin/toucan_blur.jpg)

* [x] Color Shifting
	* Function name: `shift(image)`
	* Shift RGB values one to the left (Red values become Blue, Green becomes Red, Blue becomes Green), or right.
	* Usage: `$ toucan tools/bin/toucan.jpg -t shift`
	* Shift vs LShift:

		![toucan shift](tools/bin/toucan_shift.jpg) ![toucan lshift](tools/bin/toucan_lshift.jpg)

* [x] Number Mosaic
	* Function name: `color_vis(digits)`
	* Read digits from a text file, and return a mosaic of each number represented by a rectangle with an assigned color.
	* Usage: `$ toucan tools/bin/pi_100.txt`
	* Example: first 100 digits of pi

		![pi_100](tools/bin/vis_pi_100.jpg)
