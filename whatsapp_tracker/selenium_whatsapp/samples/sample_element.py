from whatsapp_tracker.bases.samples.base_sample import BaseSample
from whatsapp_tracker.mixins.selenium_check_elements_mixin import SeleniumCheckElementsMixin


class SampleElement(BaseSample, SeleniumCheckElementsMixin):
    @classmethod
    def sample_element_value(cls, driver, selector, metric):
        if cls.check_element_exists(driver, selector):
            element = selector(driver)
            return cls.do_sample(metric=metric, value=element.text)
        return cls.do_sample(metric=metric)
