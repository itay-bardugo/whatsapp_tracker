from time import sleep

from selenium.common.exceptions import NoSuchElementException

from whatsapp_tracker.configs.selenium_wait_config import INIT_SLEEP, ITERATION_SLEEP


class SeleniumWaitMixin:
    @classmethod
    def wait_until_element_disappear(cls, driver_find_element):
        sleep(INIT_SLEEP)
        driver_find_element()
        while True:
            try:
                driver_find_element()
            except NoSuchElementException:
                break
            sleep(ITERATION_SLEEP)
