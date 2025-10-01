import speech_recognition as sr



def fallback_to_typing_interactive():
    from utils.speaker import speak  # or import at the top if needed

    speak("I couldn't hear that. Would you like to type instead? (y/n)")
    choice = input(">> ").lower()
    
    if choice == "y":
        speak("Please type your command.")
        return input("⌨️ Type here: ").lower()
    
    speak("Alright. I'm listening again.")
    return None


def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        command = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {command}")
        return command.lower()

    except sr.UnknownValueError:
        print("❗ Didn't catch that.")
        return None

    except sr.RequestError:
        print("❌ Voice recognition service is down.")
        return None


def fallback_to_typing():
    command = input("⌨️ Type your command instead: ")
    return command.lower()


def get_command():
    voice_cmd = listen_command()
    if voice_cmd:
        return voice_cmd
    else:
        return fallback_to_typing()
