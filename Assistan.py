import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import googlesearch

listener = sr.Recognizer()
engine = pyttsx3.init() 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('Iam youre assistant what can i do for you')
            print('Mendengarkan..........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Assistan' in command:
                command = command.replace('Assistan', '')
                print(command)
    except:
        pass
    return command


def run_Assistan():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('No. I am in a relationship with wifi. you better find someone else')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'what is' in command:
        things = command.replace('who is', '')
        info = googlesearch.search(things)
        print(info)
        for term in search_terms:
             
    else:
        talk('Please say the command again.')


while True:
    run_Assistan()
