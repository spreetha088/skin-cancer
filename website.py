import speech_recognition as sr
import pyttsx3
import subprocess
import mysql.connector

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

def website_name():
    speak("The website name is Sports Management System.")

def purpose():
    speak('''The purpose of the sports management system is,
          you can register for a particular sport using this website without going to the particular venue.''')

def module():
    speak('''In the sports management system, there are three modules.
          1. Index
          2. Login
          3. Register ''')

def explanation():
    speak('''The website name is Sports Management System.
          You should log in to the website using the login module.
          This module contains email id and password.
          After login, you can register for the sports you are interested in by providing your details: name, age, department, sports name, and email id. Registration is successfully completed after that.''')

def open_website():
    print("Opening the website...")
    speak("Opening the website in Google Chrome")
    url = "http://localhost/sports/index.html"

    try:
        subprocess.Popen(["start", "chrome", url], shell=True)
    except Exception as e:
        print(f"Error: {e}")
        
def open_xxamp():
    print("Opening XAMPP...")
    speak("Opening XAMPP")
    
    # Specify the path to the XAMPP control panel executable
    xampp_path = r"C:\xampp\xampp-control.exe"
    
    try:
        subprocess.Popen([xampp_path])
    except Exception as e:
        print(f"Error: {e}")



def open_database():
    print("Opening the 'sports' database...")
    speak("Opening the 'sports' database")

    # Database connection parameters
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "",  # Replace with your MySQL password
        "database": "sport"
    }

    try:
        # Establish a connection to the 'sports' database
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            print("Connected to the 'sports' database")
            speak("Connected to the 'sports' database")

            # Perform a sample query
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM register")  # Replace 'your_table' with the actual table name

            # Fetch and print the results
            for row in cursor.fetchall():
                print(row)

            # Close the cursor and the database connection
            cursor.close()
            connection.close()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        speak("An error occurred while connecting to the 'sports' database")

while True:
    command = listen_for_command()

    if command is not None:
        if "website name" in command:
            website_name()
        elif "purpose of website" in command:
            purpose()
        elif "modules in website" in command:
            module()
        elif 'explain the website' in command:
            explanation()
        elif "open website" in command:
            open_website()
        elif "open server" in command:
            open_xxamp()
        elif "open database" in command:
            open_database()
        elif "exit" in command:
            speak("Goodbye!")
            break
