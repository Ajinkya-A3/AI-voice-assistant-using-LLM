import datetime
import os
import time
import webbrowser as web
import psutil
import pyperclip
import pywhatkit
import wikipedia
from keyboard import press_and_release
from pyautogui import click
from pytube import YouTube

from requests import get

from Body.speech import greet, speak, takeCommand


def google_search():

    speak("what you want to search on google")
    query = takeCommand().lower()
    query = query.replace("raven", "")
    query = query.replace("what is", "")
    query = query.replace("what are",  "")
    query = query.replace("what is the meaning of", "")

    web.open_new_tab(f"{query}")




  

def youtube_search(query):
    result ="https://www.youtube.com/results?search_query="+query
    web.open(result)
    speak("this is what i found for you")
    pywhatkit.playonyt(query)
    speak("this may also help you.")

def download_yt():
    time.sleep(5)

    click(x=1290, y=66)

    press_and_release('ctrl + c')

    time.sleep(4)

    value = pyperclip.paste()

    Link = str(value)

    def download(link):
        url = YouTube(link)

        video = url.streams.get_highest_resolution()

        video.download('E:\\project\\Virtual_Assistant\\DataBase\\YT_vids')

    download(Link)

    speak("video has been downloaded successfully")
    speak("opening in file location")

    os.startfile('E:\\project\\Virtual_Assistant\\DataBase\\YT_vids')

def baterry():
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"our system have  {percentage}  percent battery")
    if percentage >= 75:
        speak("we have enough power to continue our work")
    elif percentage >= 40 and percentage < 75:
        speak("we have moderate amount of battery remaining")
    elif percentage >= 20 and percentage < 40:
        speak("we have low power we need to charge our device")
    else:
        speak("we have very low power our system will shut down shortly")


def wiki(query):
    speak("what should i search on wikipedia....")
    query =takeCommand().lower()

    results = wikipedia.summary(query, sentences=2)
    speak("according to wikipedia")
    speak(results)

def ip():

        ip = get('https://api.ipify.org').text
        speak(f"your IP address is : {ip}")

def notepad():

    speak("im ready to write .")


    writes = takeCommand()

    time = datetime.datetime.now().strftime("%H:%M")

    filename = str(time).replace(":","-") + "-note.txt"

    with open(filename,"w") as file:

        file.write(writes)
    path_1 = 'E:\\project\\Virtual_Assistant\\' + str(filename)

    path_2 = "E:\\project\\Virtual_Assistant\\DataBase\\Notepad\\" + str(filename)

    os.renames(path_1, path_2)

    os.startfile(path_2)

def songs():
    import random
    s_dir ='E:\\project\\Virtual_Assistant\\DataBase\\Songs'
    songlist = os.listdir(s_dir)
    i= random.randint(len(songlist))

    os.startfile(os.path.join(s_dir,songlist[i]))




















