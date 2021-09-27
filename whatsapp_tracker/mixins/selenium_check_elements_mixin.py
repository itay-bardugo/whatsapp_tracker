from selenium.common.exceptions import NoSuchElementException


class SeleniumCheckElementsMixin:
    @classmethod
    def check_element_exists(cls, driver, selector):
        try:
            selector(driver)
            return True
        except NoSuchElementException:
            return False
