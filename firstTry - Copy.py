##--------------------------------------------------------------------------------------
## Module: firstTry.py
## Release Information:
##  V0.0.0    (Jim Womack, 04/6/2015)   :   Initial version
##--------------------------------------------------------------------------------------

##--------------------------------------------------------------------------------------
## NOTES
##  1.)  This is a short file that will read the board temperature every 15 seconds and
##      print the results to the screen
##--------------------------------------------------------------------------------------


import time

settime = time.time()
tempSample = 1     #15 seconds


while True:

    if time.time() >= tempSample + settime:
        c = open("/sys/devices/platform/mtcdp/board-temperature", 'r')
        d = c.read()
        e = d.split("\n")
        f = e[0]
        print f
        settime = time.time()

    