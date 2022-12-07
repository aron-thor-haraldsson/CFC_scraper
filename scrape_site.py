from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

PATH = r'C:\Program Files (x86)\Google\Chrome\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.cfcunderwriting.com")

WebDriverWait(driver, 5)
search = driver.find_element(By.ID, "ccc-notify-accept")
search.click()
WebDriverWait(driver, 5)