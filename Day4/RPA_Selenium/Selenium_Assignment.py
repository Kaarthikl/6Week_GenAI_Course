# Selenium Login Automation for:
# https://yuvabharathierp.org/

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# -----------------------------------
# CHROME SETUP
# -----------------------------------

options = Options()

# Disable popups and notifications
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 20)

# -----------------------------------
# OPEN WEBSITE
# -----------------------------------

driver.get("https://yuvabharathierp.org/site/userlogin")

print("Website opened successfully")

# -----------------------------------
# ENTER USERNAME
# -----------------------------------

username = wait.until(
    EC.presence_of_element_located((By.NAME, "username"))
)

username.send_keys("YOUR_USERNAME")


print("Username entered")

# -----------------------------------
# ENTER PASSWORD
# -----------------------------------

password = wait.until(
    EC.presence_of_element_located((By.NAME, "password"))
)

password.send_keys("YOUR_PASSWORD")


print("Password entered")

# -----------------------------------
# CLICK LOGIN BUTTON
# -----------------------------------

login_button = wait.until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login_page"]/div[2]/div[3]/div/form/button'))
)

login_button.click()

print("Login button clicked")

# -----------------------------------
# VALIDATION
# -----------------------------------

time.sleep(5)

current_url = driver.current_url

print("Current URL:", current_url)

if "dashboard" in current_url.lower():
    print("Login Successful")
else:
    print("Login may have failed or needs captcha/OTP")

# -----------------------------------
# CLOSE BROWSER
# -----------------------------------

time.sleep(5)

driver.quit()