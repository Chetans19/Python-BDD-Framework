from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email_input_xpath = "//input[@name = 'email']"
    password_input_xpath = "//input[@name = 'password']"
    login_button_css_selector = "input[type='submit']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email(self,email_text):
        self.driver.find_element(By.XPATH, self.email_input_xpath).send_keys(email_text)

    def enter_password(self,password_text):
        self.driver.find_element(By.XPATH, self.password_input_xpath).send_keys(password_text)

    def click_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.login_button_css_selector).click()

    def display_status_of_warning_message(self, expected_warning_message):
        return self.driver.find_element(By.XPATH, self.warning_message_xpath).text.__contains__(expected_warning_message)







