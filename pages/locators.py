from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRICE_TEXT = (By.CSS_SELECTOR, ".product_main .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ALERT_TEXT = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")


class BasketPageLocators():
    BASKET_TEXT = (By.CSS_SELECTOR, "#content_inner p")
