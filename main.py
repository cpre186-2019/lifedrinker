# CPRE 186
# Spring 2019
# Written by: Alexis Renderos

from pyfirmata import Arduino, util # used to talk to Arduino over USB.
import cv2 # openCV library
import functions # local functions, syntax is functions.(method)(args)
import mainsetup # setup function, runs once.
import mainloop # loop-dee-loop
import vision # our vision code!

print(functions.map(10, 0, 100, 0, 5000))
# mainsetup.setup()
# mainloop.mainLoop()
