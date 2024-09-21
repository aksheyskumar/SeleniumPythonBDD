import time

from behave import *

from features.pageObjects.CreateAccountPage import CreateAccountPage


@when(u'Click Create your Amazon Account button')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.click_create_your_amazon_account()


@when(u'Fill all the required fields')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.enter_your_name("Akshay")
    context.create_account.enter_mobile_number_email("0000000000")
    time.sleep(5)
    context.create_account.enter_password("Jango@123")
    context.create_account.reenter_password("Jango@123")


@when(u'Click Continue')
def step_impl(context):
    context.create_account.create_account_continue()
    time.sleep(5)


@then(u'User should be navigated to the Puzzle Page')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.creation_page_validation()


@when(u'Fill all the required fields except mobile number/email')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.enter_your_name("Akshay")
    context.create_account.enter_mobile_number_email("")
    time.sleep(5)
    context.create_account.enter_password("Jango@123")
    context.create_account.reenter_password("Jango@123")


@then(u'System should throw a warning "Enter your email address or mobile phone number"')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    assert context.create_account.empty_phonenumber_warning_m()


@when(u'Fill all the required fields except Re-enterpassword')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.enter_your_name("Akshay")
    context.create_account.enter_mobile_number_email("0000000000")
    time.sleep(5)
    context.create_account.enter_password("Jango@123")
    context.create_account.reenter_password("")


@then(u'System should throw a warning "Type your password again"')
def step_impl(context):
    assert context.create_account.empty_reenter_password_m()


@when(u'Fill all the required fields with different password values')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.enter_your_name("Akshay")
    context.create_account.enter_mobile_number_email("0000000000")
    time.sleep(5)
    context.create_account.enter_password("Jango@123")
    context.create_account.reenter_password("Jando@123")


@then(u'System should throw a warning "Passwords do not match"')
def step_impl(context):
    assert context.create_account.empty_password_mismatch_m()


@then(u'System should throw  warning in all fields')
def step_impl(context):
   assert context.create_account.all_field_warning()


@when(u'Fill all the required fields except your name')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.enter_your_name("")
    context.create_account.enter_mobile_number_email("0000000000")
    time.sleep(5)
    context.create_account.enter_password("Jango@123")
    context.create_account.reenter_password("Jango@123")


@then(u'System should throw a warning "Enter your name"')
def step_impl(context):
    assert context.create_account.empty_name_warning_m()


@when(u'Fill all the required fields except password')
def step_impl(context):
    context.create_account = CreateAccountPage(context.driver)
    context.create_account.enter_your_name("Akshay")
    context.create_account.enter_mobile_number_email("0000000000")
    time.sleep(5)
    context.create_account.enter_password("")
    context.create_account.reenter_password("Jango@123")


@then(u'System should throw a warning "Enter a password"')
def step_impl(context):
    assert context.create_account.empty_password_warning_m()
