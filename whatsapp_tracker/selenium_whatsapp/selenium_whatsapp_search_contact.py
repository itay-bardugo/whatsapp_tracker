from time import sleep

from whatsapp_tracker.bases.selenium_whatsapp_bases.base_selenium_whatsapp_search_contact import BaseSeleniumWhatsappSearchContact
from whatsapp_tracker.configs.selenium_sleep_config import BEFORE_SEARCH_SLEEP
from whatsapp_tracker.data_structures.selenium_whatsapp_data_structures import SearchContactDataStructure


class SeleniumWhatsappSearchContact(BaseSeleniumWhatsappSearchContact):
    def search(self):
        sleep(BEFORE_SEARCH_SLEEP)
        elem = self.select_search_box_element(self.selenium_kit.driver)
        elem.click()
        active_element = self.select_active_element(self.selenium_kit.driver)
        active_element.send_keys(self.search_input)

        return SearchContactDataStructure(
            search_box=active_element,
            search_input=self.search_input
        )
