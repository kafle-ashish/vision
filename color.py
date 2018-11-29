import cv2
import numpy as np


def color_finder(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([120,100,0])
    upper_red = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    kernel = np.ones((5, 5), np.uint8)
    dilation = cv2.dilate(res, kernel, iterations=1)
    
    return dilation
    '''
    # lower_red = np.array([150,50,50]) 
    # upper_red = np.array([180,255,255])
    # red lies in other region too
    # use this mask as well
    # lower_red_ = np.array([0,50,50])
    # upper_red_ = np.array([30,255,255])
    # mask_lower = cv2.inRange(hsv, lower_red_, upper_red_)
    # mask = cv2.bitwise_or(mask,mask_lower)
    # kernel = np.ones((5, 5), np.uint8)
    # erosion = cv2.erode(mask, kernel, iterations=1)
    # dilation = cv2.dilate(mask, kernel, iterations=1)

    # opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)   
    # closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    # kernel = np.ones((15, 15), np.float32)/255
    # smoothed = cv2.filter2D(res, -1, kernel)

    # blur = cv2.GaussianBlur(res, (15, 15), 0)
    # median = cv2.medianBlur(res, 15)
    # bilateral = cv2.bilateralFilter(res, 15, 75, 75)'''