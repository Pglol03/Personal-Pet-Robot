import RPi.GPIO as IO

import time

IO.setwarnings(False)

IO.setmode(IO.BCM)


IO.setup(27,IO.OUT) #GPIO 2 -> Red LED as output

IO.setup(22,IO.OUT) #GPIO 3 -> Green LED as output

IO.setup(17,IO.IN) #GPIO 14 -> IR sensor as input


while 1:


    if(IO.input(17)==True): #object is far away

        IO.output(27,True) #Red led ON

        IO.output(22,False) # Green led OFF

    

    if(IO.input(17)==False): #object is near

        IO.output(22,True) #Green led ON

        IO.output(27,False) # Red led OFF

