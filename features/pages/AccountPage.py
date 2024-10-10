from selenium.webdriver.common.by import By


class AccountPage:

    def __init__(self, driver):
        self.driver = driver


    edit_account_info_text_xpath = "//a[text()='Edit your account information']"

    def display_status_of_edit_info(self):
        return self.driver.find_element(By.XPATH, self.edit_account_info_text_xpath).is_displayed()











