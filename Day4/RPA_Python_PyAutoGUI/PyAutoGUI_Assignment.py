# search for the latest car brands in germany and open the first link in the search results

import pyautogui
import pyperclip
import time
import webbrowser


# ----------------------------
# Safety Settings
# ----------------------------

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1


# ----------------------------
# Open Browser
# ----------------------------

webbrowser.open("https://www.bing.com")

# Wait for browser to open
time.sleep(5)


# ----------------------------
# Search Query
# ----------------------------

search_query = "latest car brands in germany -ai"

# Copy query to clipboard
pyperclip.copy(search_query)

# Paste into search box
pyautogui.hotkey("ctrl", "v")

# Press Enter
pyautogui.press("enter")


# ----------------------------
# Wait for Search Results
# ----------------------------

time.sleep(5)


# ----------------------------
# Open First Search Result
# ----------------------------
FIRST_LINK_X = 420
FIRST_LINK_Y = 350

pyautogui.moveTo(
    FIRST_LINK_X,
    FIRST_LINK_Y,
    duration=1.5
)

pyautogui.click()




"""
# Press TAB multiple times
# until first result is highlighted

for _ in range(10):
    pyautogui.press("tab")
    time.sleep(1)

# Press Enter to open first link
pyautogui.press("enter")"""


# ----------------------------
# Wait After Opening
# ----------------------------

time.sleep(10)

print("Automation completed successfully.")