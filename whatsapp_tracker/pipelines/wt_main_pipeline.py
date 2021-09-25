from whatsapp_tracker.wt_selenium.selenium_setups.setup_selenium import SetupSelenium
from whatsapp_tracker.wt_selenium.selenium_shutdown import SeleniumShutDown
from whatsapp_tracker.selenium_whatsapp.selenium_whatsapp_login import SeleniumWhatsappLogin


class WTMainPipeline:
    def __init__(self, browser_path):
        self.browser_path = browser_path
        self.selenium_kit = None

    def setup_selenium(self):
        setup_selenium = SetupSelenium(
            browser_path=self.browser_path
        )
        self.selenium_kit = setup_selenium.setup()

    def login(self):
        whataspp_login = SeleniumWhatsappLogin(
            selenium_kit=self.selenium_kit
        )
        whataspp_login.start_login()

    def track(self):
        ...

    def shutdown_selenium(self):
        selenium_shutdown = SeleniumShutDown(selenium_kit=self.selenium_kit)
        selenium_shutdown.shutdown()

    def save_results(self):
        ...
