from selenium import webdriver

PATH = r'C:\Program Files (x86)\Google\Chrome\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.cfcunderwriting.com")