import pyttsx3
import json
import brain
import speech_recognition as sr



        
#engine.say("Personal assistant boot up sequence complete.")

boot = brain.random_welcome("boot")
brain.speak(boot)
brain.wishMe()

while True: 
    query = brain.takeCommand().lower()

