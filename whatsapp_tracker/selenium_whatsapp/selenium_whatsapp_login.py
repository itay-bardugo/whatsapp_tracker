from selenium.common.exceptions import NoSuchElementException

from whatsapp_tracker.bases.base_selenium_whatsapp_login import BaseSeleniumWhatsappLogin


class SeleniumWhatsappLogin(BaseSeleniumWhatsappLogin):
    def login_implementation(self):
        try:
            self.selenium_kit.driver.find_element_by_tag_name('canvas')
            self.wait_until_element_disappear(lambda: self.selenium_kit.driver.find_element_by_tag_name('canvas'))
        except NoSuchElementException:
            ...
