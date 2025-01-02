import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLoginFeature(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://abzmvcapp-chanad.azurewebsites.net/")
        time.sleep(3)

    def test_login_empty_fields(self):
        """Negative Test Case: Empty username and password"""
        driver = self.driver
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='Input_Email']").clear()  # Clear username field
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").clear()  # Clear password field
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()  # Replace with actual Login button ID
        time.sleep(2)

        # Assert error message for empty fields
        error_message = driver.find_element(By.XPATH, "//span[@id='Input_Email-error']")
        self.assertIsNotNone(error_message, "The Email field is required.")

        # Assert successful login
        success_message = driver.find_element(By.XPATH, "//span[@id='Input_Password-error']")
        self.assertIsNotNone(success_message, "The Password field is required.")
        print("test case successfully executed for invalid password")
        driver.save_screenshot("invalid_password screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
