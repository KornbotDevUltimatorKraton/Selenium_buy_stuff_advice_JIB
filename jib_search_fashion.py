from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Create a new instance of the web driver (change the path to your specific driver)
driver = webdriver.Chrome('chromedriver')

# Open the URL
driver.get('https://www.jib.co.th/web/branch?bz=&bt=&sb=')
#search_input = driver.find_element_by_name('search_query')
input_element = driver.find_element(By.ID, 'sb')
input_element.clear()  # Clear the current value in the input field
desired_keyword = "สาขา แฟชั่น ไอส์แลนด์ JIB"  # Replace with your desired keyword
input_element.send_keys(desired_keyword)
# Submit the form
input_element.submit()
#CSS_clicker = driver.find_element(By.CSS_SELECTOR, 'div.col-md-12')
#CSS_clicker.click()
wait = WebDriverWait(driver, 10)
element = driver.find_elements(By.CSS_SELECTOR, "div.row.top_box.hidden-xs.hidden-sm")
# Click on the element
#element.click()
for s in element:
       print(s.text)
       s.click() 
'''
elements = driver.find_elements(By.CLASS_NAME,"col-md-12")
print(elements)
# Iterate over the found elements and print their text
for element in elements:
    print(element.text)
'''
time.sleep(5)
driver.quit()
