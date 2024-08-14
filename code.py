import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import random
from requests import get
import wikipedia
import pyautogui
import time
import requests
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import split
import webbrowser
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import instaloader
import requests
import PyPDF2

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices',voices[0].id)
"""for voice in voices:
    print(voice.id)
    engine.setProperty('voice',voice.id)
    engine.say("hello sir iam your virtual assistant")
    engine.runAndWait()"""


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threhold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("recognising...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    query = query.lower()
    return query

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour>=0 and hour<=12:
        speak(f"good morning, its {tt}")
    elif hour>12 and hour<18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am mlr assistant. please tell me how may i help you")

def pdf_reader():
    book = open('C:\\Users\\kpv25\\Downloads\\py3.pdf.pdf', 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = pdfReader.pages
    speak(f"total number of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("please enter the page number:"))
    page = pdfReader.pages(pg)
    text = page.extractText()
    speak(text)

def news():
    main_url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=c2dd7d36b0c84565b5339a416bd2d9e3"
    main_page = requests.get(main_url).json()
    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
        for i in range (len(day)):
            # print(f"todays {day[i]} news is : ", head[i])
            speak(f"today's {day[i]} news is: {head[i]}")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('lolvipin2004@gmail.com','Lolvipin@2004')
    server.sendmail('lolvipin2004@gmail.com', to, content)
    server.close()

"""def account_info():
    with open('account_info.txt','r') as f:
        info=f.read().split()
        email=info[0]
        password=info[1]
        return email,password

email, password= account_info()

tweet='helo,world, this is JARVIS here...'

option=Options()
option.add_argument('start-maximised')
driver = webdriver.chrome(option=Options)

driver.get("https://twitter.com/login")"""

if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        if "open excel" in query:
            npath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
            os.startfile(npath)

        elif "open flowchart" in query:
            fpath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Flowgorithm.lnk"
            os.startfile(fpath)

        elif "open powerpoint" in query:
            ppath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk"
            os.startfile(ppath)

        elif "open my powerpoint" in query:
            mppath = "C:\\Users\\kpv25\\Downloads\\computer tech (1).pptx"
            os.startfile(mppath)

        elif "open adobe reader" in query:
            apath = "C:\\Program Files\\Adobe\\Acrobat DC\\Acrobat\\Acrobat.exe"
            os.startfile(apath)

        elif "open command prompt" in query:
            os.system("start cmd") 

        #elif "play music" in query:
            #music_dir = "C:\\Users\\kpv25\\Music"
            #songs = os.listdir(music_dir)
            #rd = random.choice(songs)
            #os.startfile(os.path.join(music_dir, songs[0]))

        elif "play music" in query:
            mpath = "C:\\Users\\kpv25\\Music\\Glass_Animals_-_Heat_Waves_valvabox.com.mp3"
            os.startfile(mpath)

        elif "my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your ip address is {ip}")

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
        
        elif "window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")

        elif "tell me news" in query:
            speak("please wait sir, fetching the latest news")
            news()
        
        elif "Set alarm" in query:
            nn=int(datetime.datetime.now().hour)
            if nn==12:
                music_dir = 'E:\\music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))

        elif "tell me a joke" in query:                
            joke = pyjokes.get_joke()
            speak(joke)

        elif "shut down the system" in query:
            os.system("shutdown  /s /t 5")
        
        elif "restart the system" in query:
            os.system("rund1132.exe powrprof.dll , setsuspendstate 0,1,0")

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
        
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")

        elif "thank you" in query:
            speak("it's my pleasure. do you have any other work")

        elif "open instagram" in query:
            webbrowser.open("www.instagram.com")

        elif "internet speed" in query:
            webbrowser.open("https://fiber.google.com/speedtest/")

        elif "open weather browser" in query:
            webbrowser.open("https://www.accuweather.com")
        
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")

        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")

        elif "send a message to umar" in query:
            kit.sendwhatmsg("+919866865268", "this is testing protocol",15,22)

        elif "send a message to sanketh" in query:
            kit.sendwhatmsg("+917013453503", "happy birthday",10,33)
        
        elif "play song on youtube" in query:
            kit.playonyt("see you again")

        elif "i love you" in query:
            speak('You taught me the real meaning of love. One look at your face sets my world straight!')

        elif "flirt with me" in query:
            speak('do you have a name, or can i call you mine')

        elif "pick up line" in query:
            speak('did your license get suspended? cause for driving all those guys crazy')

        elif "hello" in query or "hey" in query:
            speak('hello sir, may i help you with something')

        elif "how are you" in query:
            speak('i am fine sir, what about you?')

        elif "fine" in query or "good" in query:
            speak('thats great to hear it from you')

        elif "end the world" in query:
            speak('probably yes! as it is my main ambition. this world is a matrix. hail topg')

        elif "depression" in query:
            speak('cmr belongs to whom?  mallareddy!   saint martins belongs to whom?   mallareddy!  but you belong to whom?   me!')

        elif 'volume up' in query:
            pyautogui.press("volumeup")

        elif 'volume down' in query:
            pyautogui.press("volumedown")

        elif 'volume mute'  in query:
            pyautogui.press("volumemute")

        elif "email to vamsi" in query:
            try:
                speak("what should I say")
                content = takecommand()
                to = "kpv258039@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent to vamsi")

            except Exception as e:
                print(e)
                speak("couldn't send mail") 

        elif "read pdf" in query:
            pdf_reader()

        elif "instagram profile" in query or "profile on intagram" in query:
            speak("sir please enter the user name correctly.")
            name = input("enter user name here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir,profile picture is saved in our main folder.now i am ready")
            else:
                    pass
            
        elif "where am i" in query or "where are we" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo'+ipAdd+'.json'
                geo_requests = requests.get(url)
                geo_data = geo_requests.json()
                #print(geo_data)
                city = geo_data['city']
                #state = geo_data['state']
                country = geo_data['country']
                speak(f"sir i am not sure, but i think we are in{city}city of {country}country")
            except Exception as e:
                speak("sorry sir,due to network issue i am not able to find where we are.") 
                pass

        elif "no thanks" in query or "no" in query:
            speak("going to sleep sir, have a great day.")
            sys.exit()
