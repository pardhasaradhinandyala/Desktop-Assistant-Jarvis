
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import subprocess
import urllib.parse

# Initialize Jarvis voice engine
engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


# Text-to-speech function
def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# Voice recognition function
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")

        recognizer.adjust_for_ambient_noise(
            source, duration=0.5
        )

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

            command = recognizer.recognize_google(audio)
            command = command.lower()

            print("You:", command)
            return command

        except sr.WaitTimeoutError:
            return ""

        except sr.UnknownValueError:
            speak("Sorry, I could not understand.")

        except sr.RequestError:
            speak("Speech recognition service is unavailable.")

        except OSError:
            speak("Microphone is not available.")

        return ""


# Main command execution function
def run_jarvis(command):

    if "hello" in command or "hi" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )
        speak("The current time is " + current_time)

    elif "date" in command:
        current_date = datetime.datetime.now().strftime(
            "%d %B %Y"
        )
        speak("Today's date is " + current_date)

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif command.startswith("search"):
        query = command.replace("search", "", 1).strip()

        if query:
            speak("Searching Google")
            url = (
                "https://www.google.com/search?q="
                + urllib.parse.quote(query)
            )
            webbrowser.open(url)
        else:
            speak("Please tell me what to search.")

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"])

    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen(["calc.exe"])

    elif "stop" in command or "exit" in command or "goodbye" in command:
        speak("Goodbye! Have a nice day.")
        return False

    else:
        speak("Sorry, this command is not available.")

    return True


# Main program
def main():

    speak("Hello! I am Jarvis, your desktop assistant.")
    speak("How can I help you?")

    running = True

    while running:
        command = listen()

        if command:
            running = run_jarvis(command)


# Start the assistant
if __name__ == "__main__":
    main()
