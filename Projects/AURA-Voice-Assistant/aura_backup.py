
"""
AURA - Advanced Personal Voice Assistant

Features:
- Recognize voice commands
- Speak responses using Windows Speech
- Tell date and time
- Open websites
- Search Google
- Handle errors
"""

import datetime
import webbrowser
import urllib.parse
import subprocess
import base64

import speech_recognition as sr


class AuraAssistant:

    def __init__(self):

        # Initialize speech recognition
        self.recognizer = sr.Recognizer()

        self.is_running = True

        # Supported websites
        self.websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "linkedin": "https://www.linkedin.com",
            "gmail": "https://mail.google.com"
        }

        print("=" * 50)
        print("       AURA - PERSONAL VOICE ASSISTANT")
        print("=" * 50)

    # 1. SPEAK FUNCTION

    def speak(self, text):

        print(f"AURA: {text}")

        try:
            encoded_text = base64.b64encode(
                text.encode("utf-8")
            ).decode("ascii")

            script = f"""
Add-Type -AssemblyName System.Speech

$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer

$speaker.Rate = 0
$speaker.Volume = 100

$message = [System.Text.Encoding]::UTF8.GetString(
    [System.Convert]::FromBase64String('{encoded_text}')
)

$speaker.Speak($message)

$speaker.Dispose()
"""

            subprocess.run(
                [
                    "powershell.exe",
                    "-NoProfile",
                    "-Command",
                    script
                ],
                check=True,
                capture_output=True,
                text=True,
                timeout=30
            )

        except Exception as error:
            print("Speech Error:", error)

    # 2. LISTEN FUNCTION

    def listen(self):

        try:

            with sr.Microphone() as source:

                print("\nListening...")

                self.recognizer.adjust_for_ambient_noise(
                    source, duration=0.5
                )

                audio = self.recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=8
                )

            print("Recognizing...")

            command = self.recognizer.recognize_google(audio)

            command = command.lower().strip()

            print(f"You: {command}")

            return command

        except sr.WaitTimeoutError:

            print("No speech detected.")
            return ""

        except sr.UnknownValueError:

            self.speak("Sorry, I could not understand you.")
            return ""

        except sr.RequestError:

            self.speak(
                "Speech recognition service is unavailable. "
                "Please check your internet connection."
            )

            return ""

        except OSError:

            self.speak(
                "Microphone is unavailable. "
                "Please check your microphone connection."
            )

            return ""

    # 3. TIME FUNCTION

    def tell_time(self):

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        self.speak(f"The current time is {current_time}")

    # 4. DATE FUNCTION

    def tell_date(self):

        current_date = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        self.speak(f"Today's date is {current_date}")

    # 5. WEBSITE FUNCTION

    def open_website(self, website):

        if website in self.websites:

            webbrowser.open(self.websites[website])

            self.speak(f"Opening {website}")

        else:

            self.speak(
                f"Sorry, {website} is not in my supported websites."
            )

    # 6. GOOGLE SEARCH FUNCTION

    def search_google(self, query):

        if not query:
            self.speak("Please tell me what you want to search.")
            return

        search_url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote_plus(query)
        )

        webbrowser.open(search_url)

        self.speak(f"Searching Google for {query}")

    # 7. HELP FUNCTION

    def show_help(self):

        self.speak(
            "Here are my available commands. "
            "You can ask for time, date, "
            "open Google, YouTube, GitHub, LinkedIn or Gmail, "
            "search for something on Google, "
            "or say goodbye to exit."
        )

    # 8. COMMAND PROCESSING FUNCTION

    def process_command(self, command):

        if not command:
            return

        if "hello" in command or "hey aura" in command:

            self.speak("Hello! How can I help you today?")

        elif "time" in command:

            self.tell_time()

        elif "date" in command:

            self.tell_date()

        elif command.startswith("open "):

            website = command.replace(
                "open ", "", 1
            ).strip()

            self.open_website(website)

        elif command.startswith("search for "):

            query = command.replace(
                "search for ", "", 1
            ).strip()

            self.search_google(query)

        elif "help" in command:

            self.show_help()

        elif any(word in command.split() for word in [
            "exit", "quit", "goodbye", "stop"
        ]):

            self.speak("Goodbye! Have a productive day.")

            self.is_running = False

        else:

            self.speak(
                "Sorry, I don't understand that command yet. "
                "Say help to hear my available commands."
            )

    # 9. MAIN RUN FUNCTION

    def run(self):

        self.speak(
            "Hello! I am AURA, your personal voice assistant."
        )

        self.speak("How can I help you?")

        while self.is_running:

            command = self.listen()
 
            self.process_command(command)

        print("\nAURA has been closed.")


# APPLICATION ENTRY POINT

if __name__ == "__main__":

    try:

        assistant = AuraAssistant()

        assistant.run()

    except KeyboardInterrupt:

        print("\nAURA stopped by user.")

    except Exception as error:

        print(f"An unexpected error occurred: {error}")
