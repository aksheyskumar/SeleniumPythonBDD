import time

from behave import *

from selenium.webdriver.common.by import By

from features.pageObjects.AmazonHome import AmazonHome


@given('Navigate to the application URL')
def step_impl(context):
    actual_title = "Amazon.co.uk: Low Prices in Electronics, Books, Sports Equipment & more"
    assert context.driver.title.__eq__(actual_title)


@when('Enter Valid product in the search box')
def step_impl(context):
    context.amazon_home = AmazonHome(context.driver)
    context.amazon_home.enter_product_search_box("iPhone 15 Pro (128 GB) - Black Titanium")


@when('Click search button')
def step_impl(context):
    context.amazon_home.click_search_button()
    time.sleep(10)


@then('Searched product should be available as results')
def step_impl(context):
    assert context.amazon_home.searched_product_validation()


@when('Enter invalid product in the search box')
def step_impl(context):
    context.amazon_home = AmazonHome(context.driver)
    context.amazon_home.enter_product_search_box('<span class="a-color-state a-text-bold">')


@then('Proper search message should be shown in search results')
def step_impl(context):
    assert context.amazon_home.invalid_product_validation()
