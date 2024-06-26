from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://www.amazon.in/")


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "hm-icon-label"))
)

input_element = driver.find_element(By.CLASS_NAME, "hm-icon-label")
input_element.clear()
input_element.send_keys("All" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.button, "nav_em_1_1_1_19"))
)

input_element = driver.find_element(By.button, "nav_em_1_1_1_19")
input_element.clear()
input_element.send_keys("Beauty, Health, Grocery" + Keys.ENTER)


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "hmenu-item"))
)

input_element = driver.find_element(By.CLASS_NAME, "hmenu-item")
input_element.clear()
input_element.send_keys("Coffee, Tea & Beverages" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
link.click()

time.sleep(10)

driver.quit()

