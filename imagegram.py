# imagegram.py
# This program applies a set of filters, chosen by the user, to a given image. 
# The filters include:
# 1. the negative of the image
# 2. the grayscale of the image
# 3. the image flipped vertically
# 4. the image scrolled to the right
# 5. the center of the image zoomed in

from warmupgram_func import grayscale,negative_filter, vertflip,horizontal_scroll_filter,posterize,zoom,copy
import picture
print("Welcome to Imagegram! ")



error = 0
while error == 0:
    try:
        file_name = input("Please enter a filename: ")
        image = picture.load_image(file_name)
        width = picture.image_width(image)
        height = picture.image_height(image)
    except Exception:
        print("The file does not exist. Please try again.")
    else:
        error = 1


    




img = copy(image)
picture.new_picture(width, height)
picture.draw_image(0, 0,img)
picture.display()






choice = 100
while choice != 0 :
    print("Which of the following filters would you like to apply")

    print("""
          1. Make Negative
          2. Make Grayscale
          3. Flip Vertically
          4. Scroll Horizontally
          5. Zoom
          6. Posterize
          0. Quit""")
    
    choice = int(input("Choice: "))
    if choice == 1:
        img = negative_filter(img, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0,img)
        picture.display()
    if choice == 2:
        img = grayscale(img, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0,img)
        picture.display()
    if choice == 3 :
        img = vertflip(img, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0,img)
        picture.display()
    if choice == 4:
        shift = int(input("pixels to shift the image horizontally: "))
        img = horizontal_scroll_filter(img, width, height,shift)
        picture.new_picture(width, height)
        picture.draw_image(0, 0,img)
        picture.display()
    if choice == 5:
        img = zoom(img)
        picture.new_picture(width, height)
        picture.draw_image(0,0,img)
        picture.display()
        
    if choice == 6 :
        img = posterize(img, width, height)
        picture.new_picture(width, height)
        picture.draw_image(0, 0,img)
        picture.display()





print("Goodbye ! ")
# gray_img = grayscale(image, width, height)





        








# The picture module allows us to determine the width and height of the 
# image. We will need these dimensions so that we can loop through every 
# pixel and perform some filtering operation. We will also use the 
# dimensions later to draw the image on a canvas for display.


# Here is where we'll call our filtering functions. If you are running
# this file before updating warmupgram_func.py, neither function's body is 
# defined at the moment, so a blank image is returned. 
# Add code to the body of each filtering function to get them working.



    
# To display the final image, we must first create a canvas of the same 
# size. We can then draw the image on this blank canvas.
