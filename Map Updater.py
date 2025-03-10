import win32clipboard
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Pasting latest clipboard data to IsleMap Website
def PasteToMap(data):
    coordsinput = wait.until(EC.visibility_of_element_located((By.ID, "PastedCoords")))
    coordsinput.clear()
    coordsinput.send_keys((data) + "\n")

# Getting clipboard data
def get_clipboard_data():
    win32clipboard.OpenClipboard()
    try:
        data = win32clipboard.GetClipboardData()
    except TypeError:
        data = None
    finally:
        win32clipboard.CloseClipboard()
    return data


# Setting up webdriver and launching website
previous_data = get_clipboard_data()
cService = webdriver.ChromeService(executable_path='C:/Users/Boxca/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service=cService)
wait = WebDriverWait(driver, 10)
driver.get("https://www.islemaps.com/")


# Main loop checking for any clipboard updates
while True:
    current_data = get_clipboard_data()
    if current_data != previous_data and current_data is not None:
        print("Clipboard updated:", current_data)
        PasteToMap(current_data)
        previous_data = current_data
    time.sleep(1)