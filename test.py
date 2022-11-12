import numpy as np
import cv2

filepath = "video.mp4"

cap = cv2.VideoCapture(filepath)

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    print(type(frame))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
