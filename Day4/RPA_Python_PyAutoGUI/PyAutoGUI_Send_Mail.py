import pyautogui
import pyperclip
import time
import os


# ----------------------------
# Safety Settings
# ----------------------------

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1


# ----------------------------
# Open Outlook
# ----------------------------

os.system("start outlook")

# Wait for Outlook to open
time.sleep(10)


# ----------------------------
# Create New Mail
# ----------------------------

# CTRL + N opens new mail
pyautogui.hotkey("ctrl", "n")

time.sleep(5)


# ----------------------------
# Enter Recipient
# ----------------------------

recipient = "kaarthikl@gmail.com"

pyperclip.copy(recipient)

pyautogui.hotkey("ctrl", "v")

time.sleep(1)

# Move to Subject field
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")


# ----------------------------
# Enter Subject
# ----------------------------

subject = "Test Mail from PyAutoGUI"

pyperclip.copy(subject)

pyautogui.hotkey("ctrl", "v")

time.sleep(1)

# Move to Email Body
pyautogui.press("tab")


# ----------------------------
# Enter Email Body
# ----------------------------

body = """
Hello Kaarthik,

This is an automated email sent using Python PyAutoGUI.

Regards,
Automation Bot
"""

pyperclip.copy(body)

pyautogui.hotkey("ctrl", "v")

time.sleep(2)


# ----------------------------
# Send Email
# ----------------------------

# CTRL + ENTER sends mail
pyautogui.hotkey("ctrl", "enter")

time.sleep(2)

# Confirm send if popup appears
pyautogui.press("enter")

print("Email sent successfully.")