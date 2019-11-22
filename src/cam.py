# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
<<<<<<< Updated upstream
camera.resolution = (1640, 1232) #(640, 480) 
camera.framerate = 20
camera.vflip = True
rawCapture = PiRGBArray(camera, size=(1640, 1232))
=======
res = (1280, 720)
camera.resolution = res #(640, 480) 
camera.framerate = 20
camera.vflip = True
rawCapture = PiRGBArray(camera, size=res)
>>>>>>> Stashed changes
 
# allow the camera to warmup
time.sleep(0.1)
 
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	# grab the raw NumPy array representing the image, then initialize the timestamp
	# and occupied/unoccupied text
	image = frame.array
 
	# show the frame
	cv2.imshow("Frame", image)
	key = cv2.waitKey(1) & 0xFF
 
	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break
