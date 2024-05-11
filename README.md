﻿## Финальный проект 5 спринта

Папка tests содержит файлы с тестами, проверяющими функциональность сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/) 


### Описание проверок:

#### Тесты функциональности "Регистрация"
Файл test_registration.py
  Тесты:
  - успешной регистрации - test_registration_successful,
  - неудача при некорректном пароле - test_registration_invalid_password_error.

#### Тесты функциональности "Вход"
Файл test_authoriztion.py
  Тесты:
  - входа по кнопке «Войти в аккаунт» на главной - test_authorization_via_sign_in_account_button,
  - входа через кнопку «Личный кабинет» - test_authorization_via_account_button,
  - входа через кнопку в форме регистрации - test_authorization_via_sign_in_register_button,
  - входа через кнопку в форме восстановления пароля - test_authorization_via_sign_in_forgot_password_button.

#### Тесты перехода в личный кабинет
  Файл test_personal_account.py
  - с главной страницы - test_access_to_profile_from_main,
  - из ленты заказов - test_access_to_profile_from_feed.

#### Тесты перехода в конструктор
  Файл test_link_to_constructor.py
  - по клику на кнопку «Конструктор» - test_click_from_profile_on_constructor,
  - по клику на логотип Stellar Burgers - test_click_from_profile_on_logo_burgers.

#### Тест выхода из аккаунта
  Файл test_sign_out.py

#### Тест перехода в разделы конструктора
  Файл test_constructor_sections.py
  Тесты переходов:
  - на закладку «Булки» - test_constructor_section_buns,
  - на закладку «Соусы» - test_constructor_section_sauces,
  - на закладку «Начинки» - test_constructor_section_fillings.





