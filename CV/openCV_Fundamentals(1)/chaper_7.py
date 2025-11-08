import cv2
import numpy as np

img = cv2.imread('dummy/img/pfp sm.png')

if img is None:
    print('error')
else:
    resize = cv2.resize(src=img, dsize=(200, 300))
    imgHSV = cv2.cvtColor(src=resize, code=cv2.COLOR_BGR2HSV)
    horizontal = np.hstack((resize, imgHSV))
    
    # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("output", 400, 400)
    
    cv2.imshow('output', horizontal)
    cv2.waitKey(0)