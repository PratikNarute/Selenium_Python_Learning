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
driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("financial1@kolonizer.com")
driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("123")
driver.find_element(By.XPATH, "//span[text()='login']/parent::button").click()
sleep(3)
actions = ActionChains(driver)
projectSetup=driver.find_element(By.XPATH, "//div[text()='Project Setup']/parent::div/parent::a")
actions.context_click(projectSetup).perform()
sleep(6)

mainWindow = driver.current_window_handle  #It return the address id of main window
print("Address id of mainWindow:", mainWindow)
multipleWindow = driver.window_handles # It return the address id of child windows
print("Address id of childWindow:",multipleWindow)

for index in multipleWindow:
      if index==1:
       driver.switch_to.window(index)