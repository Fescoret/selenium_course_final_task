from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()


    def price_is_correct(self):
        price_text = self.browser.find_element(*ProductPageLocators.PRICE_TEXT)
        price1 = price_text.text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE)
        price2 = basket_price.text
        assert price1 == price2, "Price is not correct"


    def product_name_is_correct(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        text1 = product_name.text
        alert_text = self.browser.find_element(*ProductPageLocators.ALERT_TEXT)
        text2 = alert_text.text
        assert text1 == text2, "Product name is not correct"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_TEXT), \
           "Success message is presented, but should not be"


    def success_message_should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_TEXT), \
           "Success message is not disappeared, but should be"


    def add_product_to_basket_without_solve(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

