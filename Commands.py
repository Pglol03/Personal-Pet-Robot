from Speech import Speak
from display import wakeup, sleep, dog

def action(Args):
    if "Lego" in Args:
        print("Input recognised")
        Speak("Hello Avyansh")
        
    elif "wake up" in Args:
        print("Executing command")
        wakeup()
        Speak("Hi I am Lego, I woke Up")

    elif "dog" in Args:
        print("Executing command")
        dog()
        Speak("Hi I am Lego, I woke Up")

    elif "sleep" in Args:
        print("Executing command")
        sleep()
        Speak("I am sleeping, Goodnight")

    else:
        print("Transfering : "+ Args)
        Speak(Args)