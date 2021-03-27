import LsbSteg
import transposition as t
import random
import os
from PIL import Image
import base64
from io import BytesIO

print("Decoding...")
emessage = LsbSteg.decodeLSB("stego.png")
message = emessage = t.decryptMessage(emessage)
#print("E-message: ", message)
# base64message = base64.b64encode(message.encode('utf-8'))
# with open('encode.bin', "wb") as file:
#     file.write(base64message)

# file2 = open('encode.bin', "rb")
# byte = file2.read()
# file2.close()

# path2 = r"/home/shivdutt/Desktop/lsb_steganography/resources2/stars_background.jpg"
# with open(path2, "rb") as img2:
#     img_str = base64.b64encode(img2.read())

u = message.encode("utf-8")

#res1 = base64.b64decode(message)
#print(res1)
# print(BytesIO(base64.b64decode(res1)))
im = Image.open(BytesIO(base64.b64decode(message)))
im.save('result.png', 'PNG')

print("DONE!")
#print("Decrypted Message: {}".format(t.decryptMessage(message)))
