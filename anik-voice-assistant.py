import speech_recognition as sr  #It will listen to your voice
#creating a recoginzer where my voice will be recognized
import pyttsx3 #by this library assistant will speak
import pywhatkit #for searching like playing video on youtube
import datetime 
import wikipedia
import pyjokes
# from googlesearch import search


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #for setting up the female voice
engine.say("Hello Aniket")
engine.runAndWait()

#this fn is created so that assistant can repeat you words
def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        #using microphone to listen to the voice and storing it in voice
        with sr.Microphone() as source:
            print("listening...") #giving indication that assistant is listening
            #voice from listner will be stored in voice variable
            voice = listener.listen(source)
            #recognize_google is a google api to convert voice to text
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print(command)
        
    except:
        pass
    return command

def run_assistant():
    command = take_command()
    if 'play' in command:
           song = command.replace('song', '')
           talk('playing' + song)
           print('playing...')
           print(song)
           pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('so, the current time is' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info) 

    elif 'date' in command:
        talk('sorry, I have a headache')

    elif 'are you single' in command:
        talk('I am in a relationship with wifi')

    elif 'joke' in command:
        a = pyjokes.get_joke()
        talk(pyjokes.get_joke())
        print(a)
    # elif 'google' in command:
    #     browser = command.replace('google', '')
    #     search(browser)       

    else:
        talk('Please say the command again.')
        print('please say the command again.')
while True:  
    run_assistant() 
     

 