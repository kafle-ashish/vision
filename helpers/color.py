import cv2
import numpy as np

LOWER_RED   = np.array([150,50,50])   # np.array([120,200,0])
UPPER_RED   = np.array([180, 255, 255])

LOWER_BLACK = np.array([0, 0, 0])
UPPER_BLACK = np.array([180, 220, 30])

LOWER_WHITE = np.array([0, 0, 200])
UPPER_WHITE = np.array([180, 255, 255])

def nothing():
    pass


cv2.namedWindow("Trackbars")
 
cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

def color_finder(frame, color):
    hsv  = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = ''
    l_h = cv2.getTrackbarPos("L - H", "Trackbars")
    l_s = cv2.getTrackbarPos("L - S", "Trackbars")
    l_v = cv2.getTrackbarPos("L - V", "Trackbars")
    u_h = cv2.getTrackbarPos("U - H", "Trackbars")
    u_s = cv2.getTrackbarPos("U - S", "Trackbars")
    u_v = cv2.getTrackbarPos("U - V", "Trackbars")

    if color == "red":
        mask =  cv2.inRange(hsv, LOWER_RED, UPPER_RED)
    if color == "white":
        mask =  cv2.inRange(hsv, LOWER_WHITE, UPPER_WHITE)
    if color == "black":
        mask =  cv2.inRange(hsv, LOWER_BLACK, UPPER_BLACK)
    else:
        lower = np.array([l_h, l_s, l_v])
        upper = np.array([u_h, u_s, u_v])
        print(lower, upper)
        mask = cv2.inRange(hsv, lower, upper)
        res = cv2.bitwise_and(frame, frame, mask=mask)
   
        return res
    # kernel = np.ones((5, 5), np.uint8)
    # dilation = cv2.dilate(res, kernel, iterations=1)
    





'''
lower_blue = np.array([100,100,0])
upper_blue = np.array([140,255,255])
lower_green = np.array([65,60,60])
upper_green = np.array([80,255,255])
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