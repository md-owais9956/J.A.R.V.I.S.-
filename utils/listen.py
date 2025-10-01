import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand your speech.")
        return ""
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service.")
        return ""
