from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigated to Login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_my_account()
    context.home_page.click_login_option()

@when(u'I enter valid email address and valid password into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("Shinchan@gmail.com")
    context.login_page.enter_password("12345")

@when(u'I click on Login button')
def step_impl(context):
    context.login_page.click_login_button()

@then(u'I should get logged in')
def step_impl(context):
    context.account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_info()

@when(u'I enter valid email address as "amotoorisampletwo@gmail.com" and valid password as "secondtwo" into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email address as "amotoorisampletwo@gmail.com" and valid password as "secondtwo" into the fields')


@when(u'I enter valid email address as "amotoorisamplethree@gmail.com" and valid password as "secondthree" into the fields')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter valid email address as "amotoorisamplethree@gmail.com" and valid password as "secondthree" into the fields')


@when(u'I enter invalid email and valid password say "12345" into the fields')
def step_impl(context):
    # time_stamp = datetime.now()
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("Shinchanxs@gmail.com")
    context.login_page.enter_password("12345")

@then(u'I should get a proper warning message')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    expected_warning_message = 'Warning: No match for E-Mail Address and/or Password.'
    assert context.login_page.display_status_of_warning_message(expected_warning_message)

@when(u'I enter valid email say "amotoriapril2023sample@gmail.com" and invalid password say "1234567890" into the fields')
def step_impl(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email("Shinchan@gmail.com")
    context.login_page.enter_password("12345678")


@when(u'I enter invalid email and invalid password say "1234567890" into the fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("Shinchan1234@gmail.com")
    context.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("12345678")


@when(u'I dont enter anything into email and password fields')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@name = 'email']").send_keys("")
    context.driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("")
