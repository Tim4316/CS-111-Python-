#
# ps7pr3.py  (Problem Set 7, Problem 3)
#
# Images as 2-D lists  
#
# Computer Science 111
# 

from hmcpng import load_pixels
from hmcpng import save_pixels
from hmcpng import compare_images

def create_green_image(height, width):
    """ creates and returns a 2-D list of pixels with height rows and
        width columns in which all of the pixels are colored green.
        inputs: height and width are non-negative integers
    """
    pixels = []

    for r in range(height):
        row = [[0, 255, 0]] * width
        pixels += [row]

    return pixels

def brightness(pixel):
    """ takes a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    return (21*red + 72*green + 7*blue) // 100

def grayscale(pixels):
    """ returns a new 2-D list of pixels for an image that is a grayscale
        version of the original image """
    height = len(pixels)
    width = len(pixels[0])
    image = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            grey = brightness(pixels[r][c])
            image[r][c] = [grey, grey, grey]
    return image

def mirror_vert(pixels):
    """ returns a new 2-D list of pixels for an image in which the original 
        image is “mirrored” vertically """
    height = len(pixels)
    width = len(pixels[0])
    image = create_green_image(height, width)
     
    for r in range(height):
         for c in range(width):
            if r < (height) // 2:
                 image[r][c] = pixels[r][c]
            else:
                image[r][c] = pixels[height - r - 1][c]
    return image

def flip_horiz(pixels):
    """ returns a new 2-D list of pixels for an image in which the original 
        image is “flipped” horizontally """
    height = len(pixels)
    width = len(pixels[0])
    image = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            image[r][c] = pixels[r][width - c - 1]
    return image

def extract(pixels, rmin, rmax, cmin, cmax):
    """ returns a new 2-D list that represents the portion of the original 
        image that is specified by the other four parameters """
    height = rmax - rmin
    width = cmax - cmin
    image = create_green_image(height, width)
    
    for r in range(height):
        for c in range(width):
            image[r][c] = pixels[rmin + r][cmin + c]
    return image
            
    
    
             
             
         
                
