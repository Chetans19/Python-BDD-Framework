from selenium import webdriver
from utilities import ConfigReader

def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name.__eq__("Chrome"):
        context.driver = webdriver.Chrome()
    elif browser_name.__eq__("Firefox"):
        context.driver = webdriver.Firefox()
    elif browser_name.__eq__("Edge"):
        context.driver = webdriver.Edge()

    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info", "url"))

def after_scenario(context, driver):
    context.driver.quit()
