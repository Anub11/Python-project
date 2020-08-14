import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")

    speak("I am Siri Sir! How may i help you ! ")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said : {query}\n")
    except Exception as e :
        print("Pleas Said Again sir !! ")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == '__main__':
    wishMe()

    while 1 :
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak("Accoding to wikipedia...")
            print(result)
            speak(result)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "naruto" in query:
            naruto_dir='D:\\Anime\\Naruto'
            videos=os.listdir(naruto_dir)
            os.startfile(os.path.join(naruto_dir,videos[0]))

        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir now time is ")
            print(strTime)
            speak(strTime)

        elif "open code" in query:
            path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.1.2\\bin\\pycharm64.exe"
            os.startfile(path)

        elif 'email to tert' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "harryyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif "stop" in query:
            speak("thank you for using me ! have a good day sir !")
            break;

        else:
            speak("sorry sir ! i cant understand!! Speak Again !")

        