import cv2

img = cv2.imread('dummy/img/pfp sm.png')

if img is None:
    print('error')
else:
    print(img.shape)
    resize = cv2.resize(img, (200, 300))
    crop = img[0:200, 200:500]
    
    # cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    # cv2.resizeWindow("output", 400, 400)
    
    cv2.imshow('output', resize)
    cv2.waitKey(0)