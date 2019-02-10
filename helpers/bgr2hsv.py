

import cv2

image = cv2.imread("black.jpg")

bgr = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

cv2.imshow('red', bgr)

cv2.waitKey(0)
