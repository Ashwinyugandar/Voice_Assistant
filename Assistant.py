# modules used for voice assistant 
import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
#import winshell
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import speech_recognition as sr
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
#import win32com.client as wincl
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif hour>12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    
    assistantname = "Wall-E 1 point o"
    speak("I am your Assistant")
    speak(assistantname)

def username():
    speak("What should i call you sir!")
    uname = takeCommand()
    speak(uname)
    columns = shutil.get_terminal_size().columns

    
    print("Welcome",uname.center(columns))
    speak("how can i help you")    

# def takeCommand():

#     r = sr.Recognizer()

#     with sr.Microphone() as source:
#         print("Listening...")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#             print(f"User said: {query}\n")

#         except Exception as e:
#             print(e)
#             print("Unable to Recognize Your Voice")
#             return "None"
    
#     return query

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}\n")

        except Exception as e:
            print(e)
            print("Unable to Recognize your voice.")
            return "None"

    return query

def sendemail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()

    server.login('codeashwin03@gmail.com','codeash03!')
    server.sendmail('codeashwin03@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    '''This Function Cleans the Terminal before
        any execution of this Python File'''
    clear()
    wishMe()
    username()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("searching wikipedia\n")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 3)
            print("According to wikipedia\n")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            print("opening youtube\n")
            speak("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            print("opening google")
            speak("opening google")
            webbrowser.open("google.com")

        elif 'play music' in query or 'play song' in query:
            speak("playing music")
            music_dir = "C:\\Users\\ashwi\\Music"
            if not os.listdir(music_dir):
                print("No Music Found")
            else:
                songs = os.listdir(music_dir)
                print(songs)
                random = os.startfile(music_dir,songs[1])
        
        elif 'the time' in query:
            currTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {currTime}")
        
        elif 'email to Ashwin' in query:
            try:
                speak("what should i mail")
                content = takeCommand()
                to = 'ashwins1609712@gmail.com'
                sendemail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("i am unable to send the email")

        elif 'how are you' in query:
            speak("i am fine thank you")
            speak("how are you sir")

        elif 'fine' in query or 'Good' in query:
            speak("its good to Know that You Are Fine")

        elif 'change my name to' in query:
            username()

        elif 'change your name' in query:
            speak("what would you like to call me")
            assistantname = takeCommand()
            speak("Thanks for naming me")
        
        elif "what's your name" in query or "what is your name" in query or "what should i call you" in query:
            speak(f"I am {assistantname}")

        elif 'exit' in query:
            exit()
        
        elif 'who created you' in query:
            speak("I was developed and Modified By Ashwin Yugandar")
        
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'calculate' in query :
            app_id = "YJE2L3-LXYQKKJGWA"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is"+answer)
            speak("The answer is"+answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search","")
            query = query.replace("play","")
            webbrowser.open(query)

        elif 'powerpoint presentation' in query:

            power = r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(power)
