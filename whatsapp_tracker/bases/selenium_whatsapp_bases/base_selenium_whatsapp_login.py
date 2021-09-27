import time
from abc import abstractmethod, ABCMeta

from whatsapp_tracker.bases.selenium_bases.base_selenium_window import BaseSeleniumWindow
from whatsapp_tracker.configs.selenium_sleep_config import INIT_WHATSAPP_SLEEP
from whatsapp_tracker.configs.urls_config import WHATSAPP_HOME_PAGE
from whatsapp_tracker.mixins.selenium_wait_mixin import SeleniumWaitMixin
from whatsapp_tracker.mixins.whatsapp_elements_selectors_mixin import WhatsappElementsSelectorsMixin


class BaseSeleniumWhatsappLogin(BaseSeleniumWindow, SeleniumWaitMixin, WhatsappElementsSelectorsMixin,
                                metaclass=ABCMeta):
    def start_login(self):
        self.open_url(driver=self.selenium_kit.driver, url=WHATSAPP_HOME_PAGE)
        time.sleep(INIT_WHATSAPP_SLEEP)
        self.login_implementation()

    @abstractmethod
    def login_implementation(self):
        ...
