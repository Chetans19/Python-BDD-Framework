from selenium.webdriver.common.by import By


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver


    first_name_id = "input-firstname"
    last_name_id = "input-lastname"
    email_id = "input-email"
    telephone_id = "input-telephone"
    password_id = "input-password"
    confirm_password_id = "input-confirm"
    privacy_policy_checkbox_css_selector = "input[type = 'checkbox']"
    continue_button_css_selector = "input[type = 'submit']"

    def enter_first_name(self, first_name_text):
        self.driver.find_element(By.ID, self.first_name_id).send_keys(first_name_text)

    def enter_last_name(self, last_name_text):
        self.driver.find_element(By.ID, self.last_name_id).send_keys(last_name_text)

    def enter_email(self, email_text):
        self.driver.find_element(By.ID, self.email_id).send_keys(email_text)

    def enter_telephone(self, telephone_text):
        self.driver.find_element(By.ID, self.telephone_id).send_keys(telephone_text)

    def enter_password(self, password_text):
        self.driver.find_element(By.ID, self.password_id).send_keys(password_text)

    def enter_confirm_password(self, confirm_password_text):
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(confirm_password_text)

    def click_privacy_policy_checkbox(self):
        self.driver.find_element(By.CSS_SELECTOR, self.privacy_policy_checkbox_css_selector).click()

    def click_continue_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.continue_button_css_selector).click()














