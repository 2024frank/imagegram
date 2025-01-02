from warmupgram_func import grayscale,vertflip,negative_filter
import picture


image = picture.load_image("crayons.jpg")

# The picture module allows us to determine the width and height of the 
# image. We will need these dimensions so that we can loop through every 
# pixel and perform some filtering operation. We will also use the 
# dimensions later to draw the image on a canvas for display.
width = picture.image_width(image)
height = picture.image_height(image)

# Here is where we'll call our filtering functions. If you are running
# this file before updating warmupgram_func.py, neither function's body is 
# defined at the moment, so a blank image is returned. 
# Add code to the body of each filtering function to get them working.


gray_img = grayscale(image, width, height)
gray_flipped_img = vertflip(gray_img, width, height)
negative_img = negative_filter(image, width, height)


# To display the final image, we must first create a canvas of the same 
# size. We can then draw the image on this blank canvas.

picture.new_picture(width, height)
picture.draw_image(0,0,image)
picture.run()