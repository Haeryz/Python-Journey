import cv2
import numpy as np

img = cv2.imread('dummy/img/pfp sm.png')

if img is None:
    print('error')
else:
    stacked = np.hstack(tup=(img, img))
    resize = cv2.resize(stacked, (200, 300))
    
    # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("output", 400, 400)
    
    cv2.imshow('output', resize)
    cv2.waitKey(0)