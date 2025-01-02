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

    def test_create_new_query(self):
        """Positive Test Case: Creating new query"""
        driver = self.driver
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shalu30@gmail.com")  # Replace with actual ID
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("Valid1Password@123")  # Replace with actual ID
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()  # Replace with actual Login button ID
        time.sleep(2)

        # Assert successful login
        success_message = driver.find_element(By.XPATH, "//button[normalize-space()='Logout']")
        self.assertIsNotNone(success_message, "Logout")

        driver.find_element(By.XPATH, "//a[normalize-space()='QueryResponse']").click()
        time.sleep(2)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")

        driver.find_element(By.XPATH, "//a[normalize-space()='Create New']").click()
        time.sleep(2)
        create_query_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Create Query Response']")
        self.assertIsNotNone(create_query_message, "Create Query Response")

        driver.find_element(By.XPATH, "//input[@id='QueryID']").send_keys("AQ12786756")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='SrNo']").send_keys("SR12786756")
        time.sleep(2)

        dropdown_element = driver.find_element(By.XPATH, "//select[@id='AgentID']")
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text("AG00001042")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@id='Description']").send_keys("Raising a request for a new insurance")
        time.sleep(2)

        date_input = driver.find_element(By.XPATH, "//input[@id='ResponseDate']").send_keys("02-01-2025")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Create']").click()
        time.sleep(2)

        print("test case successfully executed for creating new query")
        driver.save_screenshot("Create_Query screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
