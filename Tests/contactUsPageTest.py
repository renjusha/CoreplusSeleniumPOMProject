from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Edge

from Pages.contactUsPage import ContactusPage
from Locators.locators import Locators
import unittest
import HtmlTestRunner


class LoginTest(unittest.TestCase):
     # setup method during class initializaion - done once
     @classmethod
     def setUpClass(cls):
          cls.driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/CorePlusSeleniumProject/Drivers/chromedriver.exe")
          # cls.driver = webdriver.Firefox(executable_path= "C:/Users/User/PycharmProjects/CoreplusSeleniumPOMProject/Drivers/geckodriver.exe")
          # cls.driver=webdriver.Edge(executable_path="C:/Users/User/PycharmProjects/CoreplusSeleniumPOMProject/Drivers/msedgedriver.exe")
          cls.driver.implicitly_wait(10)
          cls.driver.maximize_window()

     # success test scenario with implicit wait
     def test_01_success_submission_01(self):
           driver = self.driver
           driver.get("https://coreplus.com.au/contact/")
           contactus = ContactusPage(driver)
           contactus.enter_name("QATest")
           contactus.enter_phone("0464935234")
           contactus.enter_email("test@test.com")
           contactus.enter_message("I like pineapples")
           contactus.click_submit_button()
           message = contactus.verify_success_message()
           print(message)
           self.assertEqual(message, "Your message was sent successfully. Thanks.")

     # success test scenario with explicit wait
     def test_01_success_submission_02(self):
           driver = self.driver
           driver.get("https://coreplus.com.au/contact/")
           contactus = ContactusPage(driver)
           contactus.enter_name("QATest")
           contactus.enter_phone("0464935234")
           contactus.enter_email("test@test.com")
           contactus.enter_message("I like pineapples")
           contactus.click_submit_button()
           wait =WebDriverWait(contactus.driver,10)
           message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, Locators.verify_message_class_name)))

     # empty name scenario
     def test_02_empty_name(self):
         driver = self.driver
         driver.get("https://coreplus.com.au/contact/")
         contactus = ContactusPage(driver)
         contactus.enter_phone("0464935234")
         contactus.enter_email("test@test.com")
         contactus.enter_message("I like pineapples")
         contactus.click_submit_button()
         message = contactus.verify_error_message()
         self.assertEqual(message, "Validation errors occurred. Please confirm the fields and try again.")

    # empty phone scenario
     def test_03_empty_phone(self):
         driver = self.driver
         driver.get("https://coreplus.com.au/contact/")
         contactus = ContactusPage(driver)
         contactus.enter_name("QATest")
         contactus.enter_email("test@test.com")
         contactus.enter_message("I like pineapples")
         contactus.click_submit_button()
         message = contactus.verify_error_message()
         self.assertEqual(message, "Validation errors occurred. Please confirm the fields and try again.")

     # invalid phone scenario - error because it is not handled in application
     def test_04_invalid_phone(self):
         driver = self.driver
         driver.get("https://coreplus.com.au/contact/")
         contactus = ContactusPage(driver)
         contactus.enter_name("QATest")
         contactus.enter_phone("abcd")
         contactus.enter_email("test@test.com")
         contactus.enter_message("I like pineapples")
         contactus.click_submit_button()
         message = contactus.verify_error_message()
         self.assertEqual(message, "Validation errors occurred. Please confirm the fields and try again.")

     # empty email scenario
     def test_05_empty_email(self):
        driver = self.driver
        driver.get("https://coreplus.com.au/contact/")
        contactus = ContactusPage(driver)
        contactus.enter_name("QATest")
        contactus.enter_phone("0464935234")
        # contactus.enter_email("test@test.com")
        contactus.enter_message("I like pineapples")
        contactus.click_submit_button()
        message = contactus.verify_error_message()
        self.assertEqual(message, "Validation errors occurred. Please confirm the fields and try again.")

     # invalid email senario
     def test_06_invalid_email(self):
        driver = self.driver
        driver.get("https://coreplus.com.au/contact/")
        contactus = ContactusPage(driver)
        contactus.enter_name("QATest")
        contactus.enter_phone("0464935234")
        contactus.enter_email("testtest.com")
        contactus.enter_message("I like pineapples")
        contactus.click_submit_button()
        msg = contactus.verify_email_error_message()
        self.assertEqual(msg, "Email address seems invalid.")

     # asserting title
     def test_07_assert_title(self):
        driver = self.driver
        driver.get("https://coreplus.com.au/contact/")
        contactus = ContactusPage(driver)
        title=driver.title
        print(title)
        assert "coreplus" in title

     # check element present in page
     def test_08_check_element_present(self):
         driver = self.driver
         driver.get("https://coreplus.com.au/contact/")
         contactus =ContactusPage(driver)
         msg = contactus.verify_link_text_message()
         self.assertEqual(msg,"help.coreplus.com")
         # assert "help.coreplus.com" in msg




    #tear down for class
     @classmethod
     def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

#main method to run unittest
if __name__ == '__main__':
     unittest.main(testRunner= HtmlTestRunner.HTMLTestRunner(output='C:/Users/User/PycharmProjects/CoreplusSeleniumPOMProject/Reports'))