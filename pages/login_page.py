from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()


    def should_be_login_url(self):
        fail = "Login url is not correct"
        assert "login" in self.browser.current_url, fail


    def should_be_login_form(self):
        fail = "Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), fail


    def should_be_register_form(self):
        fail = "Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), fail


    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        reg_email.send_keys(email)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        reg_pass1.send_keys(password)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        reg_pass2.send_keys(password)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_button.click()

