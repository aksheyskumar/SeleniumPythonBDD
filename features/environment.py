from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import Readconfigurations


def before_scenario(context, driver):
    browser_name = Readconfigurations.read_configuration("basic info", "browser")
    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(Readconfigurations.read_configuration("basic info", "url"))
    context.driver.find_element(By.XPATH, "//input[@name='accept']").click()


def after_scenario(context, driver):
    context.driver.quit()
