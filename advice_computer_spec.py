from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
# Create a new instance of the web driver (change the path to your specific driver)
driver = webdriver.Chrome('chromedriver')

# Open the URL
driver.get('https://www.advice.co.th')
#search_input = driver.find_element_by_name('search_query')

list_products = ['CPU INTEL CORE I9-13900K LGA 1700','VGA ASUS GEFORCE RTX 4090 ROG STRIX O24G GAMING -24GB GDDR6X','RAM DDR5(6200) 32GB (16GBX2) CORSAIR DOMINATOR PLATINU M BLACK RGB CMT32GX5M2X6200C36','2 TB HDD WD BLUE 7200RPM,2 56MB,SAT-3, WD20EZBX','POWER SUPPLY (80+PLATINUM) 1200W ASUS ROG THOR 12 00P','ATX CASE (NP) CORSAIR ICUE 5 000X RGB TG (WHITE)']
for i in list_products: 
     form_element = driver.find_element(By.ID, "form-search-new")
     # Find the input element within the form
     input_element = form_element.find_element(By.NAME, "keyword")
     # Clear the input field (optional)
     input_element.clear()
     # Type the search query into the input field
     input_element.send_keys(i)
     # Submit the form to perform the search
     form_element.submit()
     #product_column = driver.find_element(By.CLASS_NAME,'product-column-4')
     #product_column = driver.find_element(By.CLASS_NAME, 'product-column-4') 
     wait = WebDriverWait(driver, 10)
     product_column = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-column-4')))
     print(product_column)
     element_text = product_column.text
     print(element_text)
     item = product_column.find_element(By.CLASS_NAME, 'online-btn-cart')
     item.click() 
     button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.btn.btn-outline-primary')))
     # Click on the button
     button.click()
     time.sleep(1)
     if i == list_products[len(list_products)-1]:
                 print("Now checking total price of product")
                 dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'dropdown')))
                 # Click on the dropdown
                 dropdown.click() 
time.sleep(5)
driver.quit() 

