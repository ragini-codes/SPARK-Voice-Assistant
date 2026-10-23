import speech_recognition as sr
import pyttsx3
import pywhatkit

import wikipedia
from playsound import playsound
import os

f=0
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate',135)
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    

def take_command():
    try:
        with sr.Microphone() as source:
            talk("")
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            
            if 'spark' in command:
                
                #command1 = command.replace('JVM Welcomes You)
                #print(command1)
                talk('Waiting for the command....')
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if "yourself" in command:
                    talk("Hello!  I'm Spark,  an AI voice assistant created by students of class 11, Jindal Vidya Mandir, focused on developing artificial intelligence. They've worked hard to ensure I can understand and generate language, so I can have meaningful conversations and provide useful information. My goal is to help make your experience easier and more enjoyable!")
               # elif '' in command:
                    #talk('playing')
                    #pywhatkit.sendwhatmsg("", "Hi", 13, 30)
                    #print("sent")
             
                elif 'brief' in command:
                    person = command.replace('breifing', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    talk(info)
                elif 'thanks' in command:
                    talk('Thank you to our Chief Guest, for joining us today and inspiring us with their words. We appreciate the hard work of our teachers, staff, and students in making this exhibition possible. Thanks also to our parents and guests for their continued support. We hope this event encourages a love for learning.   Thank you!')
                elif 'video' in command:
                    talk('Yaa sure. Here is the awaited documentary ')
                    pywhatkit.playonyt('https://youtu.be/y8auGbDYZVo')
                elif "interact" in command:
                    talk("Yaa sure!!!! I would be delighted to do so.")
                elif "greet" in command:
                    talk("Hello everyone! I'm spark, your voice assistant. I'm excited to meet you all! ")
                elif "wrap" in command:
                    talk("I’m not ready to leave just yet! Let’s see what more we have in store!")
            
                elif "guess" in command:
                    talk("Of course, we are talking a out none other than Venerated Sangeetha Jindal Madam and Respected Murgan Sir.   Their words are both informative and motivational, inspiring urgency and excitement about innovation.    They emphasize the need to equip students , with the right tools to access knowledge,  and thrive in an evolving technological world.  They is not only a source of inspiration for many,  but also a driving force for progress,  reminding us that innovation and education are the keys to shaping the future. They are, without a doubt, our inspiration.")
                elif "invitation" in command:
                    talk("Ya sure , I will do that for you.  I will send to Ishwari ma'am and Shreenivasan sir number as they are our authorised public customer.")
                   # pywhatkit.sendwhatmsg("+918884665949", "Goof morining mam , spark here")#Ishwari mam
                    pywhatkit.sendwhatmsg("+918088452915", "Hi")
                elif "special" in command:
                    talk("Yes, there is!!!!!! A special dance performance is being presented by the talented students of JVM. It's something you wouldn't want to miss—full of energy and creativity!")
                elif "audience" in command:
                    talk("You all are the ones who make these moments meaningful. The energy in this room is incredible. Thank you for bringing such an incredible vibe to the room today.")
                elif 'stop' in command:
                    return 1
                
                    
                else:
                    talk('Please say the command again.')
                
    except: 
        pass
while True:

 T=take_command()  
 
 if T==1:
     break
talk("Thanks, Will Meet You Soon. Take Care All")
