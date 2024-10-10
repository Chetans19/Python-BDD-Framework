from selenium.webdriver.common.by import By

from features.pages.SearchPage import SearchPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_xpath = "// a[text() = 'Login']"
    register_option_xpath = "//a[text() = 'Register']"
    search_box_field_name = "search"
    search_button_xpath = "//div[@id='search']//button"

    def click_my_account(self):
        self.driver.find_element(By.XPATH,self.my_account_option_xpath).click()

    def click_login_option(self):
        self.driver.find_element(By.XPATH, self.login_option_xpath).click()

    def click_register_option(self):
        self.driver.find_element(By.XPATH, self.register_option_xpath).click()

    def check_homepage_title(self, expected_title):
        return self.driver.title.__eq__(expected_title)

    def enter_in_search_box_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        # return SearchPage(self.driver)









