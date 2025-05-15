import pytest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


get_title_courses = 'GUVI | courses'
get_title_login = 'GUVI | Login'
get_title_signup = 'GUVI | Sign Up'


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    yield driver
    # Cleanup code after tests are done
    driver.quit()


driver = webdriver.Chrome()
driver.get("https://www.guvi.in/")
time.sleep(2)
driver.maximize_window()
time.sleep(2)
# Validating the Dynamic Xpath using pytest and selenium
driver.find_element(By.XPATH,'/html/body/main/div[1]/div/div[4]/a').click()
time.sleep(2)
get_title_courses = driver.title 
# Printing the title of this URL 
print(f"Title of the Courses:",[get_title_courses]) 
time.sleep(2)
# Go back to the previous page
driver.back()  
time.sleep(2)
driver.find_element(By.XPATH,"//p[@id='liveclasseslink']").click() 
time.sleep(2)
driver.find_element(By.XPATH,"//p[@id='practiceslink']").click()  
time.sleep(2)
driver.find_element(By.XPATH,"//p[@id='resourceslink']").click()  
time.sleep(2)
driver.find_element(By.XPATH,"//p[@id='solutionslink']").click()  
time.sleep(2)
driver.find_element(By.XPATH,"//a[@id='login-btn']").click()  
time.sleep(2)
get_title_login = driver.title 
# Printing the title of this URL 
print(f"Title of the Login:",[get_title_login]) 
time.sleep(2)
driver.back() 
time.sleep(2)
driver.find_element(By.XPATH,"//a[contains (text(), 'Sign up')]").click()  
time.sleep(2)
get_title_signup = driver.title 
# Printing the title of this URL 
print(f"Title of the Sign up:",[get_title_signup]) 
time.sleep(2)
driver.back()  
time.sleep(2)
driver.quit()
