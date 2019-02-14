

import cv2
import numpy as np

from helpers import Motor
from helpers import color_finder
from helpers import get_contours, find_mean, auto_canny, roi
print(cv2.__version__)
cap = cv2.VideoCapture(0)
motor = Motor()

if __name__ == "__main__":
    print("Starting seek and destroy ...")
    while True:
        _, frame = cap.read()
        print("Image Captured ...")
        #print(frame.size)
        red_rect = white_black = frame
        #First find if a rectangular patch of red exists
        red_rect = color_finder(red_rect, color="red")
        #imgray = cv2.cvtColor(red_rect,cv2.COLOR_BGR2GRAY)
        # ret,thresh = cv2.threshold(imgray,127,255,0)
        contours, _ = get_contours(red_rect)
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # median = cv2.medianBlur(gray, 7)
        # edged = auto_canny(median)
        # contours, _ = get_contours(edged)
        # print("Searched Contours ...")

        for contour in contours:
             if cv2.contourArea(contour) > 200:
                position = find_mean(contour)
                if position[0] < 290:
                    print("move_right")
                    motor.rightTurn()
                elif position[0] <= 350 and position[0] >= 290:
                    print("move_forward")
                    motor.forwardDrive()
                elif position[0] > 350:
                    print("move_left")
                    motor.leftTurn()
                else:
                    print("stop")
                    motor.allStop()

                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2) 
        # cv2.imshow('Output', median)
        cv2.imshow('Red', frame)
        print("Finished ...")
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
    cap.release()

