from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Некорректный URL адресс"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Форма логина не найдена"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Форма регистрации не найдена"

    def register_new_user(self, email, password):
        reg_email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)
        first_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS1)
        first_password.send_keys(password)
        second_password = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASS2)
        second_password.send_keys(password)
        register = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        register.click()

