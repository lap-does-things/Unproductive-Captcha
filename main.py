# THIS LINE IS PURELY TO FLEX ON THE FACT THAT THIS CODE IS STILL WELL WITHIN 10 LINES, AND I CAN GO FURTHER WITH THE REFACTORS... There are also constants for you below
import os, sys, time, string as st, numpy as np; from PIL import Image, ImageDraw, ImageFont # I dont care about PEP8
ALPHABET = np.array(list(st.ascii_letters + ' ')) # The alphabet to use !!YOU MIGHT WANT TO CHANGE THIS!!
dim = type("Dimensions", (object,), {"width": 200, "height": 150})() # The dimensions of the image !!YOU MIGHT WANT TO CHANGE THIS!!
string = "".join(np.random.choice(ALPHABET, size=8, replace=True).tolist()).replace(" ", "")
Image.MAX_IMAGE_PIXELS = None; font = ImageFont.truetype("arial.ttf", 20); img = Image.new("RGB", tuple([dim.width, dim.height]), (255, 255, 255));draw = ImageDraw.Draw(img)
for i in range(np.random.randint(10, 60)):draw.line((np.random.randint(0,dim.width), np.random.randint(0,dim.height), np.random.randint(0,dim.width*2), np.random.randint(0,dim.height*2)), fill=(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255)), width=np.random.randint(1, 5))
draw.text((dim.width//4, dim.height//3), string, font=font, fill=(0, 0, 0),stroke_fill=(255, 255, 255),stroke_width=0.1);w = img.rotate(np.random.randint(0, 360), fillcolor=(255,255,255), expand=1);img.save(string + ".png"); print("File saved as " + string + ".png")