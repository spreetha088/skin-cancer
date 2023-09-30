import speech_recognition as sr
import subprocess
import webbrowser
import pyttsx3  
import datetime 

print('''i can assist you for:
      1.open youtube
      2. open google
      3.open chrome
      4. open email
      5. open notepad
      6. open excel
      7.open word
      8. open powerpoint
      9. current time
      10.current date day
      you should say your command by open'''
      )

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"Command recognized: {command}")
        speak(command)  # Speak the recognized command
        return command
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return None
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")
        return None

def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

def open_chrome():
    speak("Opening Chrome")
    subprocess.Popen([r"C:\Users\ELCOT\AppData\Local\Google\Chrome\Application\chrome.exe"])

def open_google():
    speak("Opening Google")
    webbrowser.open("https://www.google.com")

def open_word():
    speak("Opening Microsoft Word")
    webbrowser.open("C:/Users/ELCOT/Desktop/microsoft/word")
    
def open_powerpoint():
    speak("Opening Microsoft powerpoint")
    webbrowser.open("C:/Users/ELCOT/Desktop/microsoft/PowerPoint.lnk")
    
def open_excel():
    speak("Opening excel")
    webbrowser.open("C:/Users/ELCOT/Desktop/microsoft/Excel.lnk")
    
def open_notebook():
    speak("Opening Jupyter Notebook")
    subprocess.Popen(["jupyter", "notebook"])

def open_notepad():
    speak("Opening notepad")
    webbrowser.open("C:/Windows/notepad.exe")

def open_email():
        print("Opening email...")
        speak("opening email")
        webbrowser.open("mailto:")

def get_current_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    speak(f"The current time is {current_time}")
    
def current_date_day():
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%Y-%m-%d")
    current_day = current_datetime.strftime("%A")
    print(current_date, current_day)  # Print the values to the console
    speak(f"Today is {current_day}, {current_date}")

while True:
    command = listen_for_command()

    if command:
        if "open youtube" in command:
            open_youtube()
        elif "open chrome" in command:
            open_chrome()
        elif "open google" in command:
            open_google()
        elif "open word" in command:
            open_word()
        elif "notebook" in command:
            open_notebook()
        elif "excel" in command:
            open_excel()
        elif "notepad" in command:
            open_notepad()
        elif "powerpoint" in command:
            open_powerpoint()
        elif "email" in command:
            open_email()
        elif "current time" in command:
            get_current_time()
        elif "current date day" in command:
            current_date_day()
        elif "exit" in command:
            speak("Exiting the voice assistant. good bye.")
            break
    else:
        print("i can assist you only above commands")
       