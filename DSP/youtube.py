from datetime import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#browser exposes an executable file
#Through Selenium test we will invoke the executable file which will then #invoke #actual browser
driver = webdriver.Chrome("chromedriver.exe")
# to maximize the browser window
driver.maximize_window()
#get method to launch the URL

driver.implicitly_wait(10)

driver.get("https://www.youtube.com/watch?v=Cb5nSC2sVX4")



driver.quit()