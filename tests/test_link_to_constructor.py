from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators


class TestFromProfileToConstructor:

    def test_click_from_profile_on_constructor(self, driver, sign_in):
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PROFILE_URL_ACCOUNT))
        driver.find_element(*PageLocators.CONSTRUCTOR_BUTTON).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.COMPILE_BURGER_HEADER))

    def test_click_from_profile_on_logo_burgers(self, driver, sign_in):
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PROFILE_URL_ACCOUNT))
        driver.find_element(*PageLocators.LOGO_HEADER).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.COMPILE_BURGER_HEADER))