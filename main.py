# CPRE 186
# Spring 2019
# Written by: Alexis Renderos

from pyFirmata import Arduino, util # used to talk to Arduino over USB.
import cv2 # openCV library

def setup():
    # setup runs once
    board = Arduino('/dev/tty.usbserial-A6008rIF')
    board.digital[13].write(1) # sets the onboard LED to ON.

    iter = util.Iterator(board)
    iter.start()
    board.analog[0].enable_reporting() # change to be port of potentiometer.
    print('done!')

def mainLoop():
    # code inside the while runs till program stops.
    while (1):
        potVal = board.analog[0].read()
        print('wow!' + potVal)
