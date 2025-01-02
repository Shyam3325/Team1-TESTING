import unittest
from xml.etree.ElementTree import XMLID

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class TestCustomerQuery(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://abzmvcapp-chanad.azurewebsites.net/")
        time.sleep(3)

    def test_details_query(self):
        """Positive Test Case: Details of a query"""
        driver = self.driver
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shalu30@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("Valid1Password@123")
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()
        time.sleep(2)

        # Assert successful login
        success_message = driver.find_element(By.XPATH, "//button[normalize-space()='Logout']")
        self.assertIsNotNone(success_message, "Logout")

        driver.find_element(By.XPATH, "//a[normalize-space()='QueryResponse']").click()
        time.sleep(2)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")
        driver.find_element(By.XPATH, "//tbody/tr[1]/td[6]/div[1]/button[1]").click()
        time.sleep(2)

        driver.find_element(By.XPATH, "//ul[@class='dropdown-menu show']//a[@class='dropdown-item'][normalize-space()='Details']").click()
        time.sleep(3)
        # Assert Details Query Response
        details_query_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Details Query Response']")
        self.assertIsNotNone(details_query_message, "Details Query Response")

        edit_button = driver.find_element(By.XPATH,"//a[normalize-space()='Edit']").click()

        query_id = driver.find_element(By.XPATH, "//input[@id='QueryID']")
        query_id.clear()
        query_id.send_keys("QU12786756")
        time.sleep(2)

        serial_num = driver.find_element(By.XPATH, "//input[@id='SrNo']")
        serial_num.clear()
        serial_num.send_keys("SR12786756")
        time.sleep(2)

        agent_id = driver.find_element(By.XPATH, "//input[@id='AgentID']")
        agent_id.clear()
        agent_id.send_keys("AN12786756")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@value='Save']").click()
        time.sleep(2)

        print("test case successfully executed for details query")
        driver.save_screenshot("Details_Query screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
