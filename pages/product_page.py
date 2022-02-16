from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def compare_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        alert_name = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[0].text
        assert name == alert_name, "Имя добавленного товара не совпадает"

    def compare_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        alert_price = self.browser.find_elements(*ProductPageLocators.ALERT_LIST)[-1].text
        assert price == alert_price, "Цена добавленного товара не совпадает"

    def not_present_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Показывается сообщение об успехе"

    def disappeared_success_msg(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), \
            "Показывается сообщение об успехе"
