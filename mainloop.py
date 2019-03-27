def mainLoop():
    # code inside the while runs till program stops.
    while (1):
        potVal = board.analog[0].read()
        print('wow!' + potVal)
