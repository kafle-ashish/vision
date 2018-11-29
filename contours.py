import cv2
import numpy as np

def get_contours(frame):
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #ret,thresh = cv2.threshold(imgray,127,255,0)
    img, contours, hierarchy = cv2.findContours(imgray,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    return img, contours, hierarchy

def find_mean(contour):
    x_sum:int = 0
    y_sum:int = 0
    num:int = 0
    for points in contour:
        num += 1
        for item in points:
            if item[0] == None:
                continue
            else:
                x_sum += item[0]
            if item[1] == None:
                continue
            else:
                y_sum += item[1]
    median = [x_sum/num, y_sum/num]
    return median