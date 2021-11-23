import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
import requests
import time
import pyowm
import pyjokes
import cv2
import sys
import instaloader
import pyautogui
#from Emailsser.message import EmailMessage
email_list = {'JK':'jaya23krishna2000@gmail.com','yesh':'yeshwanthyadav550@gmail.com','aqib':'akib9985868716@gmail.com','mam':'bommareddysindhuja@gmail.com'}
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-50)
volume = engine.getProperty('volume')
engine.setProperty('volume',volume+50)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    #print(speak)
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("hello Good morning surya ")
        speak("hello Good morning surya")

    elif hour>=12 and hour<16:
        print(" hello Good Afternoon surya")
        speak("hello Good Afternoon surya")

    elif hour>=16 and  hour<19:
        print("hello Good evening surya")
        speak("hello Good evening surya")

    elif hour>=19 and  hour<22:
        print("It's dark outside surya")
        speak("It's dark outside surya")

    else:
        print("surya it's late please go to bed.......Good night surya")
        speak("surya it's late please go to bed.......Good night surya")
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing ....")
        query = r.recognize_google(audio, language='en-in')
        print( f"User said: {query} \n")
    except Exception as e:
        print("say that again Boss ........")
        return "None"
    return query
'''
def sendEmail(to,subject,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('RiotSurya.07@gmail.com','Riotsurya0706')
    email = EmailMessage()
    email['From'] = 'RiotSurya.07@gmail.com'
    email['To'] = to
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    #server.sendmail('RiotSurya.07@gmail.com',to,content)
    server.close()
'''
if __name__== "__main__":
    #speak("hello ")
    wishMe()
    speak("what can i do for u ......\n")
    '''
    print(" TRY SAYING.......\n"
          "open youtube \n"
          "open google \n"
          "weather today \n"
          "today news \n"
          "restart laptop \n"
          "shutdown laptop \n"
          "open web whatsapp  \n"
          "open instagram \n"
          "play music in youtube \n"
          "open gmail \n"
          "the time \n"
          "send mail \n"
          "wikipedia \n"
          "open notepad \n"
          )
    speak("Choose the above commands....i can perform ")
    '''
    while True:
    #if 1:
         query = takeCommand().lower()
         if 'who is ' in query:
             speak('gathering information....')
             query = query.replace("who is","")
             results = wikipedia.summary(query,sentences=5)
             speak("according to wikipedia")
             speak(results)
         elif 'open youtube' in query:
             webbrowser.open("https://www.youtube.com/")
             speak("opening youtube boss")
         elif 'open google' in query:
            speak("sir,what should i search for u")
            opp = takeCommand().lower()
            webbrowser.open(f"{opp}")
         elif 'open stackoverflow' in query:
             webbrowser.open("https://stackoverflow.com/")
             speak("opening stack overflow ")
         elif 'open web whatsapp' in query:
             webbrowser.open("https://web.whatsapp.com/")
             speak(" opening web whatsapp ")
         elif 'open instagram' in query:
             webbrowser.open("https://www.instagram.com/")
             speak(" opening instagram ")
         elif 'play ' in query:
             song = query.replace('play', '')
             speak('playing' + song)
             pywhatkit.playonyt(song)
         elif 'time' in query:
             strTime =datetime.datetime.now().strftime("%I:%M %p")
             speak(f"the time is {strTime}")
         elif 'open notepad' in query:
             notePath ="C:\\Windows\\system32\\notepad.exe"
             os.startfile(notePath)
         elif 'open command prompt' in query:
              os.system("start cmd")
              #STARTS
         elif 'open camera' in query:
             cap =cv2.VideoCapture(0)
             while True:
                 ret,img =cap.read()
                 cv2.imshow('webcam',img)
                 k = cv2.waitKey(50)
                 if k==27:
                     break ;
             cap.release()
             cv2.destroyAllWindows()
         elif 'open gmail' in query:
             webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl&pli=1#inbox")
         elif 'restart laptop' in query:
             speak("restarting the laptop ")
             os.system("shutdown /r /t 0 ")
         elif 'shutdown laptop' in query:
             speak("Shutting down the laptop ")
             os.system("Shutdown /s /t 0")
         elif 'sleep the system' in query or 'sleep completely' in query:
             speak("Sleep mode on")
             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
         elif 'joke' in query:
             j = pyjokes.get_joke()
             print(j)
             speak(j)
         elif 'today news' in query or ' todays news' in query:

            speak("what category news do u like to hear")
            print("1. science news \n"
                  "2. technology news \n"
                  "3. sports news \n"
                  "4. entertainment news \n"
                  "5. health news \n"
                  "6. business news \n"
                  "7. top headlines \n"
                  )
            speak("1. science news \n"
                  "2. technology news \n"
                  "3. sports news \n"
                  "4. entertainment news \n"
                  "5. health news \n"
                  "6. business news \n"
                  "7. top headlines \n")
            query1 = takeCommand().lower()

            if 'top headlines' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
            elif 'science news' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
            elif 'technology news' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
            elif 'sports news' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
            elif 'entertainment news' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
            elif 'health news' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
            elif 'business news' in query1:
                main_url = "http://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=3975a1d172f14e8e912f57dc1edeeb48"
                o = requests.get(main_url).json()
                # print(o)
                articles = o["articles"]
                result = []
                for a in articles:
                    result.append(a["title"])
                for i in range(2):
                    # time.sleep(2)
                    Headline = i + 1, result[i]
                    print(Headline)
                    speak(Headline)
         elif 'you can sleep now' in query or 'ok sleep now' in query:
             speak("thanks ....rest up sir ....i'll take a break")
             sys.exit()
         elif 'switch' in query or 'switch the tab' in query:
             pyautogui.keyDown("alt")
             pyautogui.press("tab")
             time.sleep(1)
             pyautogui.keyUp("alt")
         elif 'where am i' in query or 'where are we' in query:
             speak("wait sir ,let me check")
             try:
                 ipAdd = requests.get('http://api.ipify.org').text
                 print(ipAdd)
                 url='http://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                 geo_requests = requests.get(url)
                 geo_data =geo_requests.json()
                 city=geo_data['city']
                 country =geo_data['country']
                 region =geo_data['region']
                 speak(f"sir im not sure ,but i think we are in {region}region of {city} city of {country} country  ")
             except Exception as e:
                 speak("sorry sir ,due to bad internet connection i cant find your location")
                 pass
         elif 'instagram profile' in query or 'profile on instagram' in query:
             speak("sir please enter the username correctly")
             name= input("enter username here:")
             webbrowser.open(f"www.instagram.com/{name}")
             speak(f"here is the profile of the user {name}")
             time.sleep(5)
             speak("sir would you like to download the profile picture of this account")
             condition=takeCommand().lower()
             if "yes" in condition:
                 mod= instaloader.Instaloader()
                 mod.download_profile(name,profile_pic_only=True)
                 speak("i am done sir ,profile picture is saved ...now i'm ready for another command")
             else:
                 pass
         elif 'take a screenshot' in query or 'take screenshot' in query:
             speak("sir,please tell me the name for this screenshot file")
             name=takeCommand().lower()
             speak("please sir hold the screen for few seconds,i am taking screenshot")
             time.sleep(3)
             img=pyautogui.screenshot()
             img.save(f"{name}.png")
             speak("i am done sir,the screenshot is saved in our main folder.now i'm ready for another command")
         speak("Sir do u have any other work ")