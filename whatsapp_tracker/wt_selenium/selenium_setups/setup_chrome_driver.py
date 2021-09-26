from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from whatsapp_tracker.configs.default_vars_config import DEFAULT_BROWSER_DRIVER_PATH
from whatsapp_tracker.mixins.selenium_window_mixin import SeleniumWindowMixin
from whatsapp_tracker.wt_selenium.selenium_setups.setup_selenium_options import SetupSeleniumOptions


class SetupChromeDriver(SeleniumWindowMixin):
    def __init__(self):
        self._setup_options = SetupSeleniumOptions()

    def setup(self) -> WebDriver:
        driver = webdriver.Chrome(DEFAULT_BROWSER_DRIVER_PATH, options=self._setup_options.setup())
        self.maximize_window(driver=driver)
        return driver