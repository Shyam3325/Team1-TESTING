import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestRegisterPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("https://abzmvcapp-chanad.azurewebsites.net/")
        time.sleep(2)  # Wait for the page to load



    def test_register_invalid_email(self):
        """Negative Test Case: Invalid email format"""
        driver = self.driver
        register_button = driver.find_element(By.XPATH, "//a[normalize-space()='Register']")
        register_button.click()
        time.sleep(2)

    # Fill out form with an invalid email

        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shaemail@.com")
        error_message = driver.find_element(By.XPATH, "//span[@data-valmsg-for='Input.Email']")
        self.assertIsNotNone(error_message, "Error message not displayed for invalid email format.")
        print(error_message)

        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("Password123")
        driver.find_element(By.XPATH, "//input[@id='Input_ConfirmPassword']").send_keys("Password123")
        driver.find_element(By.XPATH, "//button[@id='registerSubmit']").click()
        time.sleep(2)

        print("test case invalid emailid in registration page")
        driver.save_screenshot("invalid_registration screenshots.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()