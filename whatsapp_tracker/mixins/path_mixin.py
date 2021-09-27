import os

from whatsapp_tracker.configs.paths_config import SAMPLES_PATH


class PathMixin:
    @classmethod
    def get_saving_path(cls, path):
        return os.path.join(*[path, SAMPLES_PATH])