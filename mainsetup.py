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
