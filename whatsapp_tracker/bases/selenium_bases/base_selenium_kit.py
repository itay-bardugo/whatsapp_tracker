from abc import ABCMeta

from whatsapp_tracker.data_structures.setup_data_structures import SetupSeleniumDataStructure


class BaseSeleniumKit(metaclass=ABCMeta):
    def __init__(self, selenium_kit: SetupSeleniumDataStructure):
        self.selenium_kit = selenium_kit
