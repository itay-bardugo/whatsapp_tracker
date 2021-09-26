from abc import ABCMeta

from whatsapp_tracker.bases.base_selenium_kit import BaseSeleniumKit
from whatsapp_tracker.mixins.selenium_urls_mixin import SeleniumUrlsMixin


class BaseSeleniumWindow(BaseSeleniumKit, SeleniumUrlsMixin, metaclass=ABCMeta):
    ...
