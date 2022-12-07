from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import re
import json

PATH = r'C:\Program Files (x86)\Google\Chrome\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get("https://www.cfcunderwriting.com")

WebDriverWait(driver, 5)
search = driver.find_element(By.ID, "ccc-notify-accept")
search.click()
WebDriverWait(driver, 5)

# get webpage index and write to text file
webpage_index = driver.page_source
webpage_index_FileWriter = open("webpage_index_file.txt", "w", encoding="utf-8")
webpage_index_FileWriter.write(webpage_index)
webpage_index_FileWriter.close()

# find all external resources by regex pattern
pattern = r"https?://w{0,3}.?[^\"\']*"
matches = re.findall(pattern, webpage_index)
external_resources = [x for x in matches if not x.startswith("https://www.cfcunderwritin")]
with open('external_resources.json', 'w') as json_file:
  json.dump(external_resources, json_file)