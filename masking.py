#pylint:disable=no-member

import cv2 as cv
import numpy as np

# Load image
img = cv.imread('Photos/Character 1.png')   # Change the path if needed

# Validate image path
if img is None:
    raise FileNotFoundError("Image not found. Check the path: 'Photos/Character 1.png'")

cv.imshow('Image', img)

# Create blank single-channel mask
blank = np.zeros(img.shape[:2], dtype='uint8')

height, width = img.shape[:2]
print("Image Shape:", img.shape)


circle = cv.circle(
    blank.copy(),
    (width // 2, height // 2),   # center of image
    min(width, height) // 4,     # radius automatically scales to image
    255,
    -1
)

rect_x1 = width // 4
rect_y1 = height // 4
rect_x2 = width // 4 * 3
rect_y2 = height // 4 * 3

rectangle = cv.rectangle(
    blank.copy(),
    (rect_x1, rect_y1),
    (rect_x2, rect_y2),
    255,
    -1
)

# ---------------------------
# Combine masks
# ---------------------------
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weird Shape', weird_shape)

# ---------------------------
# Apply mask to image
# ---------------------------
masked = cv.bitwise_and(img, img, mask=weird_shape)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)