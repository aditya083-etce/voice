import sys
import speech_recognition as sr
import pyttsx3 as pyt
import pywhatkit as kit
import datetime
import wikipedia as wiki
import pyjokes
import webbrowser as wb
import os

engine = pyt.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 170)
vocal = engine.getProperty('voices')
engine.setProperty('voice', vocal[1].id)


def speak(tell):
    engine.say(tell)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("listening...")
            listener.pause_threshold = 1  # seconds of non-speaking audio before a phrase is considered complete
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'cami' in command:
                command = command.replace('cami', '')
    except:
        pass
    return command


def run_assistant():
    talk = listen()
    if 'how are you' in talk:
        speak('I am fine as I look. Thanks for asking')
    elif 'play' in talk:
        song = talk.replace('play', '')
        speak('Playing' + song)
        print(song)
        kit.playonyt(song)
    elif 'browse' in talk:
        search = talk.replace('browse', '')
        print(search)
        kit.search(search)
    elif 'talk about' in talk:
        info = talk.replace('talk about', '')
        print(info)
        information = wiki.summary(info, sentences=2)
        print(information)
        speak(information)
    elif 'time' in talk:
        time24 = datetime.datetime.now().strftime('%H:%M:%S')
        time12 = datetime.datetime.now().strftime('%I:%M %p')
        print(time24)
        print(time12)
        # speak('Current time is ' + time24)
        speak('Current time is ' + time12)
    elif 'date' in talk:
        speak('I will be happy to join u on a date but do were mask its Covid outside')
    elif 'single' in talk:
        speak('No, i am in a relationship with Internet and I also have an ex Google')
    elif 'joke' in talk:
        speak(pyjokes.get_joke())
    elif 'open visual studio code' in talk:
        speak('Opening' + talk.replace('open', ''))
        path = "C:\\Users\\adity\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
    elif 'open stremio' in talk:
        speak('Opening' + talk.replace('open', ''))
        path = "C:\\Users\\adity\\AppData\\Local\\Programs\\LNV\\Stremio-4\\stremio.exe"
        os.startfile(path)
    elif 'open steam' in talk:
        speak('Opening' + talk.replace('open', ''))
        path = "D:\\Steam\\steam.exe"
        os.startfile(path)
    elif 'open epic' in talk:
        speak('Opening' + talk.replace('open', ''))
        path = "D:\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"
        os.startfile(path)
    elif 'open command prompt' in talk:
        os.startfile("start cmd")
    elif 'open bash' in talk:
        speak('Opening' + talk.replace('open', ''))
        path = "C:\\Users\\adity\\AppData\\Local\\Programs\\Hyper\\Hyper.exe"
        os.startfile(path)
    elif 'open' in talk:
        browser = talk.replace('open', '')
        speak('Opening' + browser)
        print(browser.strip())
        wb.open(f"{browser.strip()}.com")
    elif 'shutdown' in talk:
        sys.exit()
    else:
        speak('Please repeat!')


def wishMe():
    timenow = int(datetime.datetime.now().hour)
    speak('Hi I am Cami Calibrated Automatic Mobil Interface')
    speak('Initial checks completed')
    speak('Backing up the configuration')
    speak('Initializing databases')
    speak('Establishing connection to satellite 8')
    if 0 <= timenow < 12:
        speak('Good Morning')
    elif 12 <= timenow < 18:
        speak('Good Afternoon')
    else:
        speak('Good Evening')

    speak('I am online and ready')
    speak('How can I help you')


if __name__ == '__main__':
    wishMe()
    while True:
        run_assistant()
