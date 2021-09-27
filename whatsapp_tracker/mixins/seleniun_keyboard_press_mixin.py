from selenium.webdriver.common.keys import Keys


class SeleniumKeyBoardPressMixin:
    @classmethod
    def press_enter(cls, element):
        return element.send_keys(Keys.RETURN)
