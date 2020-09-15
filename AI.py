import os
import webbrowser
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import random
import smtplib
# for python text to speech

# sapi5 is inbuilt from windows to take a voice
engine = pyttsx3.init('sapi5')
# engine.say("this is a speaking time")
# engine.runAndWait()
voices = engine.getProperty('voices')
# print(voices)
# print(voices[1].id)
# setting voice property of engine
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # to wish me as per time
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour <18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis.. Please tell me how may I help you")

def takeCommand():
    # to take microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening... ")
        r.pause_threshold = 1
        # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said : {query} \n")

    except Exception as e:
        # print(e)
        print("say that again please !! ... ")
        return "None"
    return query

def sendEmail(to, content):
    # requires email access to less secure apps to send email 
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email-id-here','email-password')
    server.sendmail('email-id-here',to,content)
    server.close()

# sendEmail
if __name__ == '__main__':
    # speak("Pankaj is testing main function")
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower()
        # logic for eecuting query
        if 'wikipedia' in query:
            speak('Searching wikipedia .. ')
            # replace wikipedia with blank and search remaining into wikipedia
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2) #read two sentences
            speak("According to wikipedia")
            # print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            # locating path where music is located in computer
            music_dir = 'C:\\Users\\Pankaj\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            # selecting random songs to play using os module
            os.startfile(os.path.join(music_dir, songs[random.randint(0,30)]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is : {strTime}")
        elif 'open office' in query:
            officePath = "C:\\Users\\Pankaj\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Chrome Apps\\Office"
            os.startfile(officePath)

        elif 'email to pankaj' in query:
            # send email and detect email using dictionary
            # import contacts from google contact and send them email -- to try
            try:
                speak("what should I say")
                content = takeCommand()
                to = "asusmobile219@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry pankaj bro, ,I am not able to send the email")
