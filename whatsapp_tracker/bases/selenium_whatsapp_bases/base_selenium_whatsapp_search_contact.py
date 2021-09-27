from abc import ABCMeta, abstractmethod

from whatsapp_tracker.bases.selenium_bases.base_selenium_kit import BaseSeleniumKit
from whatsapp_tracker.mixins.whatsapp_elements_selectors_mixin import WhatsappElementsSelectorsMixin


class BaseSeleniumWhatsappSearchContact(BaseSeleniumKit, WhatsappElementsSelectorsMixin, metaclass=ABCMeta):
    def __init__(self, search_input, **kwargs):
        self.search_input = search_input
        super(BaseSeleniumWhatsappSearchContact, self).__init__(**kwargs)

    @abstractmethod
    def search(self):
        ...
