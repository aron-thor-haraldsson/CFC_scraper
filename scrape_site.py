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

# find hyperlinks, enumerate them and single out the "Privacy Policy"
elems = driver.find_elements(By.CSS_SELECTOR, "[href]")
hyper_links = [elem.get_attribute('href') for elem in elems]
privacy_policy_url = ""
for count, hyper_link in enumerate(hyper_links):
  if hyper_link.find("privacy-policy") > -1:
    print ("The Privacy Policy has a hyperlink index of:", count)
    privacy_policy_url = hyper_link
    break

# go to Privacy Policy and
driver.get(privacy_policy_url)
privacy_text = driver.find_element(By.XPATH, "/html/body").text
privacy_dict = dict()
words = privacy_text.split()
for word in words:
  word = word.strip()
  word = word.lower()
  if word in privacy_dict:
    privacy_dict[word] += 1
  else:
    privacy_dict[word] = 1