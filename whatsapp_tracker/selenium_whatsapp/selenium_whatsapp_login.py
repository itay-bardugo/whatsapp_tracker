from selenium.common.exceptions import NoSuchElementException

from whatsapp_tracker.bases.selenium_whatsapp_bases.base_selenium_whatsapp_login import BaseSeleniumWhatsappLogin


class SeleniumWhatsappLogin(BaseSeleniumWhatsappLogin):
    def login_implementation(self):
        try:
            self.select_qr_element(self.selenium_kit.driver)
            self.wait_until_element_disappear(lambda: self.select_qr_element(self.selenium_kit.driver))
        except NoSuchElementException:
            ...
