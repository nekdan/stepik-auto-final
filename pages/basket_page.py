from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def product_in_basket(self):
        # поверяем что нет кнопки "Перейти к оформлению"
        assert self.is_not_element_present(*BasketPageLocators.CHECKOUT), \
            "В корзине есть товар"

    def empty_basket_msg(self):
        # проверяем, что есть ссылка "Продолжить покупки" и сообщение о пустой корзине
        first_link = self.browser.find_element(*BasketPageLocators.FIRST_LINK)
        get_link = first_link.get_attribute('href')
        assert get_link in self.browser.current_url, \
            "Нет сообщения о пустой корзине"
