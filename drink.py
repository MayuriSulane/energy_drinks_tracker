from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# for holding the resultant list
element_list = []

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get( "https://www.amazon.in/")

input_element = driver.find_element(By.ID, "twotabsearchtextbox")
input_element.clear()
input_element.send_keys("energy drink" + Keys.ENTER)

# Give time for the page to load
time.sleep(3)


# Update these selectors to match the actual HTML structure
titles = driver.find_elements(By.CSS_SELECTOR, "span.a-size-base-plus")
prices = driver.find_elements(By.CSS_SELECTOR, "span.a-price-whole")

# ratings = driver.find_elements(By.CSS_SELECTOR, "span.a-icon-alt")

length = min(len(titles), len(prices))

for i in range(length):
    title = titles[i].text.strip().replace(",","")
    price = prices[i].text.strip().replace(",","")
    # rating = ratings[i].get_attribute("innerHTML").strip().replace(",", "")  # Remove commas from rating
    
    element_list.append([title, price])
    

driver.close()   
    
df = pd.DataFrame(element_list, columns=['Title' , 'Price'])
df.to_csv("energy_drink.csv", index=False)


