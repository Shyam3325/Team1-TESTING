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
        time.sleep(3)  # Allow the page to load

    def test_login_valid_credentials(self):
        """Positive Test Case: Valid credentials"""
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
        print("test case successfully executed for valid credentials")
        driver.save_screenshot("valid_credentials screenshot.png")



    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
