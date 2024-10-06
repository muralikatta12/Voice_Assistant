
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')#microsoft api key
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)#voices[0] is male voice

def speak(audio): 
    engine.say(audio)
    engine.runAndWait()
def wishme(): 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good morning")
    elif hour>=12 and hour<=18: 
        speak("good afternoonn")
    else: 
        speak("good evening")
    speak("HELLO THERE ,THIS IS YOUR VOICE ASSISTANT LOKI HOW CAN I HELP YOU ?")
    #speech recognizer
def takecommand(): 
    r=sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listening..............")
        r.pause_threshold=1
        audio = r.listen(source)
    try: 
        print("Recording.............")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
    except Exception as e: 
       
        print(" sorry say that again please")
        return "None"
    return query
def sendemail(to,content): 
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('muralikatta15@gmail.com','password')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()
if __name__ == "__main__": 
    wishme()
    while True:
      query=takecommand().lower()

      if 'wikipedia' in query: 
           speak('searching wikipedia.....')
           query=query.replace("wikipedia", "")
           results=wikipedia.summary(query,sentences=2)
           speak("According to wikipedia")
           speak(results)
      elif ' youtube' in query: 
          speak("opening youtube")
          webbrowser.open("youtube.com")
      elif 'google' in query: 
          speak("opening")
          webbrowser.open('google.com')
      elif 'open stackoverflow' in query: 
          webbrowser.open("stackoverflow.com")
      elif 'play the music' in query: 
          music_dir= "C:\\Users\\mural\\Music\\[iSongs.info] 03 - Kushi Title Song.mp3"
          
          print("songs")
          os.startfile(music_dir)
      elif 'time' in query: 
          strTime=datetime.datetime.now().strftime("%H:%M:%S")
          speak(f"sir,the time is {strTime}")
      
      elif 'introduce' in query: 
          videopath= "C:\\Users\\mural\\Videos\\MURALI KATTA-TITLE REVEL..mp4"
          os.startfile(videopath)
          speak("here is your introduction")
          print("PLAYING VIDEO.......")
      elif 'mail to murali' in query: 
          try: 
              speak("what should i say?")
              content =takecommand()
              to ="muralisaveetha7@gmail.com"
              sendemail(to,content)
              speak("Email has been sent")
          except Exception as e: 
              print(e)
              speak("sorry my friend murali i can't able to send mail")
