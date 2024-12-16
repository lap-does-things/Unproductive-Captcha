import numpy as np
from PIL import Image, ImageDraw, ImageFont
import string as st
import os, sys, time

string = "Hello World!" # Fallback string
ALPHABET = np.array(list(st.ascii_letters + ' ')) # The alphabet to use !!YOU MIGHT WANT TO CHANGE THIS!!

class Dimensions():     # A nicer way to define dimensions
    def __init__(self, width, height):
        self.width = width
        self.height = height

dim = Dimensions(200, 150) # The dimensions of the image !!YOU MIGHT WANT TO CHANGE THIS!!

def getlyric():
    return "".join(np.random.choice(ALPHABET, size=8, replace=True).tolist()) # who doesnt love some nested list comprehension

def main():
    string = getlyric()

    Image.MAX_IMAGE_PIXELS = None    
    font = ImageFont.truetype("arial.ttf", 20) # Default font !!YOU MIGHT WANT TO CHANGE THIS!!
    img = Image.new("RGB", tuple([dim.width, dim.height]), (255, 255, 255))
# the actual work starts here
    draw = ImageDraw.Draw(img)
    for i in range(np.random.randint(10, 60)):
        draw.line((np.random.randint(0,dim.width), np.random.randint(0,dim.height), np.random.randint(0,dim.width*2), np.random.randint(0,dim.height*2)), fill=(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), width=np.random.randint(1, 5))
    draw.text((dim.width//4, dim.height//3), string, font=font, fill=(0, 0, 0),stroke_fill=(255, 255, 255),stroke_width=0.1)
    w = img.rotate(np.random.randint(0, 360), fillcolor=(255,255,255), expand=1)

    img.save(string + ".png")
    print("File saved as " + string + ".png")
if __name__ == "__main__":
    main()