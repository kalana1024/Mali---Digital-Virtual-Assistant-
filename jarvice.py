import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import time
import pyautogui
import pykeyboard as k
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import sys
import subprocess
from bs4 import BeautifulSoup
import requests
import json



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#convert voice to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("say that it again sir")
        return "none"
    return query

#wishing
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<=18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am mali sir. please tell me how can i help you")

#send email
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('kalanasampath10@gmail.com', 'KalanaS@1024')
    server.sendmail('kalanasampath10@gmail.com', to, content)
    server.close()

#news
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=07b8645beddd44dcb06410d15fa70998'

    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")






if __name__ == "__main__":
    wish()
    while True:
    #if 1:
        query = takecommand().lower()

        #logics for tasks

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open pycharm" in query:
            npath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.5\\bin\\pycharm.exe"
            os.startfile(npath)

        elif "open visual studio" in query:
            npath = "C:\\Program Files\\Microsoft VS Code\\electron.exe"
            os.startfile(npath)

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
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" and "know about" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "open google" in query:
            speak("what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+94771526855", "this is testing protocol", 8, 38)
            time.sleep(120)
            speak("message has been sent")

        elif "play song on youtube" in query:
            speak("what should i search on youtube")
            cm = takecommand().lower()
            kit.playonyt(f"{cm}")

        elif "send email" in query:
            speak("sir what should i say")
            query = takecommand().lower()
            if "send file" in query:
                email = 'kalanasampath10@gmail.com'
                password = 'KalanaS@1024'
                send_to_email = 'charukasewmini7@gmail.com'
                speak("what should i type on subject")
                query = takecommand().lower()
                subject = query
                speak("what is the message for this email")
                query2 = takecommand().lower()
                message = query2
                speak("enter your attachment path sir")
                file_location = input ("please enter the path here: ")

                speak("please wait, i am sending the email")

                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = send_to_email
                msg['Subject'] = subject

                msg.attach(MIMEText(message, 'plain'))

                filename = os.path.basename(file_location)
                attachment = open(file_location, "rb")
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= %s " % filename)

                msg.attach(part)

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)
                text = msg.as_string()
                server.sendmail(email, send_to_email, text)
                server.quit()
                speak("email has been sent to sewmini")

            else:
                email = 'kalanasampath10@gmail.com'
                password = 'KalanaS@1024'
                send_to_email = 'charukasewmini70@gmail.com'
                message = query

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email, password)

                server.sendmail(email, send_to_email, message)
                server.quit()
                speak("email has been sent to sewmini")






        elif "shutdown" in query:
            speak("Your machine is shutting down now.")
            subprocess.run(["shutdown", "-s"])
            sys.exit()

        elif "restart" in query:
            os.system('shutdwon /s /t 5')
            speak("your machine is rebooting now")

        elif "sleep" in query:
            speak("your machine is sleeping now")
            os.system("rundll32.exe powrprof.dll, SetSuspendState 0, 1, 0")
            sys.exit()


        elif "no thanks" in query:
            speak("thank you for using me sir. have a nice day")
            sys.exit()

        #close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "close command prompt" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im cmd")

        elif "switch the window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "news" in query:
            speak("getting latest news for you sir")
            news()

        else:
            speak("Searching on google..")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")





        speak("do you have any other works sir")

else:
    speak("can you say it again sir.")