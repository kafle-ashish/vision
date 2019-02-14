import cv2
import numpy as np

def get_contours(frame):
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(imgray, (7, 7), 0)
    #ret,thresh = cv2.threshold(imgray,127,255,0)
    # contours, hierarchy = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    return  cv2.findContours(blurred,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[-2:]

def find_mean(contour):
    x_sum = 0
    y_sum = 0
    num   = 0
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
    # mean = [x_sum/num, y_sum/num]
    return [x_sum/num, y_sum/num]

def auto_canny(frame, sig=0.33):
    # compute the median of the single channel pixel intensities
	v = np.median(frame)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sig) * v))
	upper = int(min(255, (1.0 + sig) * v))
	edged = cv2.Canny(frame, lower, upper)
	# return the edged image
	return edged
    
def roi(img,vertices):
    # blank mask:
    mask = np.zeros_like(img)

    # filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, 255)

    # returning the image only where mask pixels are nonzero
    masked = cv2.bitwise_and(img, mask)
    return masked