import LsbSteg
import transposition as t
import random
import os
from PIL import Image
import base64


path = r"/home/shivdutt/Desktop/lsb_steganography/resources"
extension = "png"
rname = random.choice([x for x in os.listdir(path)if os.path.isfile(os.path.join(path, x))])
rname2 = random.choice([x for x in os.listdir(path)if os.path.isfile(os.path.join(path, x))])
print("Random image file selected for steganography:",rname)
path2 = r"/home/shivdutt/Desktop/lsb_steganography/resources2/stars_background.jpg"
with open(path2, "rb") as img2:
        img_str = base64.b64encode(img2.read())
#print(img_str)
emessage = t.encryptMessage(img_str.decode('utf-8'))
print(img_str)
#print("Transpositional cipher generates : ",emessage)

imageFilename = rname
newImageFilename = "stego"

newImg = LsbSteg.encodeLSB(emessage, imageFilename, newImageFilename)
if not newImg is None:
        print("Stego image created.")
print("Image ready to be sent!")