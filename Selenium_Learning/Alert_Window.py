from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://devdreamcity.kolonizer.in/login")
driver.maximize_window()
sleep(3)

Alert = driver.switch_to.alert
Alert.send_keys("")
Alert.accept()
Alert.dismiss()
Alert.text()  # To get the text of alert window