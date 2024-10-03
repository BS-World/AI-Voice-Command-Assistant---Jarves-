# Created by Bhanu Pratap Biswas

import speech_recognition as sr
import pyttsx3
import subprocess
import os
import platform
import psutil
import datetime

# Initialize the speech engine for text-to-speech
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I'm having trouble connecting to the internet.")
            return ""

def open_app(app_name):
    try:
        if platform.system() == 'Windows':
            os.startfile(app_name)
        else:
            subprocess.Popen(app_name)
        speak(f"Opening {app_name}")
    except Exception as e:
        speak(f"Sorry, I can't open {app_name}.")
        print(f"Error: {e}")

def close_app(app_name):
    try:
        if platform.system() == 'Windows':
            os.system(f"taskkill /im {app_name}.exe /f")
        else:
            os.system(f"killall {app_name}")
        speak(f"Closing {app_name}")
    except Exception as e:
        speak(f"Sorry, I can't close {app_name}.")
        print(f"Error: {e}")

def get_battery_status():
    battery = psutil.sensors_battery()
    speak(f"Battery is at {battery.percent} percent.")

def get_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}.")

# Example usage
if __name__ == "__main__":
    while True:
        command = listen()
        if "hi jarves" in command:
            speak("Hello sir, what can I do for you?")
        elif "what time is it" in command:
            get_time()
        elif "what is the battery" in command:
            get_battery_status()
        elif "open" in command:
            app_name = command.replace("open ", "")
            open_app(app_name)
        elif "close" in command:
            app_name = command.replace("close ", "")
            close_app(app_name)
        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break
