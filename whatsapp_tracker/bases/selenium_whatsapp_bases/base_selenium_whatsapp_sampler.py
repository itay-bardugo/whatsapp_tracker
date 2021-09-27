from abc import ABCMeta, abstractmethod
from collections import OrderedDict

import numpy as np
from pandas import DataFrame

from whatsapp_tracker.bases.selenium_whatsapp_bases.base_whatsapp_selenium_samples import BaseSeleniumWhatsappSamples
from whatsapp_tracker.data_structures.samples_data_structures import Sample
from whatsapp_tracker.selenium_whatsapp.samples.sample_add import SampleAdd
from whatsapp_tracker.selenium_whatsapp.samples.sample_save import SampleSave


class BaseSeleniumWhatsappSampler(BaseSeleniumWhatsappSamples, metaclass=ABCMeta):
    def __init__(self, save_path, **kwargs):
        self.save_path = save_path
        self.samples = []
        self.timestamps = []
        self.metrics = OrderedDict()
        super(BaseSeleniumWhatsappSampler, self).__init__(**kwargs)

    def add_sample(self, sample):
        SampleAdd.add_sample_value(self.samples, sample[:, 1])
        SampleAdd.add_timestamp_sample(self.timestamps, sample[0, 2])
        if not self.metrics:
            for metric in sample[:, 0]:
                SampleAdd.add_metric_sample(self.metrics, metric, None)

    def get_samples(self):
        return DataFrame(
            self.samples,
            columns=self.metrics,
            index=self.timestamps
        )

    def save_samples(self):
        sample_save = SampleSave(path=self.save_path, samples=self.get_samples())
        sample_save.save()

    @abstractmethod
    def sample(self):
        ...
