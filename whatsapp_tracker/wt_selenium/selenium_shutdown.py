from whatsapp_tracker.bases.selenium_bases.base_selenium_shutdown import BaseSeleniumShutDown


class SeleniumShutDown(BaseSeleniumShutDown):

    def shutdown(self):
        self.selenium_kit.driver.quit()
