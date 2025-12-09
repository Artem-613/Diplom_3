import allure

from data import Urls
from locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step('Открываем страницу профиля')
    def open_profile_page(self):
        """Открывает страницу профиля напрямую по URL"""
        self.open_page(Urls.PROFILE_PAGE_URL)
        self.wait_for_load_element(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('кликаем ссылку "История заказов"')
    def click_order_history_link(self):
        """Кликает на ссылку 'История заказов' в профиле"""
        self.click_element_by_locator(ProfilePageLocators.ORDER_HISTORY_LINK)

    @allure.step('Проверяем, что раздел История заказов становится активным')
    def order_history_is_active(self):
        """Проверяет, что раздел 'История заказов' активирован"""
        return self.wait_for_text_in_classname(
            ProfilePageLocators.ORDER_HISTORY_LINK,
            ProfilePageLocators.ORDER_HISTORY_IS_ACTIVE
        )

    @allure.step('кликаем кнопку "Выход"')
    def click_exit_button(self):
        """Кликает на кнопку 'Выход' в профиле"""
        self.click_element_by_locator(ProfilePageLocators.EXIT_BUTTON)

    # ========== Вспомогательные методы ==========
    @allure.step('Получаем список элементов с номерами заказов')
    def __get_order_history_elements(self):
        """Приватный метод: получает все элементы с номерами заказов"""
        return self.wait_for_load_all_elements(ProfilePageLocators.ORDER_HISTORY_ORDER_NUMBER)

    @allure.step('Получаем первый элемент с номером заказа')
    def __get_order_history_first_element(self):
        """Приватный метод: получает первый элемент с номером заказа"""
        return self.wait_for_load_element(ProfilePageLocators.ORDER_HISTORY_ORDER_NUMBER)

    # ========== Публичные методы для тестов ==========
    @allure.step('Получаем список номеров заказов пользователя')
    def get_order_history_list(self):
        """
        Получает список номеров заказов из истории заказов
        ВНИМАНИЕ: перед вызовом этого метода страница профиля должна быть уже открыта!
        """
        # Открываем раздел "История заказов"
        self.click_order_history_link()
        
        # Получаем все элементы с номерами заказов
        elements = self.__get_order_history_elements()
        
        # Извлекаем текст из каждого элемента
        order_list = []
        for item in elements:
            order_list.append(item.text)
        
        return order_list

    @allure.step('Получаем номер последнего заказа пользователя')
    def get_order_from_order_history(self):
        """
        Получает номер последнего заказа из истории заказов
        ВНИМАНИЕ: перед вызовом этого метода страница профиля должна быть уже открыта!
        """
        # Открываем раздел "История заказов"
        self.click_order_history_link()
        
        # Получаем первый (последний) элемент с номером заказа
        element = self.__get_order_history_first_element()
        
        # Возвращаем номер заказа
        return element.text
