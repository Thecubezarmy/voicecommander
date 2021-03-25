import onetimettsmod as tts
import datetime
import speech_recognition as sr
import os
import pyaudio
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import webbrowser
chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
x = 1
#gets volume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

while x == 1:
#useless volume function
    def getvolume():
        currentVolume = volume.GetMasterVolumeLevel()
        return currentVolume
    
    volcheck = getvolume()
#When current volume is changed
    if getvolume() != volcheck:
#initialize the recognizer
        r = sr.Recognizer()
#defines the source of the recognizer
        with sr.Microphone() as source:
            tts.onetimetts("yes?")
            audio = r.listen(source)
            volcheck = getvolume() #makes it so that the script can run multiple times
        try:
#the voice commands
            if "EXAMPLE" in r.recognize_google(audio):
                tts.onetimetts("EXAMPLE")
                os.startfile(
                    "PATH")
            elif "test" in r.recognize_google(audio):
                tts.onetimetts("TEST")
            elif "search" in r.recognize_google(audio): #the search command initalises the recogniser again for a custom search
                
                tts.onetimetts("What should i  search?")
                with sr.Microphone() as source:
                    audio = r.listen(source)
                try:
                    if r.recognize_google(audio) != "":
                        search_query = r.recognize_google(audio)
                        print(search_query)
                        search = "https://duckduckgo.com/?q="+ search_query
                        webbrowser.get(chromePath).open(search)
                except sr.UnknownValueError:
                    tts.onetimetts("I did not get that")
        except sr.UnknownValueError:
            tts.onetimetts("I did not get that")
