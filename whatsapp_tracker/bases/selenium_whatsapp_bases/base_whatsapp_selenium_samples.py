from abc import ABCMeta

from whatsapp_tracker.bases.selenium_bases.base_selenium_kit import BaseSeleniumKit
from whatsapp_tracker.configs.samples_config import SAMPLE_STATUS_METRIC_NAME, SAMPLE_STATUS_TRUE_VALUE, \
    SAMPLE_NAME_METRIC_NAME
from whatsapp_tracker.mixins.whatsapp_elements_selectors_mixin import WhatsappElementsSelectorsMixin
from whatsapp_tracker.selenium_whatsapp.samples.sample_element import SampleElement
from whatsapp_tracker.selenium_whatsapp.samples.sample_if import SampleIf


class BaseSeleniumWhatsappSamples(BaseSeleniumKit, WhatsappElementsSelectorsMixin, metaclass=ABCMeta):

    def __init__(self, **kwargs):
        super(BaseSeleniumWhatsappSamples, self).__init__(**kwargs)

    def sample_status(self):
        return SampleIf.sample_if_element_exists(
            driver=self.selenium_kit.driver,
            selector=self.select_contact_status_element,
            metric=SAMPLE_STATUS_METRIC_NAME,
            value=SAMPLE_STATUS_TRUE_VALUE
        )

    def sample_name(self):
        return SampleElement.sample_element_value(
            driver=self.selenium_kit.driver,
            selector=self.select_contact_name_elemnt,
            metric=SAMPLE_NAME_METRIC_NAME,
        )
