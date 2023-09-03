from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://devdreamcity.kolonizer.in/login")
driver.maximize_window()
sleep(3)
# driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("financial1@kolonizer.com")
# driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("123")
# sleep(1)
# driver.find_element(By.XPATH, "//span[text()='login']/parent::button").click()
# sleep(3)
# driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH,"//div[normalize-space()='Financial Setup']"))
# sleep(3)
# driver.execute_script("arguments[0].click();", driver.find_element(By.XPATH, "//span[normalize-space()='Create Item Group sub Group']"))
# sleep(6)
# driver.switch_to.frame(driver.find_element(By.XPATH, "//app-item-hierarchy//iframe"))
# sleep(4)
# driver.find_element(By.XPATH, "//body//flt-glass-pane").click()
# sleep(10)

driver.switch_to.frame() # It take three types of arguments 1) Webelement 2) id 3) index
