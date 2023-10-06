from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import requests
import time

PROFILE_ID = "162769430"
req_url = f"http://localhost:3001/v1.0/browser_profiles/{PROFILE_ID}/start?automation=1"

response = requests.get(req_url)
response_json = response.json()
port = response_json["automation"]["port"]

driver_path = Service("chromedriver\chromedriver-windows-x64.exe")
options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:"+str(port)

driver = webdriver.Chrome(service=driver_path, options=options)
driver.get("https://google.com")
