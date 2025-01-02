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

    def test_edit_query(self):
        """Positive Test Case: Editing a query"""
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

        # Click on the quickresponse tab
        driver.find_element(By.XPATH, "//a[normalize-space()='QueryResponse']").click()
        time.sleep(2)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")

        # Click on Actions dropdown button
        driver.find_element(By.XPATH, "//tbody/tr[1]/td[6]/div[1]/button[1]").click()
        time.sleep(2)

        # Click on the ByAgent button
        driver.find_element(By.XPATH, "//ul[@class='dropdown-menu show']//a[@class='dropdown-item'][normalize-space()='ByAgent']").click()
        time.sleep(3)
        ByAgent_message = driver.find_element(By.XPATH, "//h1[normalize-space()='ByAgent']")
        self.assertIsNotNone(ByAgent_message, "ByAgent")

        # Click on the back to list button
        driver.find_element(By.XPATH, "//a[normalize-space()='Back to List']").click()
        time.sleep(2)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")

        print("test case successfully executed for ByAgent_message")
        driver.save_screenshot("ByAgent_message screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
