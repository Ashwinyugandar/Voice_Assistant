# Voice Assistant "Wall-E 1.0"
This project is a Python-based voice assistant named "Wall-E 1.0". The assistant can perform various tasks such as searching Wikipedia, playing music, telling jokes, and much more. It utilizes multiple libraries and APIs to handle tasks related to speech recognition, natural language processing, web browsing, sending emails, and interacting with external devices.

## Features
* Voice interaction with the user
* Web search using Google and Wikipedia
* Email sending functionality
* Play music from a predefined folder
* Tell jokes using the pyjokes library
* Retrieve the current time
* Lock and shutdown Windows
* Change the background wallpaper
* Launch PowerPoint presentations
* Take a photo using the camera
* Integration with WolframAlpha for computational queries   
* AI-driven responses for other questions using Google's Gemini-1.5 Flash model

## Installation

### Prerequisites

Install Latest Version of Python3

Before you can run the assistant, ensure that you have the following Python modules installed:

* subprocess: Execute system commands.
* wolframalpha: Interface with WolframAlpha API for calculations.
* pyttsx3: Text-to-speech conversion.
* wikipedia: Fetch summaries from Wikipedia.
* webbrowser: Open web pages in a browser.
* os: Interface with the operating system for file operations.
* pyjokes: Tells jokes.
* winshell: Perform tasks like emptying recycle bin.
* smtplib: Send emails using an SMTP server.
* ctypes: Perform system-level tasks like changing wallpaper or locking the screen.
* speech_recognition: Recognize voice commands using the microphone.
* ecapture: Take photos with the webcam.
* google.generativeai: Generate intelligent responses using Google's Generative AI model.

Install the necessary Python packages using the following command:
```
pip install wolframalpha pyttsx3 wikipedia pyjokes winshell feedparser smtplib requests speech_recognition twilio clint ecapture BeautifulSoup4 pyaudio google-generativeai

```

### Usage

1. Configure API Keys

    * WolframAlpha: Replace the app_id variable in the code with your WolframAlpha API key.
    
    * Google Generative AI: Replace the api_key variable with your API key from Google.
2. Run the Program

    Once all dependencies are installed and API keys are configured, you can run the assistant with:

    ```python voice_assistant.py```


### Notes
* Ensure your system's microphone and speakers are functioning correctly for optimal interaction with the voice assistant.
* The takeCommand() function is designed to recognize English (India) accents. Modify the language code if you're using a different accent.
* The program currently runs in a terminal environment and can be improved with a GUI for more user-friendly interaction.

### Future Improvements
* GUI Integration: Add a graphical user interface using Tkinter or PyQt.
* Multilingual Support: Extend the assistant to support multiple languages.
* Extended Functionalities: Add more APIs for tasks like weather updates, calendar events, or task management.


### Credits
Developed and maintained by Ashwin Yugandar.

