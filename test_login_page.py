from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from pages.login_page import LoginPage
#проверка доступности страницы
def test_site_status_code():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert driver.current_url == login_page.url
    driver.quit()
#проверка редиректа страницы
def test_site_redirect():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert driver.current_url == login_page.url
    driver.quit()
#прверка перехода на новую старинцу привводе логина и пароля
def test_form_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("sashen-ka88@mail.ru")
    login_page.input_password("g9k-4i5-7FX-vMi")
    login_page.submit_form()
    assert driver.current_url != login_page.url
    driver.quit()
# проверка неверного ввода имени пользователя и получение сообщения об ошибке
def test_invalid_username_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("invalid_username")
    login_page.input_password("Gg9k-4i5-7FX-vMi")
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Неверный логин или пароль"
    driver.quit()
# проверка неверного ввода пароля пользователя и получение сообщения об ошибке
def test_invalid_password_input():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("sashen-ka88@mail.ru")
    login_page.input_password("invalid_password")
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Неверный логин или пароль"
    driver.quit()
#проверка отправки пустой формы
def test_empty_form_submission():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.submit_form()
    error_message = login_page.get_error_message()
    assert error_message == "Введите логин и пароль"
    driver.quit()
#проверка чекбокса запомнить мои данные
def test_remember_me_feature():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.input_username("test_user")
    login_page.input_password("test_password")
    login_page.click_remember_me()
    login_page.submit_form()
    login_page.open()
    assert login_page.is_username_field_populated() == True
    assert login_page.is_remember_me_checked() == True
    driver.quit()
#проверка отображения эелементов ввода формы аторизации логин  пароль и войти
def test_form_elements_enabling():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.is_username_input_field_enabled() == True
    assert login_page.is_password_input_field_enabled() == True
    assert login_page.is_submit_button_enabled() == True
    driver.quit()

# проверка отображения кнопок формы переключения типа авторизации
def test_form_tabs_enabling():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    assert login_page.is_mailtab_enable()== True
    assert login_page.is_logintab_enable() == True
    assert login_page.is_phonetab_enable()== True
    assert login_page.is_tabls_enable()==True
    driver.quit()

#проверка перехода на страницу восстановления пароля при клике на забыли пароль
def test_password_new():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_password_form()
    assert driver.current_url != login_page.url
    driver.quit()
# проверка перехода на форму регистрации при клике на зарегистрироваться
def test_form_reg():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.open()
    login_page.click_reg_form()
    assert driver.current_url != login_page.url
    driver.quit()