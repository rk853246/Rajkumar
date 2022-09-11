#Gui library
import tkinter as tk
from tkinter import END, Menu, Menubutton, PhotoImage, ttk
from tracemalloc import start
from PIL import Image, ImageTk
from itertools import count, cycle
from tkinter import Button, Label, Tk 

#main library
import pyttsx3
import requests
import datetime
import wikipedia
import webbrowser
import pywhatkit
import pyautogui
import keyboard
import pyjokes
import bs4
import os
import requests
import geocoder
import threading
import speech_recognition as sr
from geopy.distance import great_circle
from geopy.geocoders import Nominatim
from keyboard import write
from pyautogui import click
from time import sleep

focusBorderImageData = '''
        R0lGODlhQABAAPcAAHx+fMTCxKSipOTi5JSSlNTS1LSytPTy9IyKjMzKzKyq
        rOzq7JyanNza3Ly6vPz6/ISChMTGxKSmpOTm5JSWlNTW1LS2tPT29IyOjMzO
        zKyurOzu7JyenNze3Ly+vPz+/OkAKOUA5IEAEnwAAACuQACUAAFBAAB+AFYd
        QAC0AABBAAB+AIjMAuEEABINAAAAAHMgAQAAAAAAAAAAAKjSxOIEJBIIpQAA
        sRgBMO4AAJAAAHwCAHAAAAUAAJEAAHwAAP+eEP8CZ/8Aif8AAG0BDAUAAJEA
        AHwAAIXYAOfxAIESAHwAAABAMQAbMBZGMAAAIEggJQMAIAAAAAAAfqgaXESI
        5BdBEgB+AGgALGEAABYAAAAAAACsNwAEAAAMLwAAAH61MQBIAABCM8B+AAAU
        AAAAAAAApQAAsf8Brv8AlP8AQf8Afv8AzP8A1P8AQf8AfgAArAAABAAADAAA
        AACQDADjAAASAAAAAACAAADVABZBAAB+ALjMwOIEhxINUAAAANIgAOYAAIEA
        AHwAAGjSAGEEABYIAAAAAEoBB+MAAIEAAHwCACABAJsAAFAAAAAAAGjJAGGL
        AAFBFgB+AGmIAAAQAABHAAB+APQoAOE/ABIAAAAAAADQAADjAAASAAAAAPiF
        APcrABKDAAB8ABgAGO4AAJAAqXwAAHAAAAUAAJEAAHwAAP8AAP8AAP8AAP8A
        AG0pIwW3AJGSAHx8AEocI/QAAICpAHwAAAA0SABk6xaDEgB8AAD//wD//wD/
        /wD//2gAAGEAABYAAAAAAAC0/AHj5AASEgAAAAA01gBkWACDTAB8AFf43PT3
        5IASEnwAAOAYd+PuMBKQTwB8AGgAEGG35RaSEgB8AOj/NOL/ZBL/gwD/fMkc
        q4sA5UGpEn4AAIg02xBk/0eD/358fx/4iADk5QASEgAAAALnHABkAACDqQB8
        AMyINARkZA2DgwB8fBABHL0AAEUAqQAAAIAxKOMAPxIwAAAAAIScAOPxABIS
        AAAAAIIAnQwA/0IAR3cAACwAAAAAQABAAAAI/wA/CBxIsKDBgwgTKlzIsKFD
        gxceNnxAsaLFixgzUrzAsWPFCw8kDgy5EeQDkBxPolypsmXKlx1hXnS48UEH
        CwooMCDAgIJOCjx99gz6k+jQnkWR9lRgYYDJkAk/DlAgIMICZlizat3KtatX
        rAsiCNDgtCJClQkoFMgqsu3ArBkoZDgA8uDJAwk4bGDmtm9BZgcYzK078m4D
        Cgf4+l0skNkGCg3oUhR4d4GCDIoZM2ZWQMECyZQvLMggIbPmzQIyfCZ5YcME
        AwFMn/bLLIKBCRtMHljQQcDV2ZqZTRDQYfWFAwMqUJANvC8zBhUWbDi5YUAB
        Bsybt2VGoUKH3AcmdP+Im127xOcJih+oXsEDdvOLuQfIMGBD9QwBlsOnzcBD
        hfrsuVfefgzJR599A+CnH4Hb9fcfgu29x6BIBgKYYH4DTojQc/5ZGGGGGhpU
        IYIKghgiQRw+GKCEJxZIwXwWlthiQyl6KOCMLsJIIoY4LlQjhDf2mNCI9/Eo
        5IYO2sjikX+9eGCRCzL5V5JALillY07GaOSVb1G5ookzEnlhlFx+8OOXZb6V
        5Y5kcnlmckGmKaaMaZrpJZxWXjnnlmW++WGdZq5ZXQEetKmnlxPgl6eUYhJq
        KKOI0imnoNbF2ScFHQJJwW99TsBAAAVYWEAAHEQAZoi1cQDqAAeEV0EACpT/
        JqcACgRQAW6uNWCbYKcyyEwGDBgQwa2tTlBBAhYIQMFejC5AgQAWJNDABK3y
        loEDEjCgV6/aOcYBAwp4kIF6rVkXgAEc8IQZVifCBRQHGqya23HGIpsTBgSU
        OsFX/PbrVVjpYsCABA4kQCxHu11ogAQUIOAwATpBLDFQFE9sccUYS0wAxD5h
        4DACFEggbAHk3jVBA/gtTIHHEADg8sswxyzzzDQDAAEECGAQsgHiTisZResN
        gLIHBijwLQEYePzx0kw37fTSSjuMr7ZMzfcgYZUZi58DGsTKwbdgayt22GSP
        bXbYY3MggQIaONDzAJ8R9kFlQheQQAAOWGCAARrwdt23Bn8H7vfggBMueOEG
        WOBBAAkU0EB9oBGUdXIFZJBABAEEsPjmmnfO+eeeh/55BBEk0Ph/E8Q9meQq
        bbDABAN00EADFRRQ++2254777rr3jrvjFTTQwQCpz7u6QRut5/oEzA/g/PPQ
        Ry/99NIz//oGrZpUUEAAOw==
    '''

borderImageData = '''
        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
    '''
def start1():
    x = threading.Thread(target=Assistant_fun)
    x.start()

def Assistant_fun():
    label25.destroy()
    #button1.destroy()
    logo.destroy()

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    engine.setProperty('rate',170)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def wishme():
        global wishing
        global wishing1
        global wishing2
        global wishing3

        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            wishing=Label(window, text='Good Morning sir!',font=("Times", 16,'bold'),bg='white')
            wishing.place(x=200, y=90)
            speak("Good Morning sir")
            wishing.destroy()
        elif hour>=12 and hour<18:
            wishing1=Label(window, text='Good Afternoon sir!',font=("Times", 16,'bold'),bg='white')
            wishing1.place(x=200, y=90)
            speak("Good Afternoon sir")
            wishing1.destroy()
        else:
            wishing2=Label(window, text='Good evening sir!',font=("Times", 16,'bold'),bg='white')
            wishing2.place(x=200, y=90)
            speak("Good evening sir")  
            wishing2.destroy() 
        wishing3=Label(window, text='I am Zaara!, Please tell me how may i help you',font=("Times", 16,'bold'),bg='white')
        wishing3.place(x=70, y=125)
        speak("I am Zaara, Please tell me how may i help you")
        wishing3.destroy()

    def Whatsapp():
        speak("Tell me the name of the person!")
        name = takeCommand()
        if 'Rajkumar' in name or 'Rajkumar' in query2:
            inputtxt.delete('1.0', END)
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time, time in hours")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+919650778420",msg,hour,min,8)
            speak("Ok sir, sending whatsapp message!")
        if 'Shivam bhai' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+917999450233",msg,hour,min,7)
            speak("Ok sir, sending whatsapp message!") 
        if 'Gyanendra bhai' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+918920937299",msg,hour,min,7)
            speak("Ok sir, sending whatsapp message!") 

        if 'Wasim Khan' in name:
            speak("Tell me the message!")
            msg = takeCommand()
            speak("Tell me the time!")
            speak("Time in hour!")
            hour = int(takeCommand())
            speak("Time in minutes!")
            min = int(takeCommand())
            pywhatkit.sendwhatmsg("+917668778236",msg,hour,min,8)
            speak("Ok sir, sending whatsapp message!") 

    #Live corona cases
    def CoronaVrirus(country):
        global status5
        global status6
        global status7

        countries = str(country).replace(" ","")
        url = f"http://www.worldometers.info/corona/coronavirus/country/{countries}/"
        result = requests.get(url)
        soups = bs4.BeautifulSoup(result.text,'lxml')
        corona = soups.find_all('div',class_ = 'maincounter-number')
        Data = []
        for case in corona:
            span = case.find('span')
            Data.append(span.string)
        cases , Death , recovered = Data
        hide_labels()
        print(f"  Cases till now     : {cases}")
        status5=Label(window, text=f" Cases till now  : {cases}\n", justify='left', background='white', font=("Helvetica", 12,'bold'), fg='black')
        status5.place(x=180, y=120)
        speak(f"cases : {cases}")
        print(f"  Deaths till now    : {Death}")
        status6=Label(window, text=f" Deaths till now  : {Death}\n", justify='left', background='white', font=("Helvetica", 12,'bold'), fg='black')
        status6.place(x=180, y=150)
        speak(f"Deaths : {Death}")
        print(f"  Recovered till now : {recovered}")
        status7=Label(window, text=f" Recovered till now  : {recovered}\n", justify='left', background='white', font=("Helvetica", 12,'bold'), fg='black')
        status7.place(x=180, y=180)
        speak(f"Recovered : {recovered}")
        speak("Is there anything else i can do for you sir ?")
        status5.after(1000 , lambda: status5.destroy())
        status6.after(1000 , lambda: status6.destroy())
        status7.after(1000 , lambda: status7.destroy())

    #Note pad
    def Notepad():
        speak("Tell me the query .")
        speak("I am ready to wirte . ")   
        writes = takeCommand()
        time = datetime.datetime.now().strftime("%H:%M")
        filename = str(time).replace(":","-") + "-note.txt"
        with open(filename,"w") as file:
            file.write(writes)
        path_1 = "C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\ZARA 2.0\\output\\Zaramain\\" + str(filename)
        path_2 = "C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\notepad\\" + str(filename)
        os.rename(path_1,path_2)
        os.startfile(path_2)
        speak("Is there anything else i can do for you sir ?")

    #Google map automation
    def GoogleMaps(Place):
        global status8
        url_Place = "https://www.google.com/maps/place/" + str(Place)
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.geocode(Place,addressdetails=True)
        target_letlon = location.latitude , location.longitude
        webbrowser.open(url=url_Place)
        location = location.raw['address']
        target = {'city' : location.get('city',''), 'state' : location.get('state',''), 'country' : location.get('country','')}
        print(target)
        current_loca = geocoder.ip('me')
        current_latlon = current_loca.latlng
        distance = str(great_circle(current_latlon,target_letlon))
        distance = str(distance.split(' ',1)[0])
        distance = round(float(distance),2)
        print(f"sir , {Place} is {distance} Kilometer away from your location . ")
        status8=Label(window, text=f" Sir , {Place} is {distance} Kilometer away from your location . ",wraplength=550, justify='left', background='white', font=("Helvetica", 12,'bold'), fg='black')
        status8.place(x=70, y=120)
        speak(target)
        speak(f"sir , {Place} is {distance} Kilometer away from your location . ")  
        speak("Is there anything else i can do for you sir ?")
        status8.after(1000 , lambda: status8.destroy())

    #Closing app
    def ClossApp():
        speak("ok sir, wait a second!")
        if 'close google' in query:
            os.system("TASKKILL /F /im chrome.exe")
        elif 'close youtube' in query:
            os.system("TASKKILL /F /im msedge.exe")  
        elif 'close my sql' in query:
            os.system("TASKKILL /F /im mysql.exe")  
        elif 'close zoom meeting' in query:
            os.system("TASKKILL /F /im Zoom.exe")        
        elif 'close stack overflow' in query:
            os.system("TASKKILL /F /im msedge.exe")  

        elif 'microsoft edge' in query:
            os.system("TASKKILL /F /im msedge.exe") 
        elif 'close vs code' in query:
            os.system("TASKKILL /F /im Code.exe")   

        elif 'close pycharm' in query:
            os.system("TASKKILL /F /im pycharm64.exe")
        elif 'close intellij ide' in query:
            os.system("TASKKILL /F /im idea64.exe")  
        elif 'close vlc media' in query:
            os.system("TASKKILL /F /im vlc.exe")
                    
    def takeCommand():
        global status1
        global status2
        global status3
        global status4
    
        # It takes microphone input form the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("Listening....")
            status1=Label(window, text="Listening....", background='white',font=("Helvetica", 12,'bold'),fg='black' )
            status1.place(x=70, y=35)
            r.pause_threshold = 0.5
            r.energy_threshold = 2000
            audio = r.listen(source)
        try:
            print("Recognizing...")
            status2=Label(window, text="Recognizing...", background='white',font=("Helvetica", 12,'bold'), fg='black')
            status2.place(x=70, y=65)
            query = r.recognize_google(audio, language='en-in')   
            print(f"User said : {query}\n")
            status3=Label(window, text=f"User said : {query}\n",wraplength=550, justify='left', background='white',font=("Helvetica", 12,'bold'), fg='black')
            status3.place(x=70, y=95)
            status2.after(1000 , lambda: status2.destroy())
            status3.after(1000 , lambda: status3.destroy())
        except Exception as e:
            global status4
            # print(e)  
            print("Say it again please...")
            status4=Label(window, text="Say it again please...", justify='left', background='white', font=("Helvetica", 12,'bold'), fg='black')
            status4.place(x=70, y=120)
            status2.after(1000 , lambda: status2.destroy())
            status4.after(1000 , lambda: status4.destroy())
            return "None"
            
        return query 

    def hide_labels():
            status1.after(1000 , lambda: status1.destroy())
               
    if __name__ == "__main__":
        global status11
        security_img=Label(window,image=img6,bg='white')
        security_img.place(x=250, y=118)
        status11=Label(window, text="Please Write or Say Password", justify='left', background='white', font=("Helvetica", 18,'bold'), fg='Black')
        status11.place(x=120, y=280)
        speak("This particular system is password prtected, kindly provide the password to access")
        security_img.destroy()
        status11.destroy()
        while True:
            global status15
            security_img0=Label(window,image=img6,bg='white')
            security_img0.place(x=250, y=118)
            status15=Label(window, text="Please Write or Say Password", justify='left', background='white', font=("Helvetica", 18,'bold'), fg='Black')
            status15.place(x=120, y=280) 
            query = takeCommand().lower()
            query2 = inputtxt.get("1.0",'end-1c').lower()
            if 'this is a major project' in query or 'risp123' in query2:
                status15.destroy()
                security_img0.destroy()
                global status12
                global status13
                security_img2=Label(window,image=img8,bg='white')
                security_img2.place(x=265, y=125)
                status12=Label(window, text="Access Granted... ", justify='left', background='white', font=("Helvetica", 22,'bold'), fg='limegreen')
                status12.place(x=200, y=280)
                speak("accessd granted")
                security_img2.destroy()
                status12.destroy()
                hide_labels()
                inputtxt.delete('1.0', END)
                wishme()
                while True:
                    query = takeCommand().lower()
                    hide_labels()
                    query2 = inputtxt.get("1.0",'end-1c').lower() 
                    

                    # Logic for executing tasks based on query
                    if 'wikipedia' in query or 'wikipedia' in query2:
                        global Status10
                        speak('searching wikipedia....')
                        query = query.replace("wikipedia", "")
                        query = query2.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        print(results)
                        status10=Label(window, text=f" According to wikipedia  : {results}",wraplength=550, justify='left', background='white', font=("Helvetica", 12,'bold'), fg='black')
                        status10.place(x=70, y=70)
                        speak(results)
                        inputtxt.delete('1.0', END)
                        speak("Is there anything else i can do for you sir ?")
                        status10.after(1000 , lambda: status10.destroy())

                    elif 'open youtube' in query or 'open youtube' in query2:
                        webbrowser.open("youtube.com")
                        inputtxt.delete('1.0', END)
                        speak("ok! i'll open Youtube for you")

                    elif 'open google' in query or 'open google' in query2:
                        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                        inputtxt.delete('1.0', END)
                        speak("ok! i'll open google for you")
                        

                    elif 'stack overflow' in query:
                        webbrowser.open("stackoverflow.com")
                        speak("ok! i'll open stack overflow for you")

                    elif 'play music' in query or 'play music' in query2:
                        music_dir = 'D:\\Downloads\\music01'
                        songs = os.listdir(music_dir)
                        # print(songs)
                        os.startfile(os.path.join(music_dir, songs[13]))
                        inputtxt.delete('1.0', END)
                        speak("ok i'll play music for you")
                        

                    elif 'what is time now' in query or 'what is time now' in query2:
                        global status9
                        strTime = datetime.datetime.now().strftime("%H: %M: %S")
                        status9=Label(window, text=f"{strTime}\n", justify='left', background='white', font=("Helvetica", 34,'bold'), fg='black')
                        status9.place(x=200, y=207)
                        speak(f"sir, the time is {strTime}")
                        inputtxt.delete('1.0', END)
                        status9.after(1000 , lambda: status9.destroy())

                    elif 'open powerpoint' in query or 'open powerpoint' in query2:
                        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint 2016.lnk")
                        inputtxt.delete('1.0', END)
                        speak("ok! i'll open power point for you")
                        
                    elif 'open chrome' in query:
                        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
                        speak("ok! i'll open google chrome for you")

                    elif 'open my university website' in query:
                        webbrowser.open("gbu.ac.in")
                        speak("ok! i'll open your university website for you")
                    
                    elif 'open control panel' in query:
                        os.startfile("C:\\Users\\ik597\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\System Tools\\Control Panel.lnk")
                        speak("ok! i'll open control panel for you")

                    elif 'open ms word' in query:
                        os.startfile("C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\Word 2016.lnk")
                        speak("ok! i'll open microsoft word for you")

                    elif 'open notepad' in query:
                        os.startfile("C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\Notepad.lnk")
                        speak("ok! i'll open notepad for you")

            

                    elif 'open passport india portal' in query:
                        webbrowser.open("passportindia.org.in")
                        speak("ok! i'll open passport india portal for you")

                    elif 'open vs code' in query:
                        os.startfile("C:\\Users\\ik597\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
                        speak("ok i'll open visual studio code for you!")

                    elif 'open my sql' in query:
                        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\MySQL\\MySQL Server 8.0\\MySQL 8.0 Command Line Client.lnk")
                        speak("ok i'll open my sql for you") 

                    elif 'open zoom meeting' in query:
                        os.startfile("C:\\Users\\ik597\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
                        speak("ok i'll open zoom meeting for you")  

                    elif 'open pycharm' in query:
                        os.startfile("C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\pycharm64.exe")
                        speak("ok i'll open pycharm for you")

                    elif 'open microsoft edge' in query:
                        os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
                        speak("ok i'll open microsoft edge for you")  

                    elif 'open telegram' in query:
                        os.startfile("C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\Telegram Desktop.lnk")
                        speak("ok i'll open telegram for you") 

                    elif 'open this pc' in query:
                        os.startfile("C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\This PC.lnk") 
                        speak("ok i'll open this pc for you")  

                    #function fo this pc
                    elif 'open downloads' in query:
                        speak("ok")
                        os.startfile("D:\Downloads") 
                    elif 'close downloads' in query:
                        speak("ok")
                        keyboard.press_and_release('alt + up arrow')        

                    elif 'open intellij ide' in query:
                        os.startfile("C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.3.1\\bin\\idea64.exe") 
                        speak("ok i'll open intellij ide for you")  
                        
                    elif 'open vlc media' in query:
                        os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
                        speak("ok i'll open vlc for you")    
                    
                    elif 'joke' in query:
                        get = pyjokes.get_joke()
                        speak(get)   
                        speak("Is there anything else i can do for you sir ?") 

                    elif 'my location' in query:
                        speak("Ok sir , wait a second!")  
                        webbrowser.open('https://www.google.com/maps/@28.4238586,77.5229688,16z') 
                        speak("this is your location")

                    #whats app full automate
                    elif 'open whatsapp' in query or 'open whatsapp' in query:
                        os.startfile("C:\\Users\\ik597\\OneDrive\\Attachments\\Desktop\\WhatsApp Desktop.lnk")
                        speak("ok i'll open whatsapp for you") 
                    elif 'search name' in query:
                        click(x=326, y=139)
                        speak("to whome do you want to send the message")
                        search = takeCommand()
                        write(search)
                        sleep(1)
                        click(x=231, y=332)  
                        sleep(0.5)
                        click(x=750, y=978)
                        speak("give your message")
                        kkk = takeCommand()
                        write(kkk)
                        keyboard.press('enter')
                        speak("your message has been sent")
                        speak("Is there anything else i can do for you sir ?")

                            

                    #Repeat my words
                    elif 'repeat my words' in query:
                        speak("what do you want me to say")
                        jj = takeCommand()
                        speak(f"you said : {jj}")

                    # Live Corona cases
                    elif 'give me covid report' in query or 'give me covid report' in query2:
                        hide_labels()
                        inputtxt.delete('1.0', END)
                        speak("which countr's Information do you want ?")
                        cbc = takeCommand()
                        # query2 = inputtxt.get("1.0",'end-1c').lower()
                        CoronaVrirus(cbc)
                        # CoronaVrirus(query2)

                    #write on notepad
                    elif 'write a note' in query or 'write a note' in query2:
                        inputtxt.delete('1.0', END)
                        Notepad() 

                    elif 'where is' in query:
                        Place = query.replace("where is ","")
                        Place = Place.replace("hey zara ", "")
                        inputtxt.delete('1.0', END)
                        GoogleMaps(Place)    



                    #Close Applications
                    elif 'close youtube' in query:
                        ClossApp()    
                    elif 'close google' in query:
                        ClossApp()
                    elif 'close my sql' in query:
                        ClossApp()    
                    elif 'close zoom meeting' in query:
                        ClossApp()    
                    elif 'close ms word' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release('alt + f4')  
                    elif 'close media player' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release('alt + f4')     
                    elif 'close powerpoint' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release('alt + f4')    
                    elif 'close control panel' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release('alt + f4')
                    elif 'close whatsapp' in query:
                        speak("ok wait a second")   
                        keyboard.press_and_release('alt + f4') 
                    elif 'close telegram' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release("alt + f4")
                    elif 'close this pc' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release('alt + f4')  
                    elif 'close notepad' in query:
                        speak("ok wait a second")
                        keyboard.press_and_release('alt + f4')                  
                    elif 'close microsoft edge' in query:
                        ClossApp()    
                    elif 'close vs code' in query:
                        ClossApp()    
                    elif 'close pycharm' in query:
                        ClossApp()    
                    elif 'close intellij ide' in query:
                        ClossApp()  
                    elif 'close vlc media' in query:
                        ClossApp()         

                    #youtube search
                    elif 'youtube search' in query or 'youtube search' in query2:
                        speak("Ok sir, This is what i found for your search!")
                        query = query.replace("hey zara", "")
                        query = query.replace("hey sara", "")
                        query = query.replace("youtube search", "")
                        web = 'https://www.youtube.com/results?search_query=' + query
                        webbrowser.open(web)
                        speak("done sir!")

                    #Google search
                    elif 'google search' in query or 'google search' in query2:
                        speak("This is what i found for your search sir!")
                        query = query.replace("hey zara", "")
                        query = query.replace("hey sara", "")
                        query = query.replace("hijara", "")
                        query = query.replace("google search", "")
                        pywhatkit.search(query)  
                        speak("done sir!") 

                    #Open any wesite
                    elif 'open website' in query:
                        speak("Tell me the name of the website")
                        name = takeCommand()
                        name = name.replace(" ","")
                        web = 'https://www.' + name + '.com'
                        webbrowser.open(web)
                        speak("done sir!")

                    #play video on youtube
                    elif 'play video' in query:
                        speak("Tell me the name of the video!")
                        VideoName = takeCommand()
                        pywhatkit.playonyt(VideoName)
                        speak("your video has been started!, Enjoy sir!")   

                    #play song on youtube
                    elif 'play song' in query:
                        speak("Tell me the name of the song!")
                        SongName = takeCommand()
                        pywhatkit.playonyt(SongName)
                        speak("your song has been started!, Enjoy sir!")      

                    #Send message on whatsapp
                    elif 'send message on whatsapp' in query:
                        Whatsapp()

                    # Take screenshot
                    elif 'screenshot' in query:
                        speak("what should i name that file")
                        path = takeCommand()
                        pathname1 = path + ".png"
                        sc = pyautogui.screenshot()
                        sc.save('C:\\Users\\ik597\\OneDrive\\Pictures\\Screenshots\\' + pathname1)
                        #if want to watch screenshot
                        #os.startfile("C:\\Users\\ik597\\OneDrive\\Pictures\\Screenshots")
                        speak("Done sir")

                    #youtube automation  
                    elif 'pause' in query:
                        keyboard.press('space bar')
                    elif 'play' in query:
                        keyboard.press('k')
                    elif 'mute' in query:
                        keyboard.press('m')
                    elif 'skip' in query:
                        keyboard.press('l')
                    elif 'back' in query:
                        keyboard.press('j')
                    elif 'full screen' in query:
                        speak("OK")
                        keyboard.press('f')
                    elif 'remove full screen' in query:
                        speak("OK")
                        keyboard.press('esc')
                    elif 'go to mini player' in query:
                        keyboard.press('i')    
                    elif ' theatre mode' in query:
                        speak("OK")
                        keyboard.press('t')
                    elif 'go to next video' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + n')  
                    elif 'fast this video' in query:
                        speak("OK")
                        keyboard.press('shift + >')   
                    elif 'slow this video' in query:
                        speak("OK")
                        keyboard.press('shift + <')          
                    elif 'subtitle' in query:
                        speak("OK")
                        keyboard.press('c')
                    elif 'go to previous video' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + p') 
                    elif 'search in youtube' in query:
                        click(x=633, y=150)
                        speak("what do you want to search")
                        search = takeCommand()
                        write(search)
                        sleep(0.8)  
                        keyboard.press('enter')  
                        speak(f"this is the result of {search}")     

                    #chrome autommate
                    elif 'close this tab' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + w')
                    elif 'open new tab' in query:
                        speak("OK") 
                        keyboard.press_and_release('ctrl + t')
                        
                    elif 'open history' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + h')   
                    elif 'go to download' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + j') 
                    elif 'move down' in query:
                        keyboard.press('space bar') 
                    elif 'move up' in query:
                        keyboard.press_and_release('shift + space bar') 
                    elif 'go to top of the page' in query:
                        keyboard.press('home')   
                    elif 'go to bottom of the page' in query:
                        keyboard.press('end')       
                    elif 'open incognito mode' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + ctrl + n')
                    elif 'open new window' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + n') 
                    elif 'close current window' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + ctrl + w')  
                    elif 'reopen last window closed' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + ctrl + t')
                    elif 'go to next tab' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + tab')   
                    elif 'go to previous tab' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + ctrl + tab')
                    elif 'go to previous page in history' in query:
                        keyboard.press_and_release('alt + <')  
                    elif 'go to next page in history' in query:
                        keyboard.press_and_release('alt + >')   
                    elif 'maximize window' in query:
                        keyboard.press_and_release('alt + =')
                    elif 'minimize window' in query:
                        keyboard.press_and_release('alt + -')
                    elif 'page up' in query:
                        keyboard.press_and_release('alt + up arrow')   
                    elif 'page down' in query:
                        keyboard.press_and_release('alt + down arrow')  
                    elif 'print current page' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + p')    
                    elif 'save current page' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + s')  
                    elif 'reload current page' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + r')     
                    elif 'reset zoom level' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + o')  
                    elif 'stop loading my current page' in query:
                        speak("OK")
                        keyboard.press_and_release('esc')
                    elif 'save my current web as a bookmark' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + d') 
                        keyboard.press("enter") 
                    elif 'search on google' in query:
                        keyboard.press_and_release('ctrl + k')
                        speak("what do you want to search")
                        search = takeCommand()
                        write(search)
                        sleep(0.8)  
                        keyboard.press('enter') 
                        speak(f"this is the result of {search}")    
                    elif 'view page source' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + u')
                    elif 'bookmark' in query:
                        speak("OK")
                        keyboard.press_and_release('shift + ctrl + b')  # show and hide bookmark,
                    elif 'select everything on the page' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + a')  
                    elif 'select content in address bar' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + l')
                    elif 'copy selected content' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + c')
                    elif 'paste selected content' in query:
                        speak("OK")
                        keyboard.press_and_release('ctrl + v')    
                    elif 'undo my last action' in query:
                        keyboard.press_and_release('ctrl + z')
                    elif 'search in google' in query:
                        click(x=788, y=514)
                        speak("what do you want to search")
                        search = takeCommand()
                        write(search)
                        sleep(0.8)  
                        keyboard.press('enter')     
        
                        





                    # Talk to zara
                    elif 'what is your name' in query:
                        speak("My name is zaara")
                    elif 'open his PC' in query:
                        speak("I can't open")  
                    elif 'how are you' in query:
                        speak('I am fine, thanks. How about yourself') 
                    elif 'can you be my friend' in query:
                        speak('Of course, I am your VFF, virtual friend forever')  
                    elif 'my name is ibrahim khan' in query:
                        speak('hello ibrahim sir nice to meet you')
                    elif 'remember what is my name' in query:
                        speak('of course sir, you are ibrahim khan')  
                    elif 'thanks' in query:
                        speak("NO need sir!, its my duty!")



                    elif 'now you can go' in query or 'now you can go' in query2:
                        security_img0=Label(window,image=img9,bg='white')
                        security_img0.place(x=210, y=90)
                        speak("as you wish. remember me whenever you need me , bye sir!")
                        window.destroy()
                        exit()

                    elif 'shutdown' in query:
                        speak("do you really want me to turn off this coumputer?")
                        comm = takeCommand()
                        if (comm == 'yes'):
                            speak("ok as you wish")
                            speak("bye sir i am going to shutdown") 
                            keyboard.press_and_release('alt + f4')
                            keyboard.press('enter') 
                        else: 
                            speak("ok i am not turning off the computer")
                    elif 'restart' in query:
                        speak("do you really want me to restart this computer")
                        comm = takeCommand()
                        if (comm == 'yes'):
                            speak("ok sir! as you wish")
                            speak("bye sir! i am going to restart myself")
                            keyboard.press_and_release('alt + f4')
                            keyboard.press('down arrow')
                            keyboard.press('enter')
                            
                        else:
                            speak("ok i am not restarting this computer")

                    elif 'go to sleep mode' in query:
                        speak("do you really want me to go to sleep mode?")
                        comm = takeCommand()
                        if(comm == 'yes'):
                            speak("ok sir as you wish")
                            speak("bye sir! i am going to sleep mode")
                            
                            keyboard.press_and_release('alt + f4')
                            keyboard.press('up arrow')
                            keyboard.press('enter')
                            
                        else:
                            speak("ok i am not going to sleep")   
                    else:
                        hide_labels()                                            
            else:
                hide_labels()
                status15.destroy()
                security_img0.place_forget()
                security_img1=Label(window,image=img7,bg='white')
                security_img1.place(x=260, y=145)
                status13=Label(window, text="Access Denied !!", justify='left', background='white', font=("Helvetica", 22,'bold'), fg='red')
                status13.place(x=200, y=280)
                speak("Access denied")
                status13.destroy()
                security_img1.place_forget()
          

def Main_Window():
    def keyboard_off_on():
        global Keyboard
        Keyboard= Button(window, image=photo1, borderwidth=0, cursor="hand2", background='#F0FFFF', command=entry_box)
        Keyboard.place(x=635,y=447)
    def entry_box():
        global inputtxt
        global frame2
        frame2 = ttk.Frame(style="RoundedFrame", padding=10)
        inputtxt = tk.Text(frame2,height = 1.5,width = 55)
        inputtxt.pack()
        inputtxt.bind("<FocusIn>", lambda event: frame2.state(["focus"]))
        inputtxt.bind("<FocusOut>", lambda event: frame2.state(["!focus"]))
        frame2.place(x=55,y=435)
        Keyboard.destroy()
        Keyboard_dist= Button(window, image=off_keyboard, borderwidth=0, cursor="hand2", background='#F0FFFF', command=destroy13)
        Keyboard_dist.place(x=635,y=447)

 
    def destroy13():
        frame2.destroy()
        inputtxt.destroy()
        Keyboard= Button(window, image=photo1, borderwidth=0, cursor="hand2", background='#F0FFFF', command=entry_box)
        Keyboard.place(x=635,y=447)


    splash_window.destroy()
    global window
    global label25
    global button1
    global inputtxt
    global Keyboard
    global logo
    global img6
    global img7
    global img8
    global img9
    global img10
    window =tk.Tk()
    style = ttk.Style()
    window_width=680
    window_height=500
    window.minsize(680,500)
    window.maxsize(680,500)
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    window.configure(bg='#F0FFFF')
    
    borderImage = tk.PhotoImage("borderImage", data=borderImageData)
    focusBorderImage = tk.PhotoImage("focusBorderImage", data=focusBorderImageData)

    style.element_create("RoundedFrame",
                        "image", borderImage,
                        ("focus", focusBorderImage),
                        border=16, sticky="nsew")
    style.layout("RoundedFrame",
                [("RoundedFrame", {"sticky": "nsew"})])
    frame1 = ttk.Frame(style="RoundedFrame", padding=10)
    img = Image.open('voice1.png')
    img1=Image.open('keyboard.ico')
    img2=PhotoImage(file='3DotOption.png')
    img4=Image.open('Z logo2.png')
    img5=Image.open('keyboard_off.ico')
    img6=PhotoImage(file='security1.png')
    off_keyboard = ImageTk.PhotoImage(img5)
    img7=PhotoImage(file='security2.png')
    img8=PhotoImage(file='security3.png')
    img9=PhotoImage(file='bye02.png')

    window.iconbitmap("Z logo.ico")
    window.title("Zara- The Virtual Assistant")

    photo = ImageTk.PhotoImage(img)
    button1= Button(window, image=photo, borderwidth=0, cursor="hand2",command=start1 , background='white')
    button1.place(x=310,y=345)
    photo1 = ImageTk.PhotoImage(img1)
    # Keyboard= Button(window, image=photo1, borderwidth=0, cursor="hand2", background='#F0FFFF', command=entry_box)
    # Keyboard.place(x=635,y=447)
    photo0=ImageTk.PhotoImage(img4)
    logo=Label(window, image=photo0,bg='white')
    logo.place(x=300,y=80)
    
    mainmenu2 = Menubutton(window, image=img2, bg='#F0FFFF')
    mainmenu2.place(x=5)

    
    submenu2 = Menu(mainmenu2)
    mainmenu2.config(menu=submenu2)

    submenu2.add_command(label="Help", command=Help)
    submenu2.add_command(label="About Zara", command=About)
    submenu2.add_command(label="Exit", command=exit )
    label25=Label(window, text='Tap mic to say something!',font=("Times", 18,'bold'),bg='white')
    label25.place(x=180, y=200)
    keyboard_off_on()

    #round corner frame
    
    text1 = tk.LabelFrame(frame1, borderwidth=0, highlightthickness=0,
                    width=550, height=380,bg='white')
    text1.pack()

    text1.bind("<FocusIn>", lambda event: frame1.state(["focus"]))
    text1.bind("<FocusOut>", lambda event: frame1.state(["!focus"]))
    frame1.pack(padx=20, pady=20)
    frame1.focus_set()

  
    window.mainloop()



    



def Help():
    help_window=Tk()
    help_window.minsize(300,500)
    help_window.maxsize(300,500)
    help_window.title('Help')
    help="""Voice Commands
    To play--
    Youtube--
    Time--
    """
    label21=Label(help_window, text=help)
    label21.pack()
    help_window.iconbitmap("iconhelp.ico")
    help_window.mainloop()

def About():
    About_window=Tk()
    About_window.minsize(260,245)
    About_window.maxsize(260,245)
    About_window.iconbitmap("iconhelp1.ico")
    About_window.title('About')
    about="""Zara Virtual Assistant
    Version 1.0 (Built 2022)
    @ BCA Major Project 
             
    This Project Developed by
    Bca last year students at 
    'Gautam Buddha university'.
    This project is based to on AI and NPL.
    His name is 'Zara' , it is a Voice Assistant.


    This project Developed, under the 
    supervision of Mr. Bhupendra kumar.
    _________________________________
    2021-2022
            """
    label20=Label(About_window, text=about)
    label20.pack()
    About_window.mainloop()
def exit():
    window.destroy()


splash_window=Tk()
window_width=500
window_height=500
splash_window.overrideredirect(1)
screen_width = splash_window.winfo_screenwidth()
screen_height = splash_window.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
splash_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
            

lbl = ImageLabel(splash_window)
lbl.pack()
lbl.load('ZARA.gif')
splash_window.after(4000, Main_Window)
splash_window.mainloop()

