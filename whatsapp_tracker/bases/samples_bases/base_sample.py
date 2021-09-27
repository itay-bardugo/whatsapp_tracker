from abc import ABCMeta

import numpy as np
from pandas import Timestamp

from whatsapp_tracker.data_structures.samples_data_structures import Sample


class BaseSample(metaclass=ABCMeta):
    @classmethod
    def do_sample(cls, metric, value=np.nan):
        return np.array([metric, value, Timestamp.now()])
