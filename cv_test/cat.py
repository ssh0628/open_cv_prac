import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('cat.png')
img[:, :, 1] = 0
""" cv.imshow('cat', img)
cv.waitKey(0) """
plt.imshow(img)