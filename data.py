_browser = 'Chrome'
#_browser = 'Firefoxe'


# тестовые данные для функции восстановления пароля
class UserData:
    USER_EMAIL = 'ivanivanov@mail.ru'
    USER_PASSWORD = '123456'


from urls import (
    FORGOT_PASSWORD_PAGE_URL,
    LOGIN_PAGE_URL,
    RESET_PASSWORD_PAGE_URL,
    PROFILE_PAGE_URL,
    ORDER_HISTORY_URL,
    MAIN_PAGE_URL,
    FEED_PAGE_URL
)

class RESPONSE_KEYS:

    # поля в ответе API
    ACCESS_TOKEN    = 'accessToken'     # str: "Bearer ..."
    REFRESH_TOKEN   = 'refreshToken'    # str: ""

    # поля для отправки запроса к API
    AUTH_TOKEN_KEY  = 'Authorization'   # delete: headers
    TOKEN_KEY       = 'token'           # logout: body, ="refreshToken"
