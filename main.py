import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes


# initialize vooice engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=recognizer.listen(source)
        try:
            command=recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            speak("Sorry, there was a problem with the service.")
            return ""

def greet():
    hour=datetime.datetime.now().hour
    if 0<= hour < 12:
     speak("Good Morning")
    elif 12<= hour < 18: 
        speak("Good Afternoon")
    else:
        speak("Good evening") 

    speak("How can I assist you today?")

def main():
    greet()
    while True:
        command = listen()

        if "wikipedia" in command:
            speak("Searching Wikipedia...")
            topic = command.replace("wikipedia", "")
            result = wikipedia.summary(topic, sentences=2)
            speak(result)

        elif "time" in command:
            time_now = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {time_now}")

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        
        elif "joke" in command:
            joke = pyjokes.get_joke()
            speak(joke)

        elif "youtube" in command:
            speak("What should I search on YouTube?")
            search_query = listen()
            url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
            webbrowser.open(url)
            speak(f"Here are the results for {search_query} on YouTube.")
    

        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break

        else:
            speak("Sorry, I don't know how to help with that.")

if __name__ == "__main__":
    main()       