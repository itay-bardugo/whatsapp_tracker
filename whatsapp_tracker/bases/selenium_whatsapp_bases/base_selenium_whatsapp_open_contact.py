from abc import ABCMeta, abstractmethod

from whatsapp_tracker.bases.selenium_bases.base_selenium_keyboard import BaseSeleniumKeyboard
from whatsapp_tracker.data_structures.selenium_whatsapp_data_structures import SearchContactDataStructure


class BaseSeleniumWhatsappOpenContact(BaseSeleniumKeyboard, metaclass=ABCMeta):
    def __init__(self, search_meta: SearchContactDataStructure, **kwargs):
        self.search_meta = search_meta
        super(BaseSeleniumWhatsappOpenContact, self).__init__(**kwargs)

    @abstractmethod
    def open(self):
        ...
