import tkinter as tk
from commands.command_center import process_command  # Make sure this exists!

def send_message(event=None):
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "You: " + user_input + "\n", "user")
    entry.delete(0, tk.END)

    response = process_command(user_input)

    chat_log.insert(tk.END, "JARVIS: " + response + "\n", "assistant")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

# Create main window
window = tk.Tk()
window.title("Jarvis AI")

# Chat log
chat_log = tk.Text(window, bg="black", fg="white", font=("Arial", 12))
chat_log.tag_config("user", foreground="cyan")
chat_log.tag_config("JARVIS", foreground="green")
chat_log.config(state=tk.DISABLED)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry box
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind("<Return>", send_message)

# Send button
send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=(0, 10))

# Run GUI loop
window.mainloop()
