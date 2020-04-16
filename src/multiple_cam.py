# import the necessary packages
from __future__ import print_function
# from pyimagesearch.basicmotiondetector import BasicMotionDetector
from imutils.video import VideoStream
import numpy as np
import datetime
import imutils
import time
import cv2

# initialize the video streams and allow them to warmup
webcam = VideoStream(src=0).start()
picam = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)

def display_img(frame, name, ts):
     cv2.putText(frame, ts, (10, frame.shape[0] - 10), 
        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
     cv2.imshow(name, frame)


# loop over frames from the video streams
while True:
	# initialize the list of frames that have been processed

    pi_frames = []
    webcam_frames = []

    p_frame = picam.read()
    w_frame = webcam.read() 

    # update the frame lists
    pi_frames.append(p_frame)
    webcam_frames.append(w_frame)\

    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
    tss = timestamp.strftime('%H-%M-%S-%f')

    display_img(p_frame, 'Picam', ts)
    display_img(w_frame, 'Webcam', ts)

    cv2.imwrite('pi/f1_{}.jpg'.format(tss), p_frame)
    cv2.imwrite('web/f2_{}.jpg'.format(tss), w_frame)

    # check to see if a key was pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cv2.destroyAllWindows()
webcam.stop()
picam.stop()