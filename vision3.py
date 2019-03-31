from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys

(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera_resolution_x = 640
camera_resolution_y = 480
camera.resolution = (camera_resolution_x, camera_resolution_y)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(camera_resolution_x, camera_resolution_y))

if __name__ == '__main__' :

    # Set up tracker.
    # Instead of MIL, you can also use

    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[2]

    if int(minor_ver) < 3:
        tracker = cv2.Tracker_create(tracker_type)
    else:
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
        image = rawCapture.array

        # Read first frame
        ok, frame = camera.capture(rawCapture, format="bgr") # this line will probably break, consider format of video.read()'s return and data type
        if not ok:
            print('Cannot read video file')
            sys.exit()

    # Define an initial bounding box within first frame (change this for a specific area)
    # bbox = (287, 23, 86, 320)

    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)

    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)

    # Calculate center of image and store in a tuple
    frame_width  = camera_resolution_x
    frame_height = camera_resolution_y
    video_center = (int(frame_width/2.0), int(frame_height/2.0))

    while True:
        # grab an image from the camera_resolution_x
        camera.capture(rawCapture, format="bgr")
        image = rawCapture.array

        # Read a new frame
        ok, frame = image # this line will probably break, consider format of video.read()'s return and data type
        if not ok:
            break

        # Start timer
        timer = cv2.getTickCount()

        # Update tracker
        ok, bbox = tracker.update(frame)

        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);

        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)

            # from this information we can then derive distance from center and angle of correction using some fancy math.
            target_center = (int(p1[0]+(bbox[2]/2.0)),int(p1[1]+(bbox[3]/2.0)))
            cv2.line(frame, video_center, target_center, (0,255,0), 2)

            cv2.putText(frame, "Tracking Successful", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)

        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);

        # Display FPS on frame
        cv2.putText(frame, "FPS: " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

        # Display result
        cv2.imshow("Tracking video", frame)

        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : break
