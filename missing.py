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
create_new=driver.find_element(By.XPATH,"/html/body/div/main/p/a").click()
query_id=driver.find_element(By.ID,"QueryID").send_keys("")
SrNo=driver.find_element(By.ID,"SrNo").send_keys("")
agent_id=driver.find_element(By.ID,"AgentID").send_keys("")
Description=driver.find_element(By.ID,"Description").send_keys("")
ResponseDate=driver.find_element(By.ID,"ResponseDate").send_keys("")
create_button=driver.find_element(By.XPATH,"/html/body/div/main/div[1]/div/form/div[6]/input").click()
time.sleep(3)
qid_err=driver.find_element(By.XPATH,"//span[@id='QueryID-error']")
print("The QueryID field is required.")
srno_err=driver.find_element(By.XPATH,"//span[@id='SrNo-error']")
print("The SrNo field is required.")
d_err=driver.find_element(By.XPATH,"//span[@id='Description-error']")
print("The Description field is required.")

