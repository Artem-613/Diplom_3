import allure

from data import Urls
from locators import LoginPageLocators
from pages.constructor_page import ConstructorPage
from pages.profile_page import ProfilePage


class TestProfilePage:

    @allure.title('Проверяем переход по клику на «Личный кабинет»')
    @allure.description('Проверяем, что при клике на ссылку "Личный кабинет" происходит корректный переход на страницу профиля')
    def test_profile_link(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver = login_new_user
        # открываем Личный кабинет по ссылке с Главной страницы
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()

        # Проверяем что текущий url это url Личного кабинета
        assert driver.current_url == Urls.PROFILE_PAGE_URL


    @allure.title('Проверяем переход в раздел «История заказов»')
    @allure.description('Проверяем, что в личном кабинете доступен и работает переход в раздел истории заказов')
    def test_order_history_link(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver = login_new_user
        # открываем Личный кабинет по ссылке с Главной страницы
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        # кликаем ссылку История заказов
        profile_page.click_order_history_link()

        # Проверяем что раздел Истории заказов стал активным и текущий url это url Истории заказов
        assert profile_page.order_history_is_active()
        assert profile_page.get_current_url() == Urls.ORDER_HISTORY_URL


    @allure.title('Проверяем выход из аккаунта')
    @allure.description('Проверяем, что кнопка "Выход" в личном кабинете корректно выполняет выход из системы')
    def test_exit_button(self, get_browser, create_new_user_by_api, login_new_user):
        # регистрируем нового пользователя и открываем окно веб-браузер
        driver = login_new_user
        # открываем Личный кабинет по ссылке с Главной страницы
        profile_page = ProfilePage(driver)
        profile_page.open_profile_page()
        # кликаем кнопку Выход
        profile_page.click_exit_button()
        # ждем что произошел переход на страницу авторизации
        profile_page.wait_for_load_element(LoginPageLocators.LOGIN_BUTTON)

        # Проверяем что текущий url это url страницы авторизации
        assert profile_page.get_current_url() == Urls.LOGIN_PAGE_URL