
"""
AURA - Command Handler

Purpose:
Understand and process user commands.
"""

import datetime
import webbrowser
import urllib.parse

from features.app_launcher import AppLauncher


class CommandHandler:

    def __init__(self, speak_function, websites):

        self.speak = speak_function

        self.websites = websites

        # Initialize application launcher
        self.app_launcher = AppLauncher()

    # 1. Tell current time
    def tell_time(self):

        current_time = datetime.datetime.now().strftime(
            "%I:%M %p"
        )

        self.speak(f"The current time is {current_time}")

    # 2. Tell today's date
    def tell_date(self):

        current_date = datetime.datetime.now().strftime(
            "%d %B %Y"
        )

        self.speak(f"Today's date is {current_date}")

    # 3. Open supported websites
    def open_website(self, website):

        if website in self.websites:

            webbrowser.open(self.websites[website])

            self.speak(f"Opening {website}")

    # 4. Search Google
    def search_google(self, query):

        if not query:

            self.speak("Please tell me what to search.")

            return

        search_url = (
            "https://www.google.com/search?q="
            + urllib.parse.quote_plus(query)
        )

        webbrowser.open(search_url)

        self.speak(f"Searching Google for {query}")

    # 5. Open desktop applications
    def open_application(self, app_name):

        success = self.app_launcher.open_application(
            app_name
        )

        if success:

            self.speak(f"Opening {app_name}")

        else:

            self.speak(
                f"Sorry, I cannot open {app_name} yet."
            )

    # 6. Help function
    def show_help(self):

        self.speak(
            "You can ask me for time, date, "
            "open Google, YouTube, GitHub, LinkedIn or Gmail, "
            "open Notepad, Calculator or File Explorer, "
            "search Google, or say goodbye to exit."
        )

    # 7. Process commands
    def process_command(self, command):

        if not command:

            return True

        if "hello" in command or "hey aura" in command:

            self.speak(
                "Hello! How can I help you?"
            )

        elif "time" in command:

            self.tell_time()

        elif "date" in command:

            self.tell_date()

        elif command.startswith("open "):

            target = command.replace(
                "open ", "", 1
            ).strip()

            # Check websites first
            if target in self.websites:

                self.open_website(target)

            # Otherwise open desktop applications
            else:

                self.open_application(target)

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

            self.speak(
                "Goodbye! Have a productive day."
            )

            return False

        else:

            self.speak(
                "Sorry, I don't understand that command yet. "
                "Say help to hear my available commands."
            )

        return True
