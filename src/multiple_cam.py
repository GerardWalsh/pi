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
print("[INFO] starting cameras...")
webcam = VideoStream(src=0).start()
picam = VideoStream(usePiCamera=True).start()
time.sleep(2.0)

# loop over frames from the video streams
while True:
	# initialize the list of frames that have been processed
	frames = []
	# loop over the frames and their respective motion detectors
	for picam, webcam in webcam, picam:
		# read the next frame from the video stream and resize
		# it to have a maximum width of 400 pixels
		frame = picam.read()
		frame = imutils.resize(frame, width=400)

    # update the frames list
    frames.append(frame)
    timestamp = datetime.datetime.now()
    ts = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")

    # loop over the frames a second time
    for (frame, name) in zip(frames, ("Webcam", "Picamera")):
        # draw the timestamp on the frame and display it
        cv2.putText(frame, ts, (10, frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
        cv2.imshow(name, frame)

    # check to see if a key was pressed
    key = cv2.waitKey(1) & 0xFF
    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

# do a bit of cleanup
print("[INFO] cleaning up...")
cv2.destroyAllWindows()
webcam.stop()
picam.stop()