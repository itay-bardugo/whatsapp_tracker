import os

from whatsapp_tracker.configs.paths_config import ROOT_PATH, CHROME_DATA_PATH


class SeleniumOptionMixin:
    @classmethod
    def _add_option(cls, options, option, value):
        options.add_argument("%s=%s" % (option, value))
        return options

    @classmethod
    def add_user_data_dir_option(cls, options):
        cls._add_option(options=options, option='--user-data-dir', value=CHROME_DATA_PATH)
        cls._add_option(options=options, option="disable-blink-features", value='AutomationControlled')
        return options
