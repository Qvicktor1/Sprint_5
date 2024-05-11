from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators
from data_for_tests import CommonData


class TestSignIn:

    def test_authorization_via_sign_in_account_button(self, driver):
        driver.find_element(*PageLocators.SIGN_IN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*PageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PLACE_ORDER))

    def test_authorization_via_account_button(self, driver):
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*PageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PLACE_ORDER))

    def test_authorization_via_sign_in_register_button(self, driver):
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.SIGN_IN_BUTTON_REG)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*PageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PLACE_ORDER))

    def test_authorization_via_sign_in_forgot_password_button(self, driver):
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.FORGOT_PASSWORD_BUTTON_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.SIGN_IN_BUTTON_FORGOT_PASSWORD)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
        driver.find_element(*PageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PLACE_ORDER))