from matplotlib.image import imread
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image, ImageEnhance
from scipy.fftpack import fft2, ifft2
from skimage import exposure

plt.rcParams['figure.figsize'] = [5, 5]
plt.rcParams.update({'font.size': 14})  

#Input
A = imread("Sign3.jpg")

#Basic Image Manipulation


#gray scale
B = np.mean(A,-1)
#contratast 
contrast_image = exposure.rescale_intensity(B, in_range='image', out_range='dtype')


# Calculate the histogram and bin edges of the contrast-enhanced image
hist, bin_edges = exposure.histogram(contrast_image)
plt.imshow(contrast_image, cmap='gray')
plt.show()

# Plot the histogram
plt.bar(bin_edges[:-1], hist, width=bin_edges[1] - bin_edges[0])
plt.show()


