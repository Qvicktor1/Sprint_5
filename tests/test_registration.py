from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators
from data_for_tests import CommonData


class TestRegistration:
    def test_registration_successful(self, driver):
        data = CommonData.reg_data()
        name = data['name']
        login = data['login']
        password = data['password']

        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.REGISTER_BUTTON_REG))
        driver.find_element(*PageLocators.NAME_INPUT_FIELD_REG).send_keys(name)
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_REG).send_keys(login)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_REG).send_keys(password)
        driver.find_element(*PageLocators.REGISTER_BUTTON_REG).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.ACCOUNT_BUTTON)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EMAIL_INPUT_FIELD_AUTH))
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(login)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(password)
        driver.find_element(*PageLocators.SIGN_IN_BUTTON_AUTH).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PLACE_ORDER))

    def test_registration_invalid_password_error(self, driver):
        data = CommonData.reg_data()
        name = data['name']
        login = data['login']

        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.REGISTER_URL_AUTH)).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.REGISTER_BUTTON_REG))
        driver.find_element(*PageLocators.NAME_INPUT_FIELD_REG).send_keys(name)
        driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_REG).send_keys(login)
        driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_REG).send_keys(CommonData.invalid_password)
        driver.find_element(*PageLocators.REGISTER_BUTTON_REG).click()
        assert driver.find_element(*PageLocators.INCORRECT_PASSWORD_ERROR_REG)
