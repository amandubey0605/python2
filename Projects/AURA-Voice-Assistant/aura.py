#pygame(library to play mp3in text)
"""
AURA - Advanced Personal Voice Assistant

Features:
- Voice input
- Voice output
- Command processing
- Date and time
- Website automation
- Desktop application automation
"""

from core.voice_output import speak as speak_text
from core.voice_input import VoiceInput
from features.command_handler import CommandHandler


class AuraAssistant:

    def __init__(self):

        # Initialize voice input
        self.voice_input = VoiceInput()

        # Assistant running status
        self.is_running = True

        # Supported websites
        self.websites = {
            "google": "https://www.google.com",
            "youtube": "https://www.youtube.com",
            "github": "https://github.com",
            "linkedin": "https://www.linkedin.com",
            "gmail": "https://mail.google.com"
        }

        # Initialize command handler
        self.command_handler = CommandHandler(
            self.speak,
            self.websites
        )

        print("=" * 50)
        print("       AURA - PERSONAL VOICE ASSISTANT")
        print("=" * 50)

    # 1. Speak function
    def speak(self, text):

        speak_text(text)

    # 2. Listen function
    def listen(self):

        return self.voice_input.listen()

    # 3. Process command
    def process_command(self, command):

        self.is_running = (
            self.command_handler.process_command(command)
        )

    # 4. Main run function
    def run(self):

        self.speak(
            "Hello! I am AURA, your personal voice assistant."
        )

        self.speak(
            "How can I help you?"
        )

        while self.is_running:

            command = self.listen()

            self.process_command(command)

        print("\nAURA has been closed.")


# Application entry point

if __name__ == "__main__":

    try:

        assistant = AuraAssistant()

        assistant.run()

    except KeyboardInterrupt:

        print("\nAURA stopped by user.")

    except Exception as error:

        print(
            f"An unexpected error occurred: {error}"
        )
