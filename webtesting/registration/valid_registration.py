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

    def test_register_valid_inputs(self):
        """Positive Test Case: Valid inputs for registration"""
        driver = self.driver
        register_button = driver.find_element(By.XPATH, "//a[normalize-space()='Register']")  # Replace with actual Register button ID
        register_button.click()
        time.sleep(2)

        # Fill out registration form with valid details

        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shalu3@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("ValidPassword@123")
        driver.find_element(By.XPATH, "//input[@id='Input_ConfirmPassword']").send_keys("ValidPassword@123")
        driver.find_element(By.XPATH, "//button[@id='registerSubmit']").click()  # Replace with actual submit button ID
        time.sleep(5)

        # Assert registration success
        success_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Register confirmation']")
        self.assertIsNotNone(success_message, "Registration failed for valid inputs.")
        print("test case successfully executed for valid registration")
        driver.save_screenshot("valid_registration screenshots.png")
    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
