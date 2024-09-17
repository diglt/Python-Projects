typing_speed = 0.000001

# required modules
# selenium - pip install selenium
# bs4 - pip install bs4
# pyautogui - pip install pyautogui

from selenium import webdriver
from bs4 import BeautifulSoup
import pyautogui
import time

driver = webdriver.Edge()

driver.get("https://monkeytype.com")

time.sleep(5)  

need_to_run = True

while need_to_run:
    html_content = driver.page_source

    soup = BeautifulSoup(html_content, 'html.parser')

    for div in soup.find_all('div', class_='word active'):
        print("Found div:", div)
        word = ""
        
        # Extract and index the letters inside this div
        for letter in div.get_text(strip=True):
            word += letter
        
        word += " "
        
        pyautogui.write(word, interval=0.000001)

        word = ""
