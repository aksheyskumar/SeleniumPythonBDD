from selenium.webdriver.common.by import By


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    create_your_amazon_account_xpath = "//a[@id='createAccountSubmit']"
    your_name_field_xpath = "//input[@id='ap_customer_name']"
    mobilenumber_email_xpath = "//input[@id='ap_email']"
    password_xpath = "//input[@id='ap_password']"
    reenter_password_xpath = "//input[@id='ap_password_check']"
    continue_button_xpath = "//input[@id='continue']"
    puzzle = "//h1[@id='aacb-captcha-header']"
    puzzle_value = "Solve this puzzle to protect your account                "
    empty_phonenumber_warning_xpath = "//div[contains(text(),'Enter your email address or mobile phone number')]"
    empty_phonenumber_warning = "Enter your email address or mobile phone number"
    empty_name_warning_xpath = "//div[contains(text(),'Enter your name')]"
    empty_name_warning = "Enter your name"
    empty_password_warning_xpath = "//div[contains(text(),'Enter a password')]"
    empty_password_warning = "Enter a password"
    password_mismatch_xpath = "//div[contains(text(),'Passwords do not match')]"
    password_mismatch = "Passwords do not match"
    empty_reenter_password_xpath = "//div[contains(text(),'Type your password again')]"
    empty_reenter_password = "Type your password again"

    def click_create_your_amazon_account(self):
        self.driver.find_element(By.XPATH, self.create_your_amazon_account_xpath).click()

    def enter_your_name(self, your_name):
        self.driver.find_element(By.XPATH, self.your_name_field_xpath).send_keys(your_name)

    def enter_mobile_number_email(self, mobile_number):
        self.driver.find_element(By.XPATH, self.mobilenumber_email_xpath).send_keys(mobile_number)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def reenter_password(self, password):
        self.driver.find_element(By.XPATH, self.reenter_password_xpath).send_keys(password)

    def create_account_continue(self):
        self.driver.find_element(By.XPATH, self.continue_button_xpath).click()

    def creation_page_validation(self):
        pass

    def empty_phonenumber_warning_m(self):
        warning_message = self.driver.find_element(By.XPATH, self.empty_phonenumber_warning_xpath).text
        return warning_message == self.empty_phonenumber_warning

    def empty_name_warning_m(self):
        warning_message = self.driver.find_element(By.XPATH, self.empty_name_warning_xpath).text
        return warning_message == self.empty_name_warning

    def empty_password_warning_m(self):
        warning_message = self.driver.find_element(By.XPATH, self.empty_password_warning_xpath).text
        return warning_message == self.empty_password_warning

    def empty_password_mismatch_m(self):
        warning_message = self.driver.find_element(By.XPATH, self.password_mismatch_xpath).text
        return warning_message == self.password_mismatch

    def empty_reenter_password_m(self):
        warning_message = self.driver.find_element(By.XPATH, self.empty_reenter_password_xpath).text
        return warning_message == self.empty_reenter_password

    def all_field_warning(self):
        if self.empty_phonenumber_warning_m() and self.empty_name_warning_m() and self.empty_password_warning_m():
            return True
        else:
            return False
