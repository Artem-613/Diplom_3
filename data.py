_browser = 'Chrome'
#_browser = 'Firefoxe'


# тестовые данные для функции восстановления пароля
class UserData:
    USER_EMAIL = 'ivanivanov@mail.ru'
    USER_PASSWORD = '123456'


class Urls:
    FORGOT_PASSWORD_PAGE_URL = 'https://stellarburgers.education-services.ru/forgot-password'
    LOGIN_PAGE_URL = 'https://stellarburgers.education-services.ru/login'
    RESET_PASSWORD_PAGE_URL = 'https://stellarburgers.education-services.ru/reset-password'
    PROFILE_PAGE_URL = 'https://stellarburgers.education-services.ru/account/profile'
    ORDER_HISTORY_URL = 'https://stellarburgers.education-services.ru/account/order-history'
    MAIN_PAGE_URL = 'https://stellarburgers.education-services.ru'  # ГЛАВНАЯ СТРАНИЦА
    FEED_PAGE_URL = 'https://stellarburgers.education-services.ru/feed'

class RESPONSE_KEYS:

    # поля в ответе API
    ACCESS_TOKEN    = 'accessToken'     # str: "Bearer ..."
    REFRESH_TOKEN   = 'refreshToken'    # str: ""

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'   # delete: headers
    TOKEN_KEY       = 'token'           # logout: body, ="refreshToken"
