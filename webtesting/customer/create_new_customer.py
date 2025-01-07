import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCreateCustomerFeature(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://abzvehiclemvcwebapp-akshitha.azurewebsites.net/")
        time.sleep(3)  # Allow the page to load

    def test_create_new_customer(self):
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

        driver.find_element(By.XPATH,"//a[normalize-space()='Create New']").click()
        create_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Create']")
        self.assertIsNotNone(create_message, "Create")

        driver.find_element(By.XPATH, "//input[@id='CustomerID']").send_keys("john_jacob")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerName']").send_keys("John Jacob")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerPhone']").send_keys("9878675634")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerEmail']").send_keys("john_jacob34@gmail.com")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='CustomerAddress']").send_keys("Texas, New Jersey")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@value='Create']").click()
        time.sleep(4)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")

        print("test case successfully executed for create new customer")
        driver.save_screenshot("create_new_customer screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
