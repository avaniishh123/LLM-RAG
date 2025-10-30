import os
import webbrowser
import psutil
import subprocess
import speech_recognition as sr

# ========== OPEN FUNCTIONS ==========

def open_chrome():
    webbrowser.open("https://www.google.com")
    return "Chrome opened with Google."

def open_calculator():
    subprocess.Popen("calc")
    return "Calculator opened."

def open_notepad():
    subprocess.Popen("notepad")
    return "Notepad opened."

def open_paint():
    subprocess.Popen("mspaint")
    return "Paint opened."

def open_word():
    try:
        subprocess.Popen(r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        return "Word opened."
    except FileNotFoundError:
        return "Microsoft Word not found. Check the path."

# ========== SYSTEM INFO ==========

def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent(interval=1)}%"

def get_memory_usage():
    mem = psutil.virtual_memory()
    return f"Memory Usage: {mem.percent}% ({mem.used // (1024**2)}MB used of {mem.total // (1024**2)}MB)"

# ========== SHELL COMMAND ==========

def run_shell_command_from_prompt(prompt):
    try:
        if not prompt:
            return "No command provided."
        output = subprocess.check_output(prompt, shell=True, text=True)
        return output.strip()
    except subprocess.CalledProcessError as e:
        return f"Command failed: {e.output.strip()}"
    except Exception as e:
        return str(e)

# ========== GREETING ==========

def greet():
    return "Hello from custom function!"

# ========== VOICE COMMAND HANDLER ==========

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except sr.UnknownValueError:
        return "Sorry, I didn't understand that."
    except sr.RequestError:
        return "Speech recognition service is unavailable."

# ========== DATE & TIME FUNCTIONS ==========

def say_date():
    from datetime import datetime
    return "Today is " + str(datetime.now().date())

def say_time():
    from datetime import datetime
    return "Current time is " + datetime.now().strftime("%H:%M:%S")

def say_year():
    from datetime import datetime
    return "Current year is " + str(datetime.now().year)

# ========== FUN FUNCTIONS ==========

def random_joke():
    import random
    jokes = [
        "Why did the developer go broke? Because he used up all his cache.",
        "Debugging: Being the detective in a crime movie where you are also the murderer."
    ]
    return random.choice(jokes)

def say_os():
    return "This OS is " + os.name


def say_os():
    import os
    return 'This OS is ' + os.name


def say_hello():
    return 'Hello from your automation assistant!'
