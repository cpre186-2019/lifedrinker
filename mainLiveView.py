# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import numpy as np
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera_resolution_x = 640
camera_resolution_y = 480
camera.resolution = (camera_resolution_x, camera_resolution_y)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(camera_resolution_x, camera_resolution_y))

# allow the camera to warmup
time.sleep(0.1)

# Set up the tracker_type
tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[2] # 2 = TrackerKCF_create

if tracker_type == 'BOOSTING':
    tracker = cv2.TrackerBoosting_create()
if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
if tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
if tracker_type == 'TLD':
    tracker = cv2.TrackerTLD_create()
if tracker_type == 'MEDIANFLOW':
    tracker = cv2.TrackerMedianFlow_create()
if tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
if tracker_type == 'MOSSE':
    tracker = cv2.TrackerMOSSE_create()
if tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
frame = cv2.flip(rawCapture.array, -1)

# Select bounding box
bbox = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

# Calculate center of image and store in a tuple
# This represents the theoretical line of fire
frame_width  = camera_resolution_x
frame_height = camera_resolution_y
video_center = (int(frame_width/2.0), int(frame_height/2.0))

# clear buffer in anticipation of main loop
rawCapture.truncate(0)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = cv2.flip(np.array(frame.array), -1)

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(image)

    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

    # radius should be scaled with target_center
    reticule_scalar = 5.0
    radius = (((frame_height / 2.0) * reticule_scalar) / 100.0)

    # gun reticule (light blue)
    cv2.circle(image, video_center, radius, (255,255,0), thickness=2, lineType=8, shift=0)

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))

        # note: colors are blue, green, red (lmao why)

        # rectangle around target (blue)
        cv2.rectangle(image, p1, p2, (255,0,0), 2, 1)

        # from this information we can then derive distance from center and angle of correction using some fancy math.
        target_center = (int(p1[0]+(bbox[2]/2.0)),int(p1[1]+(bbox[3]/2.0)))

        # target correction arrow (green)
        cv2.arrowedLine(image, video_center, target_center, (0,255,0), 3)

        # target reticule (red)
        cv2.circle(image, target_center, radius, (0,0,255), thickness=2, lineType=8, shift=0)

        cv2.putText(image, "Tracking Successful", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
    else :
        # Tracking failure
        cv2.putText(image, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

    # Display tracker type on frame
    cv2.putText(image, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

    # Display FPS on frame
    cv2.putText(image, "FPS: " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

    # Display result
    cv2.imshow("can finder", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
    	break
