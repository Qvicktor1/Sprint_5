from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators


class TestPersonalAccount:

    def test_access_to_personal_account_from_main(self, driver, sign_in):
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PROFILE_URL_ACCOUNT))

    def test_access_to_personal_account_from_feed(self, driver, sign_in):
        driver.find_element(*PageLocators.FEED_BUTTON).click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.FEED_HEADER))
        driver.find_element(*PageLocators.ACCOUNT_BUTTON).click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located(PageLocators.PROFILE_URL_ACCOUNT))