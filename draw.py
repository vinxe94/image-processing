#pylint:disable=no-member

import cv2 as cv
import numpy as np

# Create blank canvas
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint a certain colour
paint_img = blank.copy()
paint_img[200:300, 300:400] = 0,0,255  # Red square
cv.imshow('Painted', paint_img)

# 2. Draw a Rectangle
rect_img = blank.copy()
cv.rectangle(rect_img, (0,0), (rect_img.shape[1]//2, rect_img.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', rect_img)

# 3. Draw a Circle
circle_img = blank.copy()
cv.circle(circle_img, (circle_img.shape[1]//2, circle_img.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', circle_img)

# 4. Draw a Line
line_img = blank.copy()
cv.line(line_img, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', line_img)

# 5. Write Text
text_img = blank.copy()
cv.putText(text_img, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #change the 'Hello, my name is Jason!!!' to your name
cv.imshow('Text', text_img)

cv.waitKey(0)
cv.destroyAllWindows()