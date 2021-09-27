from time import sleep

from whatsapp_tracker.bases.selenium_whatsapp_bases.base_selenium_whatsapp_open_contact import BaseSeleniumWhatsappOpenContact
from whatsapp_tracker.configs.selenium_sleep_config import AFTER_OPEN_CONTACT_WINDOW_SLEEP


class SeleniumWhatsappOpenContact(BaseSeleniumWhatsappOpenContact):
    def open(self):
        self.press_enter(self.search_meta.search_box)
        sleep(AFTER_OPEN_CONTACT_WINDOW_SLEEP)