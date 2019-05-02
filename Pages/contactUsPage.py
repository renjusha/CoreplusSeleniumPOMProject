from Locators.locators import Locators

class ContactusPage():
    # initialization of contact us page with driver and other properties
    def __init__(self, driver):
        self.driver = driver
        self.driver.name_textbox_xpath = Locators.name_textbox_xpath
        self.driver.phone_textbox_xpath = Locators.phone_textbox_xpath
        self.driver.phone_textbox_name = Locators.phone_textbox_name
        self.driver.email_textbox_xpath = Locators.email_textbox_xpath
        self.driver.message_textbox_name = Locators.message_textbox_name
        self.driver.submit_button_xpath = Locators.submit_button_xpath
        self.driver.verify_success_message_xpath = Locators.verify_message_xpath
        self.driver.verify_error_validation_xpath = Locators.validation_error_msg_xpath
        self.driver.verify_email_error_xpath = Locators.email_error_msg_xpath
        self.driver.verify_link_text_msg_xpath = Locators.verify_link_text_xpath

    # method to enter name into name field
    def enter_name(self, username):
        self.driver.find_element_by_xpath(self.driver.name_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.driver.name_textbox_xpath).send_keys(username)

    # method to enter phone into phone field
    def enter_phone(self, phoneno):
        self.driver.find_element_by_name(self.driver.phone_textbox_name).clear()
        self.driver.find_element_by_name(self.driver.phone_textbox_name).send_keys(phoneno)

    # method to enter email into email field
    def enter_email(self, emailid):
        self.driver.find_element_by_xpath(self.driver.email_textbox_xpath).clear()
        self.driver.find_element_by_xpath(self.driver.email_textbox_xpath).send_keys(emailid)

    # method to enter message into message field
    def enter_message(self, yourmessage):
        self.driver.find_element_by_name(self.driver.message_textbox_name).clear()
        self.driver.find_element_by_name(self.driver.message_textbox_name).send_keys(yourmessage)

    # method to submit the form
    def click_submit_button(self):
        self.driver.find_element_by_xpath(self.driver.submit_button_xpath).click()

    # method to get the success message from the element
    def verify_success_message(self):
        msg=self.driver.find_element_by_xpath(self.driver.verify_success_message_xpath).text
        return msg

    # method to get header icon
    def verify_navi_header_icon(self):
        self.driver.find_element_by_xpath(self.driver.verify_navi_header_icon_xpath)

    # method to get error validations message from element
    def verify_error_message(self):
        msg = self.driver.find_element_by_xpath(self.driver.verify_error_validation_xpath).text
        return msg

    # method to get email specific error message on field error
    def verify_email_error_message(self):
        msg = self.driver.find_element_by_xpath(self.driver.verify_email_error_xpath).text
        return msg

    # method to get link description
    def verify_link_text_message(self):
        msg=self.driver.find_element_by_xpath(self.driver.verify_link_text_msg_xpath).text
        return msg
