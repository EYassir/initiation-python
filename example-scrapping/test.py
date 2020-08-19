from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

url ='https://www.youtube.com/'
driver = webdriver.Firefox()
driver.get(url)

delay = 5 # seconds

try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_elements_by_xpath('..//elementid')))
    print ("Page is ready!")
    for image in driver.find_elements_by_xpath('..//img[@src]'):
        print (image.get_attribute('src'))
except TimeoutException:
    print ("Couldn't load page")