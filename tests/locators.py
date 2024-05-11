from selenium.webdriver.common.by import By


class PageLocators:
    ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']")  # кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, ".// p[text() = 'Конструктор']")  # кнопка "Конструктор" в шапке
    FEED_BUTTON = (By.XPATH, ".//a[@href='/feed']")  # кнопка "Лента заказов"
    LOGO = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип в шапке
    SIGN_IN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # кнопка "Войти в аккаунт"
    COMPILE_BURGER_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")  # заголовок "Соберите бургер"
    PLACE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # кнопка "Оформить заказ"
    BUNS_SPAN = (By.XPATH, ".//span[text()='Булки']")  # закладка "Булки"
    BUNS_HEADER = (By.XPATH, ".//h2[text()='Булки']")  # заголовок секции "Булки"
    SAUCES_SPAN = (By.XPATH, ".//span[text()='Соусы']")  # закладка "Соусы"
    SAUCES_HEADER = (By.XPATH, ".//h2[text()='Соусы']")  # заголовок секции "Соусы"
    FILLINGS_SPAN = (By.XPATH, ".//span[text()='Начинки']")  # закладка "Начинки"
    FILLINGS_HEADER = (By.XPATH, ".//h2[text()='Начинки']")  # заголовок секции "Начинки"
    SIGN_IN_BUTTON_AUTH = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти"
    REGISTER_URL_AUTH = (By.XPATH, ".//a[@href='/register']")  # ссылка "Зарегистрироваться"
    EMAIL_INPUT_FIELD_AUTH = (
    By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Email']/../input")  # поле ввода "Email"
    PASSWORD_INPUT_FIELD_AUTH = (
    By.XPATH, ".//h2[text()='Вход']/..//label[text() = 'Пароль']/../input")  # поле ввода "Пароль"
    FORGOT_PASSWORD_BUTTON_AUTH = (By.XPATH, ".//a[text()='Восстановить пароль']")  # кнопка "Восстановить пароль"
    PROFILE_URL_ACCOUNT = (By.XPATH, ".//a[text()='Профиль']")  # ссылка "Профиль"
    EXIT_BUTTON_ACCOUNT = (By.XPATH, ".//button[text()='Выход']")  # кнопка "Выход"
    LOGO_HEADER = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # логотип "Stellar Burgers"
    REGISTER_BUTTON_REG = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    NAME_INPUT_FIELD_REG = (By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Имя']/../input")  # поле "Имя"
    EMAIL_INPUT_FIELD_REG = (
    By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Email']/../input")  # поле "Email"
    PASSWORD_INPUT_FIELD_REG = (
    By.XPATH, ".//h2[text()='Регистрация']/..//label[text() = 'Пароль']/../input")  # поле "Пароль"
    INCORRECT_PASSWORD_ERROR_REG = (By.XPATH, ".//p[text()='Некорректный пароль']")  # текст ошибки в форме регистрации
    SIGN_IN_BUTTON_REG = (
    By.XPATH, ".//h2[text()='Регистрация']/..//a[text()='Войти']")  # кнопка "Войти" в форме регистрации
    SIGN_IN_BUTTON_FORGOT_PASSWORD = (By.XPATH,
                                      ".//h2[text()='Восстановление пароля']/..//a[text()='Войти']")  # кнопка "Войти" в форме восстановления пароля
    FEED_HEADER = (By.XPATH, ".//h1[text()='Лента заказов']")  # заголовок "Лента заказов"
