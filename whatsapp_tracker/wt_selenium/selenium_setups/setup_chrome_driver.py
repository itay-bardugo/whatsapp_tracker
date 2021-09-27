import shutil

from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException
from selenium.webdriver.chrome.webdriver import WebDriver

from whatsapp_tracker.configs.paths_config import CHROME_DATA_PATH
from whatsapp_tracker.mixins.selenium_window_mixin import SeleniumWindowMixin
from whatsapp_tracker.wt_selenium.selenium_setups.setup_selenium_options import SetupSeleniumOptions


class SetupChromeDriver(SeleniumWindowMixin):
    def __init__(self, browser_path):
        self._setup_options = SetupSeleniumOptions()
        self.browser_path = browser_path

    def setup(self) -> WebDriver:
        try:
            driver = webdriver.Chrome(self.browser_path, options=self._setup_options.setup())
            self.maximize_window(driver=driver)
        except InvalidArgumentException:
            shutil.rmtree(CHROME_DATA_PATH)
            return self.setup()
        return driver
