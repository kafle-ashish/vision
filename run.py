
import cv2
import numpy as np

from color import color_finder
from contours import get_contours, find_mean

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    while True:
        _, frame = cap.read()

        ret = color_finder(frame)
        image, contours, _ = get_contours(ret)  
        for contour in contours:
            if cv2.contourArea(contour) > 2000:
                position = find_mean(contour)
                if position[0] < 250:
                    print("left")
                else:
                    print("right")
                cv2.drawContours(ret, contour, -1, (0, 255, 0), 3)              
        cv2.imshow('Output', ret)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

    cv2.destroyAllWindows()
    cap.release()