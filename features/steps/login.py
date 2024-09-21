import time

from behave import *
from features.pageObjects.AmazonHome import AmazonHome

from features.pageObjects.LoginPage import LoginPage


@given(u'Navigate to the login URL')
def step_impl(context):
    context.home_page = AmazonHome(context.driver)
    context.home_page.click_on_signin_button()


@when(u'Enter the Phonenumber')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_phone_number("7768843261")


@when(u'Enter the invalid Phonenumber')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_phone_number("000000000000")


@when(u'Click the Continue button')
def step_impl(context):
    context.login_page.click_continue_button()
    time.sleep(5)


@when(u'Enter the Password')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_password("Nandanam@93")


@when(u'Click the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then(u' ')
def step_impl(context):
    assert context.home_page.display_home_text_fun()


@then(u'Warning message should popup - We cannot find an account with that mobile number')
def step_impl(context):
    assert context.login_page.warning_invalid_phone_number()


@when(u'Leave the phone number field empty')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_phone_number("")


@then(u'Warning message should popup - Enter your e-mail address or mobile phone number')
def step_impl(context):
    assert context.login_page.warning_without_phonenumber()
