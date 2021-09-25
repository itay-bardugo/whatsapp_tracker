class SeleniumWindowMixin:
    @classmethod
    def maximize_window(cls, driver):
        driver.maximize_window()

    @classmethod
    def minimize_window(cls, driver):
        driver.minimize_window()
