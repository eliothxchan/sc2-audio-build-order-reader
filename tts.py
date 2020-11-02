import sys
import pyttsx3

def init_engine():
    engine = pyttsx3.init()
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
    engine.setProperty('rate', 225)
    return engine

def say(s):
    engine.say(s)
    engine.runAndWait()

engine = init_engine()
say(str(sys.argv[1]))