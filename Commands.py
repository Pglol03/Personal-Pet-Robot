from Speech import Speak
from display import wakeup, sleep, dog
from Cmd.Cmdline import gsearch
from Recognition import listen

import Vars

def action(Args):
    if "Baymax" in Args:
        print("Input recognised")
        Speak("Hello User")
        Vars.x = True
        listen()
        action(Vars.queue.deque())
        
    elif "wake up" in Args:
        print("Executing command")
        wakeup()
        Speak("Hi I am Baymax, I woke Up")
        Vars.x = True
        listen()
        action(Vars.queue.deque())

    elif "search" in Args:
        print("Executing command")
        gsearch()
        listen()
        action(Vars.queue.deque())

    elif "sleep" in Args:
        print("Executing command")
        sleep()
        Speak("I am sleeping, Goodnight")
        Vars.x = False

    else:
        print("Transfering : "+ Args)
        Speak("Did not understand command "+Args)
        listen()
        action(Vars.queue.deque())