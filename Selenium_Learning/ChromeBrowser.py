
from time import sleep

from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome()
# driver.get("http://devdreamcity.kolonizer.in/login")
# sleep(7)

class Wait:
    def openbrowser(self):
        global driver
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver = webdriver.Chrome()
        driver.get("http://devdreamcity.kolonizer.in/login")
        driver.maximize_window()
        sleep(3)

    def implicitWait(self):
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@id='mat-input-0']").send_keys("financial1@kolonizer.com")

    def explicitWait(self):
        explicitWait = WebDriverWait(driver, 10)
        password = driver.find_element(By.XPATH, "//input[@id='mat-input-1']")
        explicitWait.until(EC.visibility_of(password))
        password.send_keys("123")

    def fluentWait(self):
        fluentWait = WebDriverWait(driver, 10, 2, ignored_exceptions=[StaleElementReferenceException])
        loginButton = driver.find_element(By.XPATH, "//span[text()='login']/parent::button")
        fluentWait.until(EC.element_to_be_clickable(loginButton))
        loginButton.click()
        sleep(2)
        addLeadButton = driver.find_element(By.CSS_SELECTOR, ".addLeadBtn")
        fluentWait.until(EC.element_to_be_clickable(addLeadButton))
        addLeadButton.click()
        sleep(5)


wait = Wait()
wait.openbrowser()
wait.implicitWait()
wait.explicitWait()
wait.fluentWait()