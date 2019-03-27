def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def updateOneFlywheel(speed, choice):
    if (choice != 0 and choice != 1):
        #error!
        print("error!")
    elif (choice == 0):
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
