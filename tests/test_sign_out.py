from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators


def test_sign_out(driver, sign_in):
    driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.EXIT_BUTTON_ACCOUNT)).click()
    assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.SIGN_IN_BUTTON_AUTH))