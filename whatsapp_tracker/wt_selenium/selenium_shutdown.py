from whatsapp_tracker.bases.base_selenium_shutdown import BaseSeleniumShutDown


class SeleniumShutDown(BaseSeleniumShutDown):

    def shutdown(self):
        self.selenium_kit.driver.close()
