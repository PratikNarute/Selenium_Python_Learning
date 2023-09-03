from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://devdreamcity.kolonizer.in/login")
driver.maximize_window()
sleep(3)
button=driver.find_element(By.XPATH, "//span[text()='login']/parent::button")
source = driver.find_element(By.XPATH, "")
target = driver.find_element(By.XPATH, "")
ma = ActionChains()
ma.move_to_element(button).perform()
ma.click(button).perform()
ma.send_keys().perform()
ma.context_click(button).perform()
ma.double_click().perform()
ma.double_click().perform()
ma.drag_and_drop(source,target)
ma.key_down().perform()
ma.key_up().perform()
ma.pause().perform()
ma.release().perform()
ma.scroll_to_element(button).perform()
