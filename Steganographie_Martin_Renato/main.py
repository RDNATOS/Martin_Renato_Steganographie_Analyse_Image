# Steganography with compression – Martin & Renato
from PIL import Image
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

pepper = Image.open("pepper.bmp").convert("L")
girlface = Image.open("girlface.bmp")

girlface = girlface.resize(pepper.size) #girlface will have 512 x 512 like pepper

# array conversion
pepper_array = np.array(pepper)
girlface_array = np.array(girlface)

# scret image compression only the 4 most significant bits
secret_compressed = girlface_array >> 4

# zero out least significant 4 bits
pepper_high = pepper_array & 0xF0  # Keep upper 4 bits

# meging both images, secret one and cover one
stego_array = pepper_high | secret_compressed

# extraction of the secret image from the cover
extracted_secret = stego_array & 0x0F  # hidden 4 bits

# decompression, 8 bit scale range again
extracted_secret = extracted_secret << 4

plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.title("Pepper - Cover Image")
plt.imshow(pepper_array, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.title("Original Secret Image")
plt.imshow(girlface_array, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.title("Image Fusion")
plt.imshow(stego_array, cmap="gray")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.title("Secret Image Extracted")
plt.imshow(extracted_secret, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()
