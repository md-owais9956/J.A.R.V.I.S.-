from wake_word_detector import start_wake_word_listener
from utils.speaker import speak
from utils.listen import listen
from commands.command_center import process_command
from input_handler import fallback_to_typing_interactive
import datetime

def greet_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, sir.")
    elif 12 <= hour < 18:
        speak("Good afternoon, sir.")
    else:
        speak("Good evening, sir.")
    speak("All systems online. Ready for your command.")

# Call this once when the assistant starts
greet_user()



def jarvis_command_handler():
    speak("Yes sir")
    command = listen()

    if command is None or command.strip() == "":
        command = fallback_to_typing_interactive()
        if not command:
            return  # Go back to listening

    process_command(command)


if __name__ == "__main__":
    speak("please complete the authentication.")
    start_wake_word_listener(jarvis_command_handler)
