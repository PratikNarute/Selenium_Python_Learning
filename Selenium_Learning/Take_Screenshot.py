from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://devdreamcity.kolonizer.in/login")
driver.maximize_window()
sleep(3)

driver.get_screenshot_as_file("C:\\Users\\Lenovo\\PycharmProjects\\AutomationPython_Learning\\Screenshot\\failed.png")
# driver.save_screenshot("C:\\Users\\Lenovo\\PycharmProjects\\AutomationPython_Learning\\Screenshot\\failed1.png")
