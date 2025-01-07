import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestEditCustomerFeature(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://abzvehiclemvcwebapp-akshitha.azurewebsites.net/")
        time.sleep(3)  # Allow the page to load

    def test_edit_customer(self):
        """Positive Test Case: Creating new customer"""
        driver = self.driver
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shalu23@gmail.com")  # Replace with actual ID
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("ValidPassword@123")  # Replace with actual ID
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()  # Replace with actual Login button ID
        time.sleep(2)

        # Assert successful login
        welcome_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Welcome']")
        self.assertIsNotNone(welcome_message, "Welcome")

        driver.find_element(By.XPATH,"//a[normalize-space()='Customer']").click()
        customer_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(customer_message, "Index")
        time.sleep(2)
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/a[1]").click()
        edit_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Edit']")
        self.assertIsNotNone(edit_message, "edit")

        driver.find_element(By.XPATH, "//input[@id='CustomerName']").clear()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerName']").send_keys("John Jacobaaas")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerAddress']").clear()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerAddress']").send_keys("austin, New Jersey")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Save']").click()
        time.sleep(4)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")

        print("test case successfully executed for  edit customer")
        driver.save_screenshot("edit_customer screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
