
"""
AURA - Optimized Voice Input

Features:
- One-time microphone calibration
- Faster command listening
- Google speech recognition
- Recognition and listening time measurements
- Error handling
"""

import speech_recognition as sr
import time


class VoiceInput:

    def __init__(self):

        self.recognizer = sr.Recognizer()

        # Microphone recognition settings
        self.recognizer.pause_threshold = 0.6
        self.recognizer.non_speaking_duration = 0.4
        self.recognizer.dynamic_energy_threshold = True

        # Calibrate only once
        self.is_calibrated = False

    def listen(self):

        try:

            with sr.Microphone() as source:

                print("\nAURA is listening...")

                # First-time microphone calibration
                if not self.is_calibrated:

                    print("Calibrating microphone...")

                    self.recognizer.adjust_for_ambient_noise(
                        source,
                        duration=0.5
                    )

                    self.is_calibrated = True

                start_time = time.perf_counter()

                # Optimized listening settings
                audio = self.recognizer.listen(
                    source,
                    timeout=3,
                    phrase_time_limit=5
                )

            print("Recognizing...")

            recognition_start = time.perf_counter()

            command = self.recognizer.recognize_google(audio)

            command = command.lower().strip()

            recognition_time = (
                time.perf_counter() - recognition_start
            )

            total_time = time.perf_counter() - start_time

            print(f"You said: {command}")

            print(
                f"Recognition time: {recognition_time:.2f} seconds"
            )

            print(
                f"Listening + recognition: {total_time:.2f} seconds"
            )

            return command

        except sr.WaitTimeoutError:

            print("No speech detected.")
            return ""

        except sr.UnknownValueError:

            print("Sorry, I could not understand.")
            return ""

        except sr.RequestError:

            print("Recognition service unavailable. Check internet.")
            return ""

        except OSError:

            print("Microphone is unavailable.")
            return ""
