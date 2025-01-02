# warmupgram_func.py
# This program applies two filters to an image (grayscale and vertflip). 
# It's currently incomplete.

import picture


def copy(image):
    """
    Returns an exact copy of the provided image.
    
    Inputs:
        image: an RGB image, loaded via the picture module
    
    Outputs:
        imagecopy: a new image that is a copy of the inputed image.
    """
    # Get the image dimensions
    width = picture.image_width(image)
    height = picture.image_height(image)
    
    # Create a blank image to hold our copied pixel values
    imagecopy = picture.blank_image(width, height)


    for x in range(width):
        for y in range(height):
            red,green,blue = picture.get_pixel(image,x,y)
            val = 0
            picture.set_blue(imagecopy,x,y,blue)
            picture.set_red(imagecopy,x,y,red)
            picture.set_green(imagecopy,x,y,green)
            


            
    # Copy all the pixel values from image to imagecopy
    # Hints: What sequence(s) do you need for looping through all the pixels 
    # in image? What pixel values will you "get" and what pixel values will 
    # you "set"?
    
    # REPLACE THIS COMMENT WITH YOUR OWN CODE
    
    return imagecopy


def grayscale(image, width, height):
    """
    Converts an image into the grayscale version of the image (i.e. no color, 
    only shades of gray).

    Inputs:
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image

    Output:
        imagecopy: the grayscale version of the input image
    """
    # Before we apply our image filter, we'll use the copy() function to 
    # make a duplicate of the original image. The copy() function is defined
    # above, but the logic is incomplete. Take a minute now to fill in the code
    # needed to get it working.

    # Now that the copy() function is complete, we can use it to duplicate our 
    # image.
    imagecopy = copy(image)

    # Next, let's convert this entire copy to grayscale. We can do this by 
    for x in range(width):
        for y in range(height):
           red,green,blue = picture.get_pixel(image,x,y)
           val = (red + green + green)//3
           picture.set_blue(imagecopy,x,y,val)
           picture.set_red(imagecopy,x,y,val)
           picture.set_green(imagecopy,x,y,val)


    # looping through each of the pixels. For each pixel we will set its new 
    # color values to be the average of its RGB values. The pseudocode for 
    # this step is as follows:

    # for every pixel (x,y) in the image:
    #   1. get the red, green, and blue values
    #   2. compute the average of red, green, and blue
    #   3. set the color of the pixel in imagecopy to this average
    
    # REPLACE THIS COMMENT WITH YOUR OWN CODE
    return imagecopy


def vertflip(image, width, height):
    """
    Converts an image into the vertically flipped version of the image.
    
    Inputs:
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image
    
    Output:
        imagecopy: the vertically flipped version of the input image
    """

    # Again, use the copy() function you defined above to duplicate your image.
    imagecopy = copy(image)
    
    # We are now ready to vertically flip our image. The pseudocode for this 
    # step is as follows:

    # for every pixel (x,y) in imagecopy:
    #   1. get the red, green, and blue values from the original image
    # #   2. use these values to set the color of the appropriate pixel in imagecopy
    for x in range(width):
        for y in range(height):
            red,green,blue = picture.get_pixel(image,x,height-1-y)
            picture.set_blue(imagecopy,x,y,blue)
            picture.set_red(imagecopy,x,y,red)
            picture.set_green(imagecopy,x,y,green)

    
    # REPLACE THIS COMMENT WITH YOUR OWN CODE
    return imagecopy

def negative_filter(image, width, height):
        
        """
    Converts an image into the negative version of the image.
    
    Inputs:
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image
    
    Output:
        imageneg the negative version of the input image
    """
        imageneg = copy(image)

        for x in range(width):
            for y in range(height):
                red,green,blue = picture.get_pixel(image,x,y)
                picture.set_blue(imageneg,x,y,abs(blue - 255))
                picture.set_red(imageneg,x,y,abs(red-255))
                picture.set_green(imageneg,x,y,abs(green-255) )
        return imageneg



def horizontal_scroll_filter(image,width,height,shift):
    """This program asks the user for an input(“Number of pixels”)
Then shift the image that many pixels to the right
Inputs:
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image
    
    Output:
        imagecopy: the vertically flipped version of the input image  """
    width = picture.image_width(image)
    height = picture.image_height(image)
    
 
    imagecopy = picture.blank_image(width, height)
    
    for y in range(height):
     for x in range(width):
            new_x = (x + shift) % width 
            red, green, blue = picture.get_pixel(image, x, y)
            red, green, blue = picture.get_pixel(image, x, y)
            picture.set_pixel(imagecopy, new_x, y, red, green, blue)
    return imagecopy



def posterize(image,width,height):
    """This program posterize thee image 
    input
        image: an RGB image, loaded via the picture module
        width: the width of the image
        height: the height of the image
    
    Output:
        imagecopy: posterized image  """
    width = picture.image_width(image)
    height = picture.image_height(image)
    
 
    imagecopy = picture.blank_image(width, height)
    
    for y in range(height):
     for x in range(width):
        red,green,blue = picture.get_pixel(image,x,y)
        r = red //64
        b = blue //64
        g = green // 64
        picture.set_blue(imagecopy,x,y,64*b)
        picture.set_red(imagecopy,x,y,r*64)
        picture.set_green(imagecopy,x,y,g*64)
    return imagecopy

# def zoom(image,width,height):
#     """
#     """
#     width = picture.image_width(image)
#     height = picture.image_width(image)
#     new_width = width + 2
#     new_height = height + 2

#     imagecopy = picture.blank_image(width, height)
    
    
#     for y in range(height):
#      for x in range(width):
#             center_x = x+1
#             center_y = y+1
#             red, green, blue = picture.get_pixel(image, x, y)
#             red, green, blue = picture.get_pixel(image, x, y)
#             picture.set_pixel(imagecopy, center_x, center_y, red, green, blue)
#     return imagecopy


def zoom(image):
    """
    Zoom into the center portion of the image.
    
    """
    
    width = picture.image_width(image)
    height = picture.image_height(image)
    
    start_x = width // 4
    start_y = height // 4


    imagecopy = picture.blank_image(width, height)


    for y in range(height//2):
        for x in range(width//2):
            red, green, blue = picture.get_pixel(image, start_x + x, start_y + y)
            for ay in range(2):
                for ax in range(2):
                    new_x = (2 * x + ax)
                    new_y = (2 * y +ay )
                    picture.set_pixel(imagecopy, new_x, new_y, red, green, blue)

    return imagecopy


    
 



    


    




    
 



    


    


