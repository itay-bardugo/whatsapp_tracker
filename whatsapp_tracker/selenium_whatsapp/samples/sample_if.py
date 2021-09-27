import numpy as np

from whatsapp_tracker.bases.samples.base_sample import BaseSample
from whatsapp_tracker.mixins.selenium_check_elements_mixin import SeleniumCheckElementsMixin


class SampleIf(BaseSample, SeleniumCheckElementsMixin):

    @classmethod
    def sample_if_element_exists(cls, driver, selector, metric, value):
        if cls.check_element_exists(driver, selector):
            return cls.do_sample(metric=metric, value=value)
        return cls.do_sample(metric=metric)

    @classmethod
    def sample_if_element_not_exists(cls, driver, selector, metric, value):
        sample = cls.sample_if_element_exists(driver=driver, selector=selector, metric=metric, value=value)
        if np.isnan(sample.value):
            return cls.do_sample(metric=metric, value=value)
        return sample
