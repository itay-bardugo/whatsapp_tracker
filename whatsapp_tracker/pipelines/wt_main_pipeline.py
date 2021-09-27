from whatsapp_tracker.mains.whatsapp_tracking_main import WhatsappTrackingMain
from whatsapp_tracker.wt_selenium.selenium_setups.setup_selenium import SetupSelenium
from whatsapp_tracker.wt_selenium.selenium_shutdown import SeleniumShutDown
from whatsapp_tracker.selenium_whatsapp.selenium_whatsapp_login import SeleniumWhatsappLogin


class WTMainPipeline:
    def __init__(self, browser_path, search_input, save_path, resolution, minutes):
        self.browser_path = browser_path
        self.search_input = search_input
        self.save_path = save_path
        self.resolution = resolution
        self.minutes = minutes
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
        tracking_main = WhatsappTrackingMain(
            selenium_kit=self.selenium_kit,
            search_input=self.search_input,
            save_path=self.save_path,
            resolution=self.resolution,
            minutes=self.minutes
        )
        tracking_main.main()

    def shutdown_selenium(self):
        selenium_shutdown = SeleniumShutDown(selenium_kit=self.selenium_kit)
        selenium_shutdown.shutdown()

