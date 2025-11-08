import cv2
import numpy as np

img = cv2.imread("dummy/img/pfp sm.png")
kernel = np.ones((5,5), np.uint8) # define matrix size and assign it as unasigned int 8bit 0 -> 255

if img is None:
    print("error")
else:
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayscale, (7,7), 0)
    canny = cv2.Canny(blur, 25, 30) # edge detection lower for more sensitive image
    dialation = cv2.dilate(canny, kernel=kernel, iterations=3) # Expand the white detection from canny
    erode = cv2.erode(dialation, kernel=kernel, iterations=2)
    
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("output", 400, 400)
    
    cv2.imshow("output", erode)
    cv2.waitKey(0)
