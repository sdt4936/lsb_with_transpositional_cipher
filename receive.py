import LsbSteg
import transposition as t
import random
import os

print("Decoding...")
message = LsbSteg.decodeLSB("stego.png")
print("E-message: ", message)
print("Decrypted Message: {}".format(t.decryptMessage(message)))
