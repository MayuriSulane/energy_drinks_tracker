from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# for holding the resultant list
element_list = []

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get( "https://www.amazon.in/")

input_element = driver.find_element(By.ID, "twotabsearchtextbox")
input_element.clear()
input_element.send_keys("energy drink" + Keys.ENTER)

for page in range(1, 2, 1):
    
    driver.get(f"https://www.amazon.in/s?k=energy+drink&page={page}")
    
    # Give time for the page to load
    time.sleep(3)

    # Update these selectors to match the actual HTML structure
    titles = driver.find_elements(By.CSS_SELECTOR, "span.a-text-normal")
    prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")
    # descriptions = driver.find_elements(By.CSS_SELECTOR, "span.a-text-normal")  # Adjust as necessary
    
    for i in range(len(titles)):
        title = titles[i].text if i < len(titles) else 'N/A'
        price = prices[i+1].text if i+1 < len(prices) else 'N/A'
        # description = descriptions[i].text if i < len(descriptions) else 'N/A'
        element_list.append([title, price])
    
    driver.close()
    for item in element_list:
        print(item)
