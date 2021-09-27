from abc import ABCMeta

from whatsapp_tracker.bases.selenium_bases.base_selenium_kit import BaseSeleniumKit
from whatsapp_tracker.mixins.seleniun_keyboard_press_mixin import SeleniumKeyBoardPressMixin


class BaseSeleniumKeyboard(BaseSeleniumKit, SeleniumKeyBoardPressMixin, metaclass=ABCMeta):
    ...
