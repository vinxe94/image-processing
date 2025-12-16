import cv2 as cv

cap = cv.VideoCapture('Videos/name.webm')
while True:
    ret, frame = cap.read()
    if not ret or cv.waitKey(20) & 0xFF == ord('d'): break
    cv.imshow('Video', frame)
cap.release(); cv.destroyAllWindows()

import cv2 as cv 
cap = cv.VideoCapture('Videos/name.webm')
while True:
    ret, frame = cap.read()
    if not ret or cv.waitKey(20) & 0xFF == ord('d'): break
    cv.imshow('Video', frame)
cap.release(); cv.destroyAllWindows()