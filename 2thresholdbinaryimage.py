import numpy as np
import cv2
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from scipy import ndimage
image = cv2.imread('dogs.jpg')# Load the image using OpenCV
gray_image = rgb2gray(image)# Convert the image to grayscale using scikit-image
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)# Convert BGR image to RGB format for matplotlib display
gray_r = gray_image.reshape(gray_image.shape[0] * gray_image.shape[1])# Reshape the grayscale image for thresholding
mean_value = gray_r.mean()# Reshape the grayscale image for thresholding
thresholded = np.where(gray_r > mean_value, 1, 0)# Apply thresholding based on mean value
thresholded_image = thresholded.reshape(gray_image.shape[0], gray_image.shape[1])# Reshape the thresholded array back to the original shape
plt.imshow(thresholded_image, cmap='gray')# Display the thresholded image using matplotlib
plt.title('Thresholded Binary Image')
plt.axis('off')
plt.show()
