import RPi.GPIO as IO

import time

IO.setwarnings(False)

IO.setmode(IO.BOARD)


IO.setup(11,IO.OUT) #GPIO 2 -> Red LED as output

IO.setup(13,IO.OUT) #GPIO 3 -> Green LED as output

IO.setup(15,IO.IN) #GPIO 14 -> IR sensor Front as input

IO.setup(16,IO.OUT) #GPIO 2 -> Red LED as output

IO.setup(18,IO.OUT) #GPIO 3 -> Green LED as output

IO.setup(22,IO.IN) #GPIO 14 -> IR sensor back as input
# while 1:
#     IO.output(11,True)
#     IO.output(16,True)
while 1:


    if(IO.input(15)==True): #object is far away
        print("case1")
        IO.output(11,True) #Red led ON

        IO.output(13,False) # Green led OFF

    

    if(IO.input(15)==False): #object is near

        IO.output(13,True) #Green led ON

        IO.output(11,False) # Red led OFF

