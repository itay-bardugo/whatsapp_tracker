from whatsapp_tracker.configs.whatsapp_elements_config import QR_ELEMENT, SEARCH_INPUT_ELEMENT, ONLINE_ELEMENT, \
    CONTACT_NAME_ELEMENT


class WhatsappElementsSelectorsMixin:
    @classmethod
    def select_qr_element(cls, driver):
        return driver.find_element_by_tag_name(QR_ELEMENT)

    @classmethod
    def select_search_box_element(cls, driver):
        return driver.find_element_by_css_selector(SEARCH_INPUT_ELEMENT)

    @classmethod
    def select_active_element(cls, driver):
        return driver.switch_to.active_element

    @classmethod
    def select_contact_status_element(cls, driver):
        return driver.find_element_by_xpath(ONLINE_ELEMENT)

    @classmethod
    def select_contact_name_elemnt(cls, driver):
        return driver.find_element_by_xpath(CONTACT_NAME_ELEMENT)
