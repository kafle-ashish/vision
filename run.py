
import cv2
import numpy as np

#from helpers import Motor
from helpers import color_finder
from helpers import get_contours, find_mean

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    #motor = Motor()
    while True:
        _, frame = cap.read()

        ret = color_finder(frame)
        image, contours, _ = get_contours(ret)  
        for contour in contours:
            if cv2.contourArea(contour) > 2000:
                position = find_mean(contour)
                '''
                    Include a failsafe when no contours found
                    if was previously moving left? -> then move right 
                    and vice-versa 
                '''
                if position[0] < 290:
                    print("left")
                    #Motor.move_right()
                elif position[0] <= 350 and position[0] >= 290:
                    print("forward")
                    #Motor.move_forward()
                elif position[0] > 350:
                    print("right")
                    #Motor.move_left()
                ################################
                #Motor.brake()
                ################################
                #cv2.drawContours(ret, contour, -1, (0, 255, 0), 3)
                x,y,w,h = cv2.boundingRect(contour)
                cv2.rectangle(ret,(x,y),(x+w,y+h),(0,255,0),2)              
        cv2.imshow('Output', ret)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()