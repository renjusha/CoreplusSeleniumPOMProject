class Locators():
    #contactUsPage locators to be reused in other Pages and Tests
    name_textbox_xpath = "//input[@name='your-name']"
    phone_textbox_xpath = "//input[@name='your-phone']"
    phone_textbox_name = "your-phone"
    email_textbox_xpath = "//input[@name='your-email']"
    message_textbox_name = "your-message"
    submit_button_xpath = "//input[@value='Submit']"
    verify_message_xpath= "//div[@class='wpcf7-response-output wpcf7-display-none wpcf7-mail-sent-ok']"
    verify__header_xpath = "//div[@class='navbar-header']//img[@class='retina-image']"
    verify_message_class_name = "wpcf7-mail-sent-ok"
    validation_error_msg_xpath = "//div[@class='wpcf7-response-output wpcf7-display-none wpcf7-validation-errors']"
    email_error_msg_xpath = "//span[@class='wpcf7-not-valid-tip']"
    verify_link_text_xpath ="//div[@class='true-wysiwyg-field entry-content']//a[contains(text(),'help.coreplus.com')]"