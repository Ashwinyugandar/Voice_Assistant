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
import winshell
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
import win32com.client as wincl
from urllib.request import urlopen
import google.generativeai as Genai

api_key = ""
Genai.configure(api_key=api_key)

model = Genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=Genai.GenerationConfig(
        max_output_tokens=2048,
        temperature=0.7,
    ),
)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
assistantname = "Wall-E 1 point o"

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good morning ")
        speak("Good morning ")
    elif hour>12 and hour<18:
        speak("Good Afternoon ")
        print("Good Afternoon ")
    else:
        speak("Good Evening ")
        print("Good Evening ")
    
    
    speak("I am your Assistant")
    print("I am your Assistant")
    speak(assistantname)
    print(assistantname)

def loadusername():
    try:
        with open('username.txt',"r")as file:
            uname = file.read().strip()
            return uname
    except FileNotFoundError:
         return  None

def saveusername(uname):
    with open('username.txt',"w")as file:
        file.write(uname)


def username():
    
    speak("What should i call you")
    print("What should i call you")
    uname = takeCommand()
    speak(f"Hello{uname}")
    print("Welcome",uname)
    speak("how can i help you")  
    saveusername(uname)
    return  uname  

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
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

    server.login('example@gmail.com','password')
    server.sendmail('togmail@gmail.com',to,content)
    server.close()

if __name__ == '__main__':
    clear = lambda: os.system('cls')

    '''This Function Cleans the Terminal before
        any execution of this Python File'''
    clear()
    wishMe()
    uname = loadusername()
    if uname is None:
        uname = username()
    else:
        print(f"Welcome back,{uname}")
        speak(f"Welcome back,{uname}")
        speak("How can i help you")

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
            exit()

        elif 'open google' in query:
            print("opening google")
            speak("opening google")
            webbrowser.open("google.com")
            exit()

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
                to = 'toemail@gmail.com'
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
            app_id = ""
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

        elif 'change background' in query:
            ctypes.windll.user32.SystemParametersInfoW(20,0, "Location of wallpaper",0)

        elif 'lock windows'in query:
            speak('locking windows')
            print('locking windows')
            ctypes.windll.user32.LockWorkStation()
            exit()

        elif "restart" in query:
            print("restarting")
            speak("restarting")
            subprocess.call(["shutdown", "/r"])
        
        elif 'shutdown windows' in query:
            speak('are you sure you want me to shut down windows')
            print('are you sure you want me to shut down windows')
            print('if you are sure say |SHUTDOWN WINDOWS| Again')

            query = takeCommand().lower()

            if 'shutdown windows' in query:
                speak('shutting down windows')
                print('shutting down windows')
                subprocess.call('shutdown /p /f')
            else:
                print('No conformation provided!')
                speak('No conformation provided!')

        elif 'camera' in query or 'take a photo' in query or 'take picture' in query:
            ec.capture(0,"wall e camera","walleimg.png")
 
        else:
            response = model.generate_content(query)
            ans = response.text
            print (ans)
            speak(ans)
