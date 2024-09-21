from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    phonenumber_field_xpath = "//input[@type='email']"
    password_field_xpath = "//input[@name='password']"
    continue_button_xpath = "//input[@type='submit']"
    login_button_xpath = "//input[@type='submit']"
    login_error_withoutphone = "Enter your email address or mobile phone number"
    login_error_invalidphone = "We cannot find an account with that mobile number"
    warning_message_invalidphone_xpath = "//span[contains(text(),'We cannot find an account with that mobile number')]"
    warning_message_withoutphone_xpath = "//div[contains(text(),'Enter your email address or mobile phone number')]"

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH, self.phonenumber_field_xpath).send_keys(phone_number)

    def click_continue_button(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def enter_password(self, pass_word):
        self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(pass_word)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def warning_invalid_phone_number(self):
        warning_message = self.driver.find_element(By.XPATH, self.warning_message_invalidphone_xpath).text
        return warning_message == self.login_error_invalidphone

    def warning_without_phonenumber(self):
        return self.driver.find_element(By.XPATH, self.warning_message_withoutphone_xpath).text.__eq__(
            self.login_error_withoutphone)
