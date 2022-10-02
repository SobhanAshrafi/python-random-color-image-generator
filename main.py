
import random

from PIL import Image

random.seed()

# generate 3 random numbers to creat a random rgb color
random_color_generator = lambda : ( random.randrange(0,255), random.randrange(0,225), random.randrange(0,255) )
 


if __name__ == '__main__':

    # creat new image
    im = Image.new("RGB",(1024,1024),(255,255,255))

    for j in range(im.height):
        
        Color = random_color_generator()
        
        for i in range(im.width):
            
            # uncomment below line to make all pixels color random
            # Color = random_color_generator()
            
            im.putpixel((i,j),Color)
            

    # to show generated image
    im.show()



    # save result image
    im.save("result/img.jpg")
    im.close()


