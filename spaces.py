import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/Character 1.png') #Change the path if needed
cv.imshow('Image', img)

#plt.imshow(img)
#plt.show()

gray = cvt = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR) #copy this if you want to reverse it back to bgr
cv.imshow('HSV --> BGR', hsv_bgr) #change the hsv to any example lab -- lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
                                  #cv.imshow('LAB --> BGR', lab_bgr)

plt.imshow(rgb) #you can change rgb to show the other plots too
plt.show()

cv.waitKey(0)