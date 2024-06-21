from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
image = cv2.imread('dogs.jpg')# Load the image using OpenCV
gray_image = rgb2gray(image)# Convert the image to grayscale using scikit-image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)# Convert BGR image to RGB format for matplotlib display
plt.figure(figsize=(10, 5))# Display the original and grayscale images using matplotlib
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image_rgb)
plt.axis('off')
plt.subplot(1, 2, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')
plt.tight_layout()
plt.show()
