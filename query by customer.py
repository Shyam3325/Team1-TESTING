from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://abzmvcapp-chanad.azurewebsites.net/")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[2]/li[2]/a").click()
email=driver.find_element(By.ID,"Input_Email").send_keys("konnegarishivani09@gmail.com")
password=driver.find_element(By.ID,"Input_Password").send_keys("Shiv@ni032002")
login_button=driver.find_element(By.ID,"login-submit").click()
time.sleep(3)
query_response=driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[1]/li[11]/a").click()
time.sleep(2)
dropdown=driver.find_element(By.ID,"dropdownMenuButton").click()
bycustomer=driver.find_element(By.XPATH,"/html/body/div/main/table/tbody/tr[1]/td[6]/div/ul/li[4]/a").click()
driver.find_element(By.XPATH,"/html/body/div/main/a").click()