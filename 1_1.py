from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage

# Load the image using OpenCV
image = cv2.imread('dogs.jpg')

# Convert the image to grayscale using scikit-image
gray_image = rgb2gray(image)

# Display the original and grayscale images using matplotlib
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
