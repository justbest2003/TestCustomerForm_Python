import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class TestGoogleWebsite(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome WebDriver
        s = Service('D:\DriverWeb\chromedriver.exe')     
        self.driver = webdriver.Chrome(service=s)

    def test01(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canonc")
        ageInput.send_keys("2")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case1.png")

    def test02(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("Johnj")
        lastNameInput.send_keys("canoncanoncano")
        ageInput.send_keys("149")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case2.png")

    def test03(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjo")
        lastNameInput.send_keys("canoncanoncanon")
        ageInput.send_keys("150")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case3.png")

    def test04(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("Johnjohnjohnjo")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case4.png")

    def test05(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohnjohnjoh")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case5.png")

    def test06(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("John")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case6.png")

    def test08(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("cano")
        ageInput.send_keys("75")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case8.png")

    def test10(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("0")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case10.png")

    def test11(self):
        self.driver.get("http://localhost/customer/index.html")

        firstNameInput = self.driver.find_element(By.ID, "firstname")
        lastNameInput = self.driver.find_element(By.ID, "lastname")
        ageInput = self.driver.find_element(By.ID, "age")
        submitButton = self.driver.find_element(By.ID, "sub")
        firstNameInput.send_keys("johnjohn")
        lastNameInput.send_keys("canoncan")
        ageInput.send_keys("151")

        submitButton.click()

        result = self.driver.find_element(By.ID, "formname").text
        self.assertEqual("Customer Details Form", result)

        self.driver.save_screenshot("img/test_case11.png")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
