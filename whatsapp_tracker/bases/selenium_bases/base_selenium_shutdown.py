from abc import ABCMeta, abstractmethod

from whatsapp_tracker.bases.selenium_bases.base_selenium_kit import BaseSeleniumKit


class BaseSeleniumShutDown(BaseSeleniumKit, metaclass=ABCMeta):
    @abstractmethod
    def shutdown(self):
        ...
