import logging

from pandas import DataFrame

from whatsapp_tracker.mixins.path_mixin import PathMixin


class SampleSave(PathMixin):
    def __init__(self, path, samples: DataFrame):
        self.path = path
        self.samples = samples

    def save(self):
        self.samples.to_csv(path_or_buf=self.get_saving_path(self.path))
        logging.info('saved to : %s' % (self.path,))
