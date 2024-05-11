from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from locators import PageLocators


class TestConstructorSections:

    def test_constructor_section_buns(self, driver):
        element = driver.find_element(*PageLocators.FILLINGS_HEADER)
        driver.execute_script("arguments[0].scrollIntoView();", element)
        driver.find_element(*PageLocators.BUNS_SPAN).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PageLocators.BUNS_HEADER))

    def test_constructor_section_sauces(self, driver):
        driver.find_element(*PageLocators.SAUCES_SPAN).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PageLocators.SAUCES_HEADER))

    def test_constructor_section_fillings(self, driver):
        driver.find_element(*PageLocators.FILLINGS_SPAN).click()
        assert WebDriverWait(driver, 3).until(ec.visibility_of_element_located(PageLocators.FILLINGS_HEADER))
