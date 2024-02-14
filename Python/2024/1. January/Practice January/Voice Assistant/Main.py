# DATE ==> 12 January 2023
import speech_recognition
import random
import pyttsx3

def speak(text):
    print("TOMMY :", text)  
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    

    engine.setProperty('voice', voices[1].id)  # You may need to adjust the index based on available voices
    
    # Set a slower rate for a more robotic effect
    engine.setProperty('rate', 130)
    
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio).lower()
        print("YOU:", command)
        return command
    except speech_recognition.UnknownValueError:
        print("Sorry, could not understand your audio.")
        return None

def process_command(command):
    if "hello" in command:
        speak("Hello! ")

    elif "your name" in command:
        speak("My name is thommmy. You can call me thommmy.")

    elif "how are you" in command:
        speak("I'm doing well, thank you for asking!")

    elif "joke" in command or "tell me another joke" in command:
        jokes = random.choice(["Why don't scientists trust atoms? Because they make up everything!", "What do you call a fish with no eyes?  the answer is fsh!"])
        speak(jokes)

    elif "thank you" in command:
        speak("You're welcome! If you have more questions, feel free to ask.")

    elif "make a python file" in command or "create a python file" in command:
        speak("OK")
        with open("tommy.py", "w") as f:
            f.write("# HELLO WORLD BY TOMMY")

    elif any(keyword in command for keyword in ["bye", "exit", "stop"]):
        speak("Goodbye! Have a great day!")
        return True
        
    else:
        speak("Sorry, I didn't understand that command.")

    return False


if __name__ == "__main__":
    speak("Hello! I am thommmy. How can I help you today?")

    while True:
        command = listen()

        if command:
            if process_command(command):
                break
