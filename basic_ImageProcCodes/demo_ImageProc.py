import numpy as np
from matplotlib import pyplot as plt
# import pandas as pd
import PIL

img = PIL.Image.open('einstein.png')

# #UNCOMMENT this to see the results, it's really big, so we'll keep it hidden
# img.show()

# #========= IMG.mode ==================
# #This gives us the current color mode of our image from this list:
# 
# #1: 1-bit pixels, black and white
# #L: 8-bit pixels, Greyscale
# #P: 8-bit pixels, mapped to any other mode using a color palette
# #RGB: 3×8-bit pixels, true color
# #RGBA: 4×8-bit pixels, true color with transparency mask
# #image.convert()

# #================== IMAGE.convert(CONVERSION) ==================
# #tells the image to change it's color mode to a new one specified

print(img.mode)

img1 = img.convert("1")

# #UNCOMMENT this to see the results!
# img1.show()
# print(img.size)

# # ======== Images as numpy arrays ==================
# # An image is just a matrix with each pixel having a value.
# # Let's use the Einstein image and turn it into a numpy array to work with!

einstein_arr = np.array(img, dtype='int16')
print(einstein_arr)
#each 8-bit pixel is now a 16 bit integer arranged into a matrix!

print(einstein_arr.shape)


# # ======= To show the numpy version, we use first set up  ==================
# # matplotlib ax using our fig, axs = plt.subplots(),
# # then we use ax.imshow(ARRAY)
# 
# fig, ax = plt.subplots()
# 
# ax.imshow(einstein_arr)

data1 = PIL.Image.fromarray(einstein_arr)
data1.show()

# # ======== Let's start with a transpose operation  ==================

trans_Data = np.transpose(einstein_arr)
data2 = PIL.Image.fromarray(trans_Data)
data2.show()

# # ======== Let's crop or slice  ==================

crop_Data = einstein_arr[0:300, :]
data3 = PIL.Image.fromarray(crop_Data)
data3.show()