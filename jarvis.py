import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices =  engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)    
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("good evening")

    speak("hello sir, I am phoebe. How may i help you?")            



# def takeCommand():
#     #it takes microphones input from the user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening......")
#         r.pause_threshold = 1
#         audio = r.listen(source)


#     try:
#         print("Recognizing.....")
#         query  = r.recognize_google(audio,language='en-in')    
#         print(f"user said: {query}\n")

#     except Exception as e:
#         # print(e)
#         print("say that again please....")
#         return "None"
#     return query




def takeCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return "None"
    
    return query

# Call the function
takeCommand()



if __name__ =="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

    #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching  Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com") 

        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'play music' in query:
            webbrowser.open("https://open.spotify.com/")

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strTime}")

        