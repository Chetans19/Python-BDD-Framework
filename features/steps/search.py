from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'I got navigated to Home page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_homepage_title("Your Store")

@when(u'I enter valid product say "HP" into the Search box field')
def step_impl(context):
    context.home_page.enter_in_search_box_field("HP")


@when(u'I click on Search button')
def step_impl(context):
    context.home_page.click_on_search_button()

@then(u'Valid product should get displayed in Search results')
def step_impl(context):
    search_page = SearchPage(context.driver)
    assert search_page.display_status_of_product()


@when(u'I enter invalid product say "Honda" into the Search box field')
def step_impl(context):
    context.home_page.enter_in_search_box_field("Honda")

@then(u'Proper message should be displayed in Search results')
def step_impl(context):
    search_page = SearchPage(context.driver)
    expected_text = "There is no product that matches the search criteria."
    assert search_page.display_status_of_message(expected_text)


@when(u'I dont enter anything into Search box field')
def step_impl(context):
    context.home_page.enter_in_search_box_field("")










