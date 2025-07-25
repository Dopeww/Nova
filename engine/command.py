import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    eel.DisplayMessage(text)
    #print(voices) #This is for the voices that can be changed.
    engine.say(text) #this will speak the texts that we will be giving
    engine.runAndWait() #for delays

def takecommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening....')
        eel.DisplayMessage('Listening....')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language= 'en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        #time.sleep(2)
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands():

    query = takecommand()
    print(query)

    if "open" in query:
        from engine.features import opencommand
        opencommand(query)
    elif "on youtube":
        from engine.features import PlayYoutube
        PlayYoutube(query)
    else:
        print("not run")

    eel.ShowHood()