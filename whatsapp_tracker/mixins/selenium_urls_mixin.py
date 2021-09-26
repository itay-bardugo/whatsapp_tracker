class SeleniumUrlsMixin:
    @classmethod
    def open_url(cls, driver, url):
        return driver.get(url)
