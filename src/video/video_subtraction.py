"""
@author: KhanhLQ
Goals:
    - Load video from camera (web cam)
    - Subtract 2 frames in a row to identify the movement
"""
import cv2
from collections import deque

# Create a queue of frame
q_frame = deque([])
cap = cv2.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Append frame to stack
    q_frame.append(frame)

    # Show the subtract frame
    if len(q_frame) > 1:
        subtract_frame = q_frame[1] - q_frame[0]
        q_frame.popleft()
        cv2.imshow('frame', subtract_frame)

    # Break capture when hit 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()










