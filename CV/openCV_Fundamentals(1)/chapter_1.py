import cv2
import numpy as np
from typing import Optional

def read_image(path: str) -> Optional[np.ndarray]:
    img = cv2.imread(f'{path}')
    if img is not None:
        cv2.imshow("img", img)
        cv2.waitKey(0)
        return img
    else:
        print("Error: Could not load image. Check the file path.")
        return None

def read_video(path:str) -> Optional[np.ndarray]:
    vid = cv2.VideoCapture(f"{path}")
    while True:
        success, img = vid.read()
        cv2.imshow("video", img)
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break