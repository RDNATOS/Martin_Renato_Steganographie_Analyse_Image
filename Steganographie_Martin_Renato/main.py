#Steganographie With Compression - Martin & Renato
# 19 03 2025
#PIL comes from the Pillow package
from PIL import Image
import numpy as np

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

pepper = Image.open("pepper.bmp").convert("L") #convertion to grayscale
girlface = Image.open("girlface.bmp").convert("L")

#now girlface has a size of 512 x 512 like pepper
girlface = girlface.resize(pepper.size)

#array conversion
pepper_array = np.array(pepper)
girlface_array = np.array(girlface)

#compression of the secret image


compressed_secret = np.diff(girlface_array, axis=1)
compressed_secret = np.hstack([compressed_secret, np.zeros((girlface_array.shape[0], 1), dtype=compressed_secret.dtype)])

#secret image is hidden in the cover image
secret_high = (compressed_secret >> 4) & 0x0F

#least signifiant bits to 0 and most significant bits are kept for the cover image
pepper_high = pepper_array & 0xF0

#images fusion
stego_array = pepper_high | secret_high

#the 4 hiddent bits are extracted
#extracted_secret = (stego_array & 0x0F) << 4
extracted_secret = stego_array & 0x0F
extracted_secret = (extracted_secret / 15) * 255
extracted_secret = extracted_secret.astype(np.uint8)
extracted_secret = (extracted_secret << 4) | (extracted_secret & 0x0F)

plt.figure(figsize=(10, 8))

#starting image pepper
plt.subplot(2, 2, 1)
plt.title("Image de départ (pepper)")
plt.imshow(pepper_array, cmap="gray")
plt.axis("off")

#image to hide girlface
plt.subplot(2, 2, 2)
plt.title("Image à cacher (girlface)")
plt.imshow(girlface_array, cmap="gray")
plt.axis("off")

#image containing the secret image
plt.subplot(2, 2, 3)
plt.title("Image résultante avec secret")
plt.imshow(stego_array, cmap="gray")
plt.axis("off")

#secret image extracted
plt.subplot(2, 2, 4)
plt.title("Secret extrait")
plt.imshow(extracted_secret, cmap="gray", vmin=0, vmax=255)
plt.axis("off")


plt.tight_layout()
plt.show()



