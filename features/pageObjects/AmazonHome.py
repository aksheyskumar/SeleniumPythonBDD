from selenium.webdriver.common.by import By


class AmazonHome:
    def __init__(self, driver):
        self.driver = driver

    display_home_text = "Hello, Akshay"
    display_home_text_xpath = "//span[contains(text(),'Hello, Akshay')]"
    search_box = "//input[@placeholder='Search Amazon.co.uk']"
    search_button = "//input[@type='submit']"
    searched_product_xpath = "//span[contains(text(),'Apple iPhone 15 Pro (128 GB) - Black Titanium (Renewed)')]"
    signin_button = "//span[contains(text(),'Hello, sign in')]"
    display_text = "No results for"
    invalid_product_xpath = "//span[contains(text(),'No results for ')]"

    def display_home_text_fun(self):
        return self.driver.find_element(By.XPATH, self.display_home_text_xpath).text.__eq__(self.display_home_text)

    def enter_product_search_box(self, product_name):
        self.driver.find_element(By.XPATH, self.search_box).send_keys(product_name)

    def click_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button).click()

    def searched_product_validation(self):
        return self.driver.find_element(By.XPATH, self.searched_product_xpath).is_displayed()

    def click_on_signin_button(self):
        self.driver.find_element(By.XPATH, self.signin_button).click()

    def invalid_product_validation(self):
        warning_message = self.driver.find_element(By.XPATH, self.invalid_product_xpath).text
        return warning_message == self.display_text
