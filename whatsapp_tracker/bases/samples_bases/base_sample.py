import logging
from abc import ABCMeta

import numpy as np
from pandas import Timestamp


class BaseSample(metaclass=ABCMeta):
    @classmethod
    def do_sample(cls, metric, value=np.nan):
        logging.info('sampling metric: "%s"' % (metric,))
        return np.array([metric, value, Timestamp.now()])
