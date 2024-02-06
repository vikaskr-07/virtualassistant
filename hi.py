import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
from requests import get
import wikipedia
import pywhatkit as kit
import smtplib
import sys
import pyjokes


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio)
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please.....")
        return "none"
    return query


def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am jarvis tell me how can i help you")


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikaskum0ar@gmail.com', 'vikas12345@')
    server.sendmail('your mail id', to, content)
    server.close()


if __name__ == "__main__":
    # speak("hii hello")
    wish()
    while True:
        query = takecommand().lower()

        if "open chrome" in query:
            cr = "C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
            os.startfile(cr)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "E:\\songs"
            songs = os.listdir(music_dir)
            for song in songs:
                if song.endswith('.mp3'):
                    os.startfile(os.path.join(music_dir, song))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia...")
            speak(results)
            print(results)

        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("www.facebook.com")

        elif "open linkedin" in query:
            speak("opening linkedin")
            webbrowser.open("www.linkedin.com")

        elif "open google" in query:
            speak("sir what do I search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+916204042821", "kyaa re bhikmangya", 20, 13)

        elif "search songs on youtube" in query:
            kit.playonyt("see you again")

        elif "send email to vikas" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "vikaskum1ar@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir i am not able to send this email")

        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day")
            sys.exit()

        elif "close chrome" in query:
            speak("closing chrome sir")
            os.system("taskkill /f /im chrome.exe")

        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn == 00:
                speak(f"alarm is set at {nn}")
                music_dir = "E:\\songs"
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[1]))

        elif "tell me a joke" in query:
            jk = pyjokes.get_joke()
            speak(jk)

        elif "shut down the system" in query:
            os.system('shutdown /s /t 5')
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.dll, SetSuspendState 0,1,0")

        speak("sir, do you have any other work")