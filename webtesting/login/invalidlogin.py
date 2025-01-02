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

    def test_login_invalid_password(self):
        """Negative Test Case: Invalid password"""
        driver = self.driver
        driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shalu23@gmail.com")  # Replace with actual ID
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("Valid1Password@123")  # invalid password
        driver.find_element(By.XPATH, "//button[@id='login-submit']").click()  # Replace with actual Login button ID
        time.sleep(2)

        # Assert error message for invalid password
        error_message = driver.find_element(By.XPATH, "//li[normalize-space()='Invalid login attempt.']")
        self.assertIsNotNone(error_message, "Error message not displayed for invalid password.")
        print("test case successfully executed for invalid password")
        driver.save_screenshot("invalid_password screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
