import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPageLocators:
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.XPATH, "//div[@class='kc-feedback-text']")
    PASSWORD_RESET_LINK = (By.LINK_TEXT, "Забыли пароль?")
    REGISTER_LINK = (By.LINK_TEXT, "Зарегистрироваться")
    TABTEl=(By.ID,"t-btn-tab-phone")
    TABPOCHTA = (By.ID, "t-btn-tab-mail")
    TABLOGIN = (By.ID, "t-btn-tab-login")
    TABLS = (By.ID, "t-btn-tab-ls")

class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://b2c.passport.rt.ru/account_b2c/login"
        self.locators = LoginPageLocators

    def open(self):
        self.driver.get(self.url)

    def input_username(self, username):
        username_input = self.driver.find_element(*self.locators.USERNAME_INPUT)
        username_input.send_keys(username)

    def input_password(self, password):
        password_input = self.driver.find_element(*self.locators.PASSWORD_INPUT)
        password_input.send_keys(password)

    def submit_form(self):
        login_button = self.driver.find_element(*self.locators.LOGIN_BUTTON)
        login_button.click()

    def get_error_message(self):
        error_message = self.driver.find_element(*self.locators.ERROR_MESSAGE)
        return error_message.text

    def click_remember_me(self):
        remember_me = self.driver.find_element(*self.locators.REMEMBER_ME_CHECKBOX)
        remember_me.click()

    def click_reg_form(self):
            reg_form= self.driver.find_element(*self.locators.REGISTER_LINK)
            reg_form.click()

    def click_password_form(self):
        password_form = self.driver.find_element(*self.locators.PASSWORD_RESET_LINK)
        password_form.click()

    def is_remember_me_checked(self):
        remember_me = self.driver.find_element(*self.locators.REMEMBER_ME_CHECKBOX)
        return remember_me.is_selected()

    def is_username_field_populated(self):
        username_input = self.driver.find_element(*self.locators.USERNAME_INPUT)
        return username_input.get_attribute("value") != ""

    def get_password_input(self):
        password_input = self.driver.find_element(*self.locators.PASSWORD_INPUT)
        return password_input

    def get_login_button(self):
        login_button = self.driver.find_element(*self.locators.LOGIN_BUTTON)
        return login_button

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.submit_form()

    def is_logged_in(self):
        profile_link = self.driver.find_element(*self.locators.PROFILE_LINK)
        return profile_link.is_displayed()

    def is_username_input_field_visible(self):
        try:
            self.driver.find_element(*self.locators.USERNAME_INPUT)
            return True
        except:
            return False

    def is_form_displayed(self):
        form = self.driver.find_element(*self.locators.LOGIN_FORM)
        return form.is_displayed()

    def is_password_input_field_visible(self):
        password_input_field = self.driver.find_element(*self.locators.PASSWORD_INPUT)
        return password_input_field.is_displayed()

    def is_submit_button_visible(self):
        submit_button = self.driver.find_element(*self.locators.LOGIN_BUTTON)
        return submit_button.is_displayed()

    def is_username_input_field_enabled(self):
        username_input_field = self.driver.find_element(*self.locators.USERNAME_INPUT)
        return username_input_field.is_enabled()

    def is_password_input_field_enabled(self):
        password_input_field = self.driver.find_element(*self.locators.PASSWORD_INPUT)
        return password_input_field.is_enabled()

    def is_submit_button_enabled(self):
        submit_button = self.driver.find_element(*self.locators.LOGIN_BUTTON)
        return submit_button.is_enabled()

    def is_phonetab_enable(self):
        submit_button = self.driver.find_element(*self.locators.TABTEl)
        return submit_button.is_enabled()

    def is_mailtab_enable(self):
        submit_button = self.driver.find_element(*self.locators.TABPOCHTA)
        return submit_button.is_enabled()

    def is_logintab_enable(self):
        submit_button = self.driver.find_element(*self.locators.TABLOGIN)
        return submit_button.is_enabled()

    def is_tabls_enable(self):
        submit_button = self.driver.find_element(*self.locators.TABLS)
        return submit_button.is_enabled()

