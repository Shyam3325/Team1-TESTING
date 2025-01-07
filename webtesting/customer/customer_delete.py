import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestCustomerDeleteFeature(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup WebDriver
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get("http://abzvehiclemvcwebapp-akshitha.azurewebsites.net/")
        time.sleep(3)  # Allow the page to load

    def test_customer_delete(self):
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
        #assert index
        driver.find_element(By.XPATH,"//a[normalize-space()='Customer']").click()
        customer_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(customer_message, "Index")
        time.sleep(2)
        #assert delete
        driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/a[3]").click()
        delete_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Delete']")
        self.assertIsNotNone(delete_message, "delete")


         #delete button
        driver.find_element(By.XPATH, "//input[@value='Delete']").click()
        time.sleep(2)
        #index page
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")
        #again delete assert
        driver.find_element(By.XPATH, "//tbody/tr[2]/td[6]/a[3]").click()
        time.sleep(2)
        delete_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Delete']")
        self.assertIsNotNone(delete_message, "delete")





        driver.find_element(By.XPATH, "//a[normalize-space()='Back to List']").click()
        time.sleep(2)
        index_message = driver.find_element(By.XPATH, "//h1[normalize-space()='Index']")
        self.assertIsNotNone(index_message, "Index")




        print("test case successfully executed for customer_delete")
        driver.save_screenshot("customer_delete screenshot.png")

    @classmethod
    def tearDownClass(cls):
        # Close the browser
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()
