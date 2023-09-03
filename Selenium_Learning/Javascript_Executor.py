from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://devdreamcity.kolonizer.in/login")
driver.maximize_window()
sleep(3)


username=driver.find_element(By.XPATH, "//input[@id='mat-input-0']")
driver.execute_script("arguments[0].value = arguments[1];", username, "financial1@kolonizer.com")
sleep(1)
password = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")
driver.execute_script("arguments[0].value = arguments[1];", password, "123")
sleep(2)
login=driver.find_element(By.XPATH, "//span[text()='login']/parent::button")
login.click()
sleep(5)