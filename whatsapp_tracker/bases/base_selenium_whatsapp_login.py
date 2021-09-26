from abc import abstractmethod, ABCMeta

from whatsapp_tracker.bases.base_selenium_window import BaseSeleniumWindow
from whatsapp_tracker.configs.urls_config import WHATSAPP_HOME_PAGE
from whatsapp_tracker.mixins.selenium_wait_mixin import SeleniumWaitMixin


class BaseSeleniumWhatsappLogin(BaseSeleniumWindow, SeleniumWaitMixin, metaclass=ABCMeta):
    def start_login(self):
        self.open_url(driver=self.selenium_kit.driver, url=WHATSAPP_HOME_PAGE)
        self.login_implementation()

    @abstractmethod
    def login_implementation(self):
        ...
