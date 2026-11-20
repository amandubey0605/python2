
"""
AURA - Optimized Voice Output
"""

import subprocess
import base64
import atexit


_speech_process = None


def start_speech_engine():

    global _speech_process

    if (
        _speech_process is not None
        and _speech_process.poll() is None
    ):
        return

    script = r"""
Add-Type -AssemblyName System.Speech

$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speaker.Rate = 0
$speaker.Volume = 100

while ($true) {

    $line = [Console]::In.ReadLine()

    if ($null -eq $line -or $line -eq "__AURA_EXIT__") {
        break
    }

    try {

        $message = [System.Text.Encoding]::UTF8.GetString(
            [System.Convert]::FromBase64String($line)
        )

        $speaker.Speak($message)

    }
    catch {
        # Continue running if one message fails
    }
}

$speaker.Dispose()
"""

    _speech_process = subprocess.Popen(
        [
            "powershell.exe",
            "-NoProfile",
            "-NonInteractive",
            "-Command",
            script
        ],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="ascii"
    )


def speak(text):

    print(f"AURA: {text}")

    global _speech_process

    try:

        start_speech_engine()

        encoded_text = base64.b64encode(
            text.encode("utf-8")
        ).decode("ascii")

        _speech_process.stdin.write(
            encoded_text + "\n"
        )

        _speech_process.stdin.flush()

    except Exception as error:

        print("Speech Error:", error)


def stop_speech_engine():

    global _speech_process

    if _speech_process is None:
        return

    try:

        if _speech_process.poll() is None:

            _speech_process.stdin.write("__AURA_EXIT__\n")
            _speech_process.stdin.flush()
            _speech_process.stdin.close()

            try:
                _speech_process.wait(timeout=3)

            except subprocess.TimeoutExpired:
                _speech_process.terminate()

    except Exception:
        pass

    _speech_process = None


atexit.register(stop_speech_engine)
