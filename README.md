# Диплом_3
# Задание 3: UI-тесты для Stellar Burgers

## 📋 Описание проекта
Автоматизированные UI-тесты для веб-приложения Stellar Burgers. Тестирование пользовательского интерфейса в браузерах Chrome и Firefox с использованием паттерна Page Object.

---

### Установка зависимости
```bash
pip install -r requirements.txt
```

### Запуск тестов

```bash
# Все тесты с отчетом Allure
pytest --alluredir=allure-results -v

# Только тесты конструктора
pytest test_constructor_page.py -v

# Только тесты ленты заказов
pytest test_feed_page.py -v
```

### Генерация отчета 
```bash
allure serve allure-results
```

---

## Структура проекта
```
ui-tests/
├── 📂 pages/                    # Page Object классы
│   ├── base_page.py           # Базовый класс страницы
│   ├── constructor_page.py    # Страница конструктора
│   ├── feed_page.py           # Лента заказов
│   ├── login_page.py          # Страница входа
│   ├── profile_page.py        # Личный кабинет
│   ├── forgot_password_page.py # Восстановление пароля
│   └── reset_password_page.py  # Сброс пароля
│
├── 📂 tests/                   # Тестовые сценарии
│   ├── test_constructor_page.py # Тесты конструктора
│   ├── test_feed_page.py        # Тесты ленты заказов
│   ├── test_login_user.py       # Тесты авторизации
│   ├── test_profile_page.py     # Тесты профиля
│   └── test_forgot_password_page.py # Тесты восстановления пароля
|
|── 📂 halpers/
├   |── helpers_requests.py         # Хелпер для API
├   |── helpers_register_user.py    # Хелпер для регистрации
|
├── locators.py                # Локаторы
├── conftest.py                # Фикстуры pytest
├── data.py                    # Тестовые данные и URL
├── requirements.txt           # Зависимости Python
└── README.md                  # Документация
```

---

## Тестовые сценарии
 Конструктор бургера (test_constructor_page.py)

1. Переход по клику на "Конструктор"
2. Переход по клику на "Лента заказов"
3. Открытие модального окна с деталями ингредиента
4. Закрытие модального окна по крестику
5. Увеличение счетчика ингредиента при добавлении в заказ

 Лента заказов (test_feed_page.py)

1. Увеличение счетчика "Выполнено за всё время" при новом заказе
2. Увеличение счетчика "Выполнено за сегодня" при новом заказе
3. Номер заказа появляется в разделе "В работе" после оформления

 Личный кабинет (test_profile_page.py)

1. Переход в личный кабинет
2. Переход в историю заказов
3. Выход из аккаунта# Diplom_3
