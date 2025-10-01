import os
import json
import webbrowser
import subprocess
import datetime
import input_handler

from utils import listen
from utils import volume_control


import threading


import cv2
import datetime

def take_picture():
    cap = cv2.VideoCapture(0)  # 0 is the default camera
    if not cap.isOpened():
        speak("Sorry, I couldn't access the camera.")
        return

    ret, frame = cap.read()
    if ret:
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"photo/photo_{time_stamp}.jpg"
        cv2.imwrite(filename, frame)
        speak(f"Picture taken and saved")
    else:
        speak("Sorry, I couldn't take the picture.")

    cap.release()
    cv2.destroyAllWindows()




camera_running = False  # Global flag

def open_camera():
    global camera_running
    camera_running = True
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        speak("Unable to access the camera")
        return

    while camera_running:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Manual quit fallback
            break

    cap.release()
    cv2.destroyAllWindows()


def take_note():
    speak("What would you like me to write down?")
    note = input_handler.listen_command()   # your existing voice input function
    if note:
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"notes/note_{time_stamp}.txt"
        with open(filename, "w") as file:
            file.write(note)
        speak("Noted, sir. I've saved it.")
    else:
        speak("I didn't catch that. Try again.")

# === Load app open/close skills ===

def load_app_skills():
    try:
        app_skills_path = os.path.join(os.path.dirname(__file__), "app_skills.json")
        with open(app_skills_path, "r") as f:

            return json.load(f)
    except Exception as e:
        print(f"❌ Failed to load app skills: {e}")
        return {}

# === Open App ===

def open_app(app_name):
    app_name = app_name.lower().strip()
    app_skills = load_app_skills()

    if app_name in app_skills:
        command = app_skills[app_name]
        try:
            os.system(command)
            print(f"✅ Opening {app_name.title()}")
        except Exception as e:
            print(f"❌ Failed to open {app_name}: {e}")
    else:
        print(f"❌ Sorry, I don’t know how to open {app_name}")

# === Close App ===

def close_app(app_name):
    exe_map = {
        "notepad": "notepad.exe",
        "chrome": "chrome.exe",
        "vs code": "Code.exe",
        "vscode": "Code.exe",
        "spotify": "Spotify.exe",
        "calculator": "Calculator.exe",
        "netflix": "Netflix.exe",
        # Add more exe names as needed
    }

    app_name = app_name.lower().strip()
    if app_name in exe_map:
        exe_name = exe_map[app_name]
        try:
            subprocess.call(["taskkill", "/f", "/im", exe_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"✅ Closed {app_name.title()}")
        except Exception as e:
            print(f"❌ Failed to close {app_name}: {e}")
    else:
        print(f"❌ Sorry, I don’t know how to close {app_name}")

# === Open Website if app not found ===

def open_website(command):
    website_urls = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "github": "https://www.github.com",
        "playlist": "https://www.youtube.com/watch?v=-E270r7o730&list=PLyiuJFeckymt_Wj_CIcaZp9w4g5xb0ySq"

        # Add more if needed
    }

    for name in website_urls:
        if name in command.lower():
            print(f"🌐 Opening {name}")
            webbrowser.open(website_urls[name])
            return True

    return False

# === Main command handler ===

def process_command(command):
    command = command.lower().strip()

    if "open" in command:
        app = command.replace("open", "").strip()
        open_app(app)

    elif "close" in command:
        app = command.replace("close", "").strip()
        close_app(app)

   



    elif open_website(command):
        pass

    else:
        print("🤖 I didn’t understand that command.")



# ===================================old_one=====================================



import subprocess
import webbrowser
from utils.speaker import speak
import os
import psutil

from memory import remember, recall_history


# def process_command(command):
#     command = command.lower()
def process_command(command: str) -> str:
    


    # === LOCAL APP COMMANDS ===

    if "hello jarvis" in command:
        speak("Hello sir! i am jarvis, how can i assist you?")
        subprocess.Popen

    elif "take picture" in command:
        take_picture()


        

    

    elif "take a note" in command or "write this down" in command:
        take_note()   

    elif "open notepad" in command:
        speak("Opening Notepad")
        subprocess.Popen("notepad.exe")

   
    elif "open camera" in command:
        speak("Launching camera")
        threading.Thread(target=open_camera).start()

    elif "close camera" in command:
        global camera_running
        speak("Closing camera")
        camera_running = False

    
    

    
    

  

    
    elif "open calculator" in command:
        speak("Opening Calculator")
        subprocess.Popen("calc.exe")

    

    elif "open chrome" in command:
        speak("Opening Google Chrome")
        subprocess.Popen("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
       
    elif "open code" in command or "open vs code" in command:
        speak("Opening Visual Studio Code")
        subprocess.Popen(r"C:\Users\mdowa_t185pyb\AppData\Local\Programs\Microsoft VS Code\Code.exe")

    elif "open file explorer" in command:
        speak("Opening File Explorer")
        subprocess.Popen("explorer")

    # === ONLINE COMMANDS ===


    
    # Add logic for opening desktop apps here if needed






    elif "search for" in command:
        query = command.replace("search for", "").strip()
        speak(f"Searching Google for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "play on youtube" in command:
        query = command.replace("play on youtube", "").strip()
        speak(f"Playing {query} on YouTube")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif "open my playlist" in command:
        speak("Opening your playlist")
        webbrowser.open("https://www.youtube.com/watch?v=VmZ8pKZUVfY&list=PLyiuJFeckymt_Wj_CIcaZp9w4g5xb0ySq&index=1")

    elif "open chat GPT" in command:
        speak("Opening chat GPT")
        webbrowser.open("https://chatgpt.com/")



    # elif "open chatgpt" in command or "open chat gpt" in command:
    #     speak("Opening ChatGPT")
    #     webbrowser.open("https://chatgpt.com/")
    #     return

  


   

    elif "increase volume" in command:
        volume_control.increase_volume()
        speak("Volume increased.")

    elif "decrease volume" in command:
        volume_control.decrease_volume()
        speak("Volume decreased.")

    elif "now unmute" in command:
        volume_control.unmute_volume()
        speak("Volume unmuted.")

    elif "turn off sound" in command:
        volume_control.mute_volume()
        speak( "done.")

    
       

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("https://github.com")

    elif "open college" in command:
        speak("Opening VTOP")
        webbrowser.open("https://vtop.vitbhopal.ac.in/vtop/open/page")

    # === SYSTEM COMMANDS ===
    elif "exit" in command or "shutdown" in command:
        speak("Shutting down. Goodbye sir.")
        exit()

    # === HISTORY ===
    elif "show history" in command or "what did i say" in command:
        past_commands = recall_history()
        speak("Here are your last commands:")
        for cmd in past_commands:
            print(f"🕘 {cmd}")
            speak(cmd)


    elif "open" in command:
        if open_website(command):
            return
    # === CLOSING ===
    





    elif "close" in command:
        app = command.replace("close", "").strip().lower()
        if app:
            close_app(app)
        else:
            speak("Please say the app name to close.")




    # === DEFAULT RESPONSE ===
    else:
        speak("Sorry sir, I didn't understand that command.")






app_name_map = {
    # Apps
    "chrome": "chrome",
    "vs code": "Code",
    "notepad": "notepad",
    "spotify": "Spotify",
    "edge": "msedge",
    "netflix":"Netflix",


    # Websites (special handling)
    "youtube" : "website",
    "chat gpt": "website",
    "google": "website",
    "college" : "website",
    "amazon": "website",
    "instagram": "website",
    "whatsapp": "website",
    "facebook": "website"
}





def close_app(app_name):
    app_key = app_name.lower()
    exe_name = app_name_map.get(app_key)

    if exe_name == "website":
        # Try to find Chrome or Edge processes with 'youtube' in the title
        closed = False
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                if proc.info['name'] and proc.info['name'].lower() in ["chrome.exe", "msedge.exe"]:
                    proc_cmd = " ".join(proc.cmdline()).lower()
                    if "youtube" in proc_cmd:
                        psutil.Process(proc.info['pid']).terminate()
                        closed = True
            except Exception:
                pass
        if closed:
            speak(f"Closed {app_name}")
        else:
            speak(f"I couldn't find any open {app_name} tabs.")
    elif exe_name:
        os.system(f"taskkill /f /im {exe_name}.exe")
        speak(f"Closing {app_name}")
    else:
        speak("I don't know how to close that app yet.")


import webbrowser

def open_website(command):
    # Dictionary for websites
    website_urls = {
        "youtube": "https://www.youtube.com",
        "chat gpt": "https://chat.openai.com",
        "google": "https://www.google.com",
        "amazon": "https://www.amazon.in",
        "instagram": "https://www.instagram.com",
        "facebook": "https://www.facebook.com",
        "whatsapp": "https://web.whatsapp.com",
        "song playlist": "https://www.youtube.com/watch?v=-E270r7o730&list=PLyiuJFeckymt_Wj_CIcaZp9w4g5xb0ySq",
        "college ": "https://vtop.vitbhopal.ac.in/vtop/open/page"
    }

    for name in website_urls:
        if name in command:
            speak(f"Opening {name}")
            webbrowser.open(website_urls[name])
            return True

    return False
    








# # def process_command(command):
# #     remember(command)

# #     command = command.lower()

# #     if "open notepad" in command:
# #         speak("Opening Notepad.")
# #         os.system("start notepad")

# #     elif "show history" in command or "what did i say" in command:
# #         past_commands = recall_history()
# #         speak("Here are your last commands:")
# #         for cmd in past_commands:
# #             print(f"🕘 {cmd}")
# #             speak(cmd)

# #     else:
# #         speak("Sorry, I don't understand that yet.")




# # def process_command(command: str) -> str:
# #     command = command.lower()
    
# #     if "hello" in command:
# #         return "Hello Sir, how can I assist you?"
# #     elif "your name" in command:
# #         return "I am Jarvis, your assistant."
# #     elif "exit" in command or "quit" in command:
# #         return "Goodbye Sir."
# #     else:
# #         return "Sorry Sir, I didn’t understand that."
