# importing all madules required
import pyttsx3
import datetime
from pygame import mixer

# Download source mp3 file from this link  
#https://klingeltonemp3.info/ding-dong-clock.htm

# intialising engine 
engine = pyttsx3.init('sapi5')
# declaring voices variable to change voice if required
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id) #for male voice
#engine.setProperty('voice', voices[0].id) #for female voice

# defining speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# defining wish me function
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir")

    else:
        speak("Good Evening sir")

# defining alarm function
def alarm(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    if stopper=="stop":
        mixer.music.stop()





# main function 
if __name__ == '__main__':
    # writing our logic
    while True:
        wishMe()
        speak('I am alarm ai sir. Please tell me ur alarm')

        break

    
    year=datetime.datetime.now().year

    
    month =datetime.datetime.now().month

    
    day = datetime.datetime.now().day

    speak("tell me the hour")
    hour = int(input("Enter here\n"))

    speak("tell me the minute")
    minutes = int(input("Enter here\n"))

    speak("can u tell me what's your message")
    message =str(input("Enter here\n"))

    speak("Remember done is the stopper")
    print("Remember done is the stopper")

    speak("thank u sir the alarm will ring when its time")
    while True:
        stopper1=""
        if year ==datetime.datetime.now().year and month==datetime.datetime.now().month and day==datetime.datetime.now().day and hour==datetime.datetime.now().hour and minutes==datetime.datetime.now().minute:
            speak(f"{message}")
            
                

                
                
            alarm("Ding Dong Clock.mp3", stopper1)
            stopper1=input("Enter here: ")
            if stopper1=="done":
                break	        