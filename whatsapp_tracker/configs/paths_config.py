import os

import whatsapp_tracker

ROOT_PATH = os.path.dirname(os.path.abspath(whatsapp_tracker.__file__))
CHROME_DATA_PATH = os.path.join(*[ROOT_PATH, 'chrome-data'])
SAMPLES_PATH = 'WTTracker.csv'
