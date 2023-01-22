from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://www.amazon.de/')
shopping_button = browser.find_element_by_link_text('Best Sellers')
shopping_button.click()
time.sleep(3)
