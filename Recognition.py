import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
m = sr.Microphone()

def listen():
    with m as source:
        #print("Wait")
        r.adjust_for_ambient_noise(source, duration=0.5)
        print("say something")
        audio = r.listen(source)
        try:
            mytext = r.recognize_google(audio)
            #print("you said "+mytext)
            return mytext
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError as e:
            print("errpr: {0}".format(e))

