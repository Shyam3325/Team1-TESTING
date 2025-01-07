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

        driver.find_element(By.XPATH, "//input[@value='Create']").click()
        time.sleep(4)

        driver.find_element(By.XPATH, "//input[@id='CustomerID']").clear()
        time.sleep(2)
        customerID_message = driver.find_element(By.XPATH, "//span[@id='CustomerID-error']")
        self.assertIsNotNone(customerID_message, "The CustomerID field is required.")

        driver.find_element(By.XPATH, "//input[@id='CustomerName']").clear()
        time.sleep(2)
        customerName_message = driver.find_element(By.XPATH, "//span[@id='CustomerName-error']")
        self.assertIsNotNone(customerName_message, "The CustomerName field is required.")

        driver.find_element(By.XPATH, "//input[@id='CustomerPhone']").clear()
        time.sleep(2)
        customerPhone_message = driver.find_element(By.XPATH, "//span[@id='CustomerPhone-error']")
        self.assertIsNotNone(customerPhone_message, "The CustomerPhone field is required.")

        driver.find_element(By.XPATH, "//input[@id='CustomerEmail']").clear()
        time.sleep(2)
        customerEmail_message = driver.find_element(By.XPATH, "//span[@id='CustomerEmail-error']")
        self.assertIsNotNone(customerEmail_message, "The CustomerEmail field is required.")

        driver.find_element(By.XPATH, "//input[@id='CustomerAddress']").clear()
        time.sleep(2)



        # index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        # self.assertIsNotNone(index_message, "Index")

        print("test case successful executed for empty filed")
        driver.save_screenshot("empty_customer screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
