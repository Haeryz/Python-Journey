import cv2
import numpy as np

img = cv2.imread('dummy/img/pfp sm.png')
black = np.zeros((512, 512, 3), dtype=np.uint8)

if img is None:
    print('error')
else:
    print(black.shape)
    # black[50:200] = 186, 88, 56
    cv2.line(black, (0,0), (black.shape[0], black.shape[1]), (0, 255, 0), 3)
    cv2.rectangle(black, (0,0), (250, 350), (55, 90, 255), 5)
    cv2.circle(black, (400,500), 30, (0, 0, 255))
    
    # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("output", 400, 400)
    
    cv2.imshow('output', black)
    cv2.waitKey(0)