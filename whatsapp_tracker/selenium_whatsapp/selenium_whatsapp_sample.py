import numpy as np

from whatsapp_tracker.bases.selenium_whatsapp_bases.base_selenium_whatsapp_sampler import BaseSeleniumWhatsappSampler


class SeleniumWhatsappSample(BaseSeleniumWhatsappSampler):
    def sample(self):
        self.add_sample(np.array([
            self.sample_status(),
            self.sample_name()
        ]))
        self.save_samples()
