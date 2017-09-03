"""
@author: KhanhLQ
Goals:
    - Learn to read video, display video and save video
    - Learn to capture camera and display it
"""

# Capture video from camera (camera can be webcam or external camera)
import cv2
import numpy as np


def load_video_from_camera():
    # parameter is the index of camera divide.
    cap = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Operations on each frame
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        # Display image
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
