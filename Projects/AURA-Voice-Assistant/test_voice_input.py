
from core.voice_input import VoiceInput

voice = VoiceInput()

command = voice.listen()

print("Final Command:", command)
