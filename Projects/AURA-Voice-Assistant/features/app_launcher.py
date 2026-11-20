
"""
AURA - Application Launcher

Purpose:
Open supported Windows applications.
"""

import subprocess


class AppLauncher:

    def __init__(self):

        # Supported Windows applications
        self.applications = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "calc": "calc.exe",
            "file explorer": "explorer.exe",
            "explorer": "explorer.exe"
        }

    # Open an application
    def open_application(self, app_name):

        app_name = app_name.lower().strip()

        if app_name not in self.applications:

            return False

        try:

            subprocess.Popen(
                [self.applications[app_name]]
            )

            return True

        except OSError as error:

            print("Application Error:", error)

            return False
