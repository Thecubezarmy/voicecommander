
import os
import playsound
from gtts import gTTS
from random import *


def onetimetts(x):
    print('helo')
    s = x
    file = "FILE" + str(randint(0, 1000000000)) + ".mp3"
    tts = gTTS(s, 'com', "en")
    tts.save(file)
    playsound.playsound(file)
    os.remove(file)
