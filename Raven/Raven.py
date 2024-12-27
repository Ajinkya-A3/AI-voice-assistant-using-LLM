from Brain.brain import AIreply
from Body.speech import takeCommand, speak, greet
from Main import MainTaskexe
import sys
def TaskExecution():
    greet()

    while True:
        Data=takeCommand()
        Data=str(Data).lower()

        valuereturned = MainTaskexe(Data)
        
        if valuereturned==True:
            pass
        elif Data=="none" :
            pass
        elif Data=="sleep"  :
            speak("hybernating ....")
            break
        else:
            reply = AIreply(Data)
            speak(reply)

def wake_up():    
    while True:
        hotword = takeCommand()
        if "wake up" in hotword:
            TaskExecution()        
        elif "quit" in hotword:
            speak("it was my pleasure helping you. have a good day")
            sys.exit()
        
     
if __name__ == "__main__":

    wake_up()             


