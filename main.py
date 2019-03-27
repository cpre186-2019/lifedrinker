# CPRE 186
# Spring 2019
# Written by: Alexis Renderos

from pyfirmata import Arduino, util # used to talk to Arduino over USB.
import cv2 # openCV library

setup()
mainLoop()





def setup():
    # setup runs once
    board = Arduino('/dev/tty.usbserial-A6008rIF')
    board.digital[13].write(1) # sets the onboard LED to ON.

    analog_0 = board.get_pin('a:0:i') # pot pin
    pin0 = board.get_pin('d:0:o') # pin0 for motor 1
    pin1 = board.get_pin('d:1:o') # pin1 for motor 1
    pin2 = board.get_pin('d:2:o') # pin2 for motor 2
    pin3 = board.get_pin('d:3:o') # pin3 for motor 2
    pwm1 = board.get_pin('d:5:p') # pwm pin for motor 1
    pwm2 = board.get_pin('d:6:p') # pwm pin for motor 2

    # start these values with the correct values for a forward shot.
    pin0state = 0
    pin1state = 0
    pin2state = 0
    pin3state = 0

    pin0.write(pin0state)
    pin1.write(pin1state)
    pin2.write(pin2state)
    pin3.write(pin3state)

    iter = util.Iterator(board)
    iter.start()
    board.analog[0].enable_reporting() # change to be port of potentiometer.
    print('done!')

def mainLoop():
    # code inside the while runs till program stops.
    while (1):
        potVal = board.analog[0].read()
        print('wow!' + potVal)





def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
}

def updateOneFlywheel(speed, choice):
    if (choice != 0 and choice != 1):
        #error!
        print("error!")
    else if (choice == 0):
        print("bottom motor updating...")
    else:
        print("top motor updating...")

def updateFlywheel(speed):
    # updates both same speed
    updateOneFlywheel(speed, 0)
    updateOneFlywheel(speed, 1)

def updateFlywheel(speed1, speed2):
    # updates both, different speed
    # first param is bottom speed, second param is top speed
    updateOneFlywheel(speed1, 0)
    updateOneFlywheel(speed2, 1)
