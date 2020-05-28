import numpy as np
import sys
import cv2

input_rtsp = "rtsp://10.10.10.9:8080"
cap = cv2.VideoCapture(input_rtsp)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:        
        sys.stdout.write(frame.tostring())
    else:
        break

cap.release()