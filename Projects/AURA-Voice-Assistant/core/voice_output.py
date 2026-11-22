
"""
AURA - Optimized and Synchronized Voice Output

Features:
- Persistent Windows System.Speech engine
- Base64 text transfer
- Synchronized speech playback
- Startup time measurement
- Speech playback time measurement
- Automatic process cleanup
"""

import subprocess
import base64
import atexit
import time


_speech_process = None


def start_speech_engine():

    global _speech_process

    # Reuse the existing speech process
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

[Console]::Out.WriteLine("READY")
[Console]::Out.Flush()

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
    finally {

        [Console]::Out.WriteLine("DONE")
        [Console]::Out.Flush()

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
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
        encoding="ascii",
        bufsize=1
    )

    response = _speech_process.stdout.readline().strip()

    if response != "READY":

        _speech_process.terminate()
        _speech_process = None

        raise RuntimeError(
            "AURA speech engine failed to start."
        )


def speak(text):

    global _speech_process

    print(f"AURA: {text}")

    try:

        # Check whether the engine is already running
        engine_already_running = (
            _speech_process is not None
            and _speech_process.poll() is None
        )

        engine_start = time.perf_counter()

        start_speech_engine()

        # Measure startup only when a new process was needed
        if not engine_already_running:

            startup_time = (
                time.perf_counter() - engine_start
            )

            print(
                f"Speech engine startup: {startup_time:.2f} seconds"
            )

        # Convert text into Base64
        encoded_text = base64.b64encode(
            str(text).encode("utf-8")
        ).decode("ascii")

        # Start measuring speech playback
        speech_start = time.perf_counter()

        _speech_process.stdin.write(
            encoded_text + "\n"
        )

        _speech_process.stdin.flush()

        # Wait until PowerShell finishes speaking
        response = _speech_process.stdout.readline().strip()

        speech_time = (
            time.perf_counter() - speech_start
        )

        if response != "DONE":

            raise RuntimeError(
                "Speech engine did not confirm completion."
            )

        print(
            f"Speech playback time: {speech_time:.2f} seconds"
        )

    except Exception as error:

        print("Speech Error:", error)


def stop_speech_engine():

    global _speech_process

    if _speech_process is None:
        return

    try:

        if _speech_process.poll() is None:

            _speech_process.stdin.write(
                "__AURA_EXIT__\n"
            )

            _speech_process.stdin.flush()
            _speech_process.stdin.close()

            try:

                _speech_process.wait(timeout=3)

            except subprocess.TimeoutExpired:

                _speech_process.terminate()
                _speech_process.wait(timeout=2)

    except Exception:
        pass

    finally:

        _speech_process = None


# Automatically stop the engine when Python exits
atexit.register(stop_speech_engine)
