import json
import random
from random import randint
import pyttsx3
import speech_recognition as sr
import os 
import time
import datetime

data = {}

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def identityName():
    with open("memory.json") as json_file:
        data = json.load(json_file)
        memory = data["identity"]["name"]
        return memory
        
        
def identityNickname():
    with open("memory.json") as json_file:
        data = json.load(json_file)
        memory = data["identity"]["nickname"]
        return memory
        

def speak(audio): 
    engine.say(audio) 
    engine.runAndWait() 


def wishMe(): 
    hour = int(datetime.datetime.now().hour) 
    print(hour)
    if hour>= 5 and hour<12: 
        speak(random_welcome('morning')) 
   
    elif hour>= 12 and hour<18: 
        speak(random_welcome('afternoon'))    
   
    else: 
        speak(random_welcome('evening'))   


def takeCommand(): 
      
    r = sr.Recognizer() 
      
    with sr.Microphone() as source: 
          
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source) 
   
    try: 
        print("Recognizing...")     
        query = r.recognize_google(audio, language ='en-in') 
        print(f"User said: {query}\n") 
   
    except Exception as e: 
        print(e)     
        print("Unable to recognize your voice.")   
        return "None"
      
    return query

def random_welcome(category):
    ctg = category
    with open('memory.json') as json_file:
        data = json.load(json_file)
        memory = data["welcome"][ctg]
        random_index = randint(0,len(memory)-1)
        return memory[random_index]

def keyword_handler(sentence):
    name = identityName()
    nickname = identityNickname()
    text = sentence.lower()
    text = text.split(" ")
    if name or nickname in text:
        try:
            pos = text.index(name)
        except:
            pos = text.index(nickname)
        
    return pos
