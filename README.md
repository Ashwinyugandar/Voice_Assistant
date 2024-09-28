Voice Assistant: Wall-E 1.0
Overview
Wall-E 1.0 is a Python-based voice assistant that can perform a variety of tasks, such as searching the web, sending emails, playing music, giving jokes, capturing photos, and much more. It is also integrated with WolframAlpha for calculations and Google’s Generative AI model for generating responses based on user queries.

Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x
pip (Python package installer)
Installation
Clone the repository or download the project files.

Install the necessary Python packages using the following command:

bash
Copy code
pip install wolframalpha pyttsx3 wikipedia pyjokes winshell feedparser smtplib requests speech_recognition twilio clint ecapture BeautifulSoup4 pyaudio google-generativeai
Note: You may need additional system-specific packages for some functionalities, such as pyaudio and winshell.

Usage
Configure API Keys

WolframAlpha: Replace the app_id variable in the code with your WolframAlpha API key.
Google Generative AI: Replace the api_key variable with your API key from Google.
Run the Program

Once all dependencies are installed and API keys are configured, you can run the assistant with:

bash
Copy code
python voice_assistant.py
Voice Commands

Wall-E 1.0 listens to your voice commands and responds accordingly. Here are some example commands:

"Open YouTube"
"Search Wikipedia for Albert Einstein"
"Play music"
"What's the time?"
"Send an email to [recipient's name]"
"Tell me a joke"
"Take a photo"
"Shutdown Windows"
Interaction

The assistant can save your name and remember it for future interactions. It will ask for your name the first time you run it or if you wish to change the saved name.

Features
Web Search: Search on YouTube, Google, and Wikipedia.
Music Playback: Plays songs from the specified music directory.
Time Announcement: Tells you the current time.
Email Sending: Send an email using the configured SMTP server.
WolframAlpha Integration: Performs calculations using WolframAlpha.
Google Generative AI: Generates responses for undefined queries.
Jokes: Tells jokes from the pyjokes library.
Windows Commands: Lock, shutdown, or restart your system.
Camera: Take a photo using your webcam.
Voice Commands Recognition: Uses speech_recognition to understand user commands.
Modules Used
subprocess: Execute system commands.
wolframalpha: Interface with WolframAlpha API for calculations.
pyttsx3: Text-to-speech conversion.
wikipedia: Fetch summaries from Wikipedia.
webbrowser: Open web pages in a browser.
os: Interface with the operating system for file operations.
pyjokes: Tells jokes.
winshell: Perform tasks like emptying recycle bin.
smtplib: Send emails using an SMTP server.
ctypes: Perform system-level tasks like changing wallpaper or locking the screen.
speech_recognition: Recognize voice commands using the microphone.
ecapture: Take photos with the webcam.
google.generativeai: Generate intelligent responses using Google's Generative AI model.
And many more...
Notes
Ensure your system's microphone and speakers are functioning correctly for optimal interaction with the voice assistant.
The takeCommand() function is designed to recognize English (India) accents. Modify the language code if you're using a different accent.
The program currently runs in a terminal environment and can be improved with a GUI for more user-friendly interaction.
Future Improvements
GUI Integration: Add a graphical user interface using Tkinter or PyQt.
Multilingual Support: Extend the assistant to support multiple languages.
Extended Functionalities: Add more APIs for tasks like weather updates, calendar events, or task management.
Credits
Developed and maintained by Ashwin Yugandar.

