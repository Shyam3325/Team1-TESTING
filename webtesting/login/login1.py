from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://abzmvcapp-chanad.azurewebsites.net/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"/html/body/header/nav/div/div/ul[2]/li[2]/a").click()
email=driver.find_element(By.ID,"Input_Email").send_keys("konnegarishivani09@gmail.com")
password=driver.find_element(By.ID,"Input_Password").send_keys("Shiv@ni032002")
login_button=driver.find_element(By.ID,"login-submit").click()