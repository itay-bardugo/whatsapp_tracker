from selenium.webdriver.chrome.options import Options

from whatsapp_tracker.mixins.selenium_options_mixin import SeleniumOptionMixin


class SetupSeleniumOptions(SeleniumOptionMixin):
    def __init__(self):
        self.options = Options()

    def setup(self):
        self.add_user_data_dir_option(options=self.options)

        return self.options
