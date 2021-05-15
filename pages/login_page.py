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
