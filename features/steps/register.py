from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to Register Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.home_page.click_register_option()

@when(u'I enter below details into mandatory fields')
def step_impl(context):
    context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name("Shizuka")
    context.register_page.enter_last_name("Minamoto")
    context.register_page.enter_email("xy657z@gmail.com")
    context.register_page.enter_telephone("123455678")
    context.register_page.enter_password("12345678")
    context.register_page.enter_confirm_password("12345678")

@when(u'I select Privacy Policy option')
def step_impl(context):
    context.register_page.click_privacy_policy_checkbox()

@when(u'I click on Continue button')
def step_impl(context):
    context.register_page.click_continue_button()

@then(u'Account should get created')
def step_impl(context):
    account_success_page = AccountSuccessPage(context.driver)
    expected_text = "Your Account Has Been Created!"
    assert account_success_page.display_status_of_account_created(expected_text)


@when(u'I enter below details into all fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter below details into all fields')


@when(u'I enter details into all fields except email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter details into all fields except email field')


@when(u'I enter existing accounts email into email field')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter existing accounts email into email field')


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning message informing about duplicate account should be displayed')


@when(u'I dont enter anything into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I dont enter anything into the fields')


@then(u'Proper warning messages for every mandatory fields should be displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then Proper warning messages for every mandatory fields should be displayed')
