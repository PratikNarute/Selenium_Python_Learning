from time import sleep
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
# driver.get("https://pypi.org/project/webdriver-manager/")
# driver.maximize_window()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://devdreamcity.kolonizer.in/login")
driver.maximize_window()
sleep(3)
driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("financial1@kolonizer.com")
driver.find_element(By.XPATH, "//input[@id='mat-input-1']").send_keys("123")
driver.find_element(By.XPATH, "//span[text()='login']/parent::button").click()
sleep(3)
addLeadButton=driver.find_element(By.CSS_SELECTOR, ".addLeadBtn")
print("text of login button:", addLeadButton.text)
addLeadButton.click()
sleep(5)
listWebElement=driver.find_elements(By.XPATH,"//input")
print("listWebElement:", len(listWebElement))


