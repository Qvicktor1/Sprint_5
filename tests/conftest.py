import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators
from data_for_tests import CommonData


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(CommonData.main_url)
    yield browser
    browser.quit()


@pytest.fixture
def sign_in(driver):
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EMAIL_INPUT_FIELD_AUTH))
    driver.find_element(*PageLocators.EMAIL_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_email)
    driver.find_element(*PageLocators.PASSWORD_INPUT_FIELD_AUTH).send_keys(CommonData.test_user_password)
    driver.find_element(*PageLocators.SIGN_IN_BUTTON_AUTH).click()