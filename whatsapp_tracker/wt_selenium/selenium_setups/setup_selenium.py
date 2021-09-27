from whatsapp_tracker.data_structures.setup_data_structures import SetupSeleniumDataStructure
from whatsapp_tracker.wt_selenium.selenium_setups.setup_chrome_driver import SetupChromeDriver


class SetupSelenium:
    def __init__(self, browser_path):
        self.browser_path = browser_path

    def setup(self):
        chrome_setup = SetupChromeDriver()
        chrome = chrome_setup.setup()

        return SetupSeleniumDataStructure(
            driver=chrome
        )
