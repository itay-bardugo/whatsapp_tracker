import pickle
import time
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from whatsapp_tracker.configs.default_vars_config import DEFAULT_BROWSER_DRIVER_PATH
from whatsapp_tracker.configs.urls_config import WHATSAPP_HOME_PAGE

options = Options()

options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome(DEFAULT_BROWSER_DRIVER_PATH, options=options)
driver.maximize_window()
driver.get(WHATSAPP_HOME_PAGE)
try:
    try:
        sleep(2)
        driver.find_element_by_tag_name('canvas')
        while True:
            try:
                driver.find_element_by_tag_name('canvas')
            except NoSuchElementException:
                break
            sleep(1)

    except NoSuchElementException:
        ...
    sleep(3)
    elem = driver.find_element_by_css_selector('[data-testid="search"]')
    elem.click()
    sleep(3)
    elem = driver.switch_to.active_element
    elem.send_keys('xxx')
    sleep(3)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)

except Exception as e:
    print(e)

finally:
    driver.close()
