import subprocess
import threading
import time
import random
from datetime import datetime

import pyautogui

pyautogui.FAILSAFE = False

def open_teams():
    """Function to open Microsoft Teams."""
    try:
        # Path to the MS Teams executable
        teams_path = r"C:\Users\yoshi\AppData\Local\Microsoft\WindowsApps\ms-teams.exe"  # Change path
        subprocess.Popen(teams_path)
        print("MS Teams has been opened.")
    except Exception as e:
        print(f"An error occurred while trying to open Teams: {e}")


def close_teams():
    """Function to close Microsoft Teams."""
    try:
        subprocess.call(["taskkill", "/IM", "ms-teams.exe", "/F"])
        print("MS Teams has been closed.")
    except Exception as e:
        print(f"An error occurred while trying to close Teams: {e}")


def move_mouse():
    """Function to move the mouse randomly to prevent sleep and center it every 10 minutes."""
    while True:
        # Move mouse every second
        x, y = pyautogui.position()
        pyautogui.moveTo(x + 5, y + 5)
        pyautogui.moveTo(x, y)
        pyautogui.press("shift")
        time.sleep(1)  # Wait for 1 second
        print("Movement made at {}".format(datetime.now().time()))

def check_teams():
    """Function to open and close Teams based on the time."""
    while True:
        now = datetime.now()
        print("Checking")
        # Check if it's a weekday and current time is between 9 AM and 6 PM
        if now.weekday() < 5:  # 0-4: Monday to Friday
            if now.hour == 9 and now.minute == 8:
                open_teams()
                time.sleep(60)  # Wait 60 seconds to avoid multiple openings within the same minute
            elif now.hour == 18 and now.minute == 12:
                close_teams()
                time.sleep(60)  # Wait 60 seconds to avoid multiple closings within the same minute

        time.sleep(30)  # Check every 30 seconds


if __name__ == "__main__":
    # Start the mouse mover in a separate thread
    mouse_thread = threading.Thread(target=move_mouse, daemon=True)
    mouse_thread.start()

    # Start checking Teams in the main thread
    check_teams()
