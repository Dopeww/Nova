import os
import re
from playsound import playsound
import eel
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit

#Playing assistant sound function

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\mic start sound.mp3"
    playsound(music_dir)


def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    if query!="":
        speak("Opening "+query) #if query is not empty then it will speak.
        os.system('start '+query)
    else:
        speak("not found")

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+ " on YouTube")
    kit.playonyt(search_term)

def extract_yt_term(command):
 ##### DEFINES A REGULER EXPRESSION PATTERN TO CAPTURE THE SONG NAME #####
    pattern = r'play\s+(.*?)\s+on\s+youtube'
#####  Use re.search to find the match in the command #####
    match = re.search(pattern, command, re.IGNORECASE)
#####  If a match is found, return the extracted song name; otherwise, return None
    return match.group(1)