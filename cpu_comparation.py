from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
# Create a new instance of the web driver (change the path to your specific driver)
driver = webdriver.Chrome('chromedriver')

# Open the URL
driver.get('https://www.jib.co.th/web/')
#search_input = driver.find_element_by_name('search_query')
#search_input = driver.find_element(By.ID, 'productTitle')
#search_input.clear()
search_list = ['INTEL CORE I7-12700K','CORE I9-12900K'] 
for i in search_list:
       search_input = driver.find_element(By.ID, 'productTitle')
       search_input.clear()
       search_input.send_keys(i)
       search_input.send_keys(Keys.ENTER)
       #search_input.send_keys(Keys.RETURN)
       print(search_input)
       time.sleep(3)

time.sleep(5)
driver.quit()
