from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

try:
	browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
	browser.switch_to.alert.accept()
	x = browser.find_element(By.ID, "input_value").text
	f = calc(x)
	browser.find_element(By.ID, "answer").send_keys(f)
	browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

finally:
	time.sleep(5)
	browser.quit()
