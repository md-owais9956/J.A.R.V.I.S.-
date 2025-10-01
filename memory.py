import json
import os

MEMORY_FILE = "jarvis_memory.json"

# Ensure the memory file exists
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump([], f)

def remember(command):
    with open(MEMORY_FILE, "r") as f:
        history = json.load(f)
    
    history.append(command)

    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f)

def recall_history(limit=5):
    with open(MEMORY_FILE, "r") as f:
        history = json.load(f)

    return history[-limit:]  # return the latest few commands
