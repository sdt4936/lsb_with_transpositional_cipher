import LsbSteg
import transposition as t
import random
import os

path = r"/home/shivdutt/Desktop/lsb_steganography/resources"
rname = random.choice([x for x in os.listdir(path)if os.path.isfile(os.path.join(path, x))])
print("Random image file selected for steganography:",rname)
message = input("enter the text to be encrypted:")
emessage = t.encryptMessage(message)
print("Transpositional cipher generates : ",emessage)

imageFilename = rname
newImageFilename = "stego"

newImg = LsbSteg.encodeLSB(emessage, imageFilename, newImageFilename)
if not newImg is None:
        print("Stego image created.")
print("Image ready to be sent!")



