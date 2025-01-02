
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

    def test_register_existing_user(self):

        # """Positive Test Case: Register with an existing user"""
        driver = self.driver
        register_button = driver.find_element(By.XPATH, "//a[normalize-space()='Register']")
        register_button.click()
        time.sleep(2)

        # Fill out form with existing user details

        driver.find_element(By.XPATH, "//input[@id='Input_Email']").send_keys("shalu35@gmail.com")
        driver.find_element(By.XPATH, "//input[@id='Input_Password']").send_keys("ValidPassword@123")
        driver.find_element(By.XPATH, "//input[@id='Input_ConfirmPassword']").send_keys("ValidPassword@123")
        driver.find_element(By.XPATH, "//button[@id='registerSubmit']").click()
        time.sleep(5)

        # Assert error for existing user
        error_message = driver.find_element(By.XPATH, "//div[@class='container']//li[1]")
        self.assertIsNotNone(error_message, "Error message not displayed for existing user.")
        print("test case successfully executed for Existing user registration")
        driver.save_screenshot("Existing_registration screenshots.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

