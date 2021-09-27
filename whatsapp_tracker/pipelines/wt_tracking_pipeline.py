from whatsapp_tracker.selenium_whatsapp.samples.sample_interval import SampleInterval
from whatsapp_tracker.selenium_whatsapp.selenium_whatsapp_open_contact import SeleniumWhatsappOpenContact
from whatsapp_tracker.selenium_whatsapp.selenium_whatsapp_sample import SeleniumWhatsappSample
from whatsapp_tracker.selenium_whatsapp.selenium_whatsapp_search_contact import SeleniumWhatsappSearchContact


class WTTrackingPipeline:
    def __init__(self, search_input, selenium_kit, save_path, resolution, minutes):
        self.search_input = search_input
        self.selenium_kit = selenium_kit
        self.save_path = save_path
        self.sample_resolution = resolution
        self.minutes = minutes
        self.search_meta = None

    def search_contact(self):
        search_contact = SeleniumWhatsappSearchContact(search_input=self.search_input, selenium_kit=self.selenium_kit)
        self.search_meta = search_contact.search()

    def open_contact_window(self):
        open_contact = SeleniumWhatsappOpenContact(
            search_meta=self.search_meta,
            selenium_kit=self.selenium_kit
        )
        open_contact.open()

    def track(self):
        sampler = SeleniumWhatsappSample(
            save_path=self.save_path,
            selenium_kit=self.selenium_kit
        )
        interval = SampleInterval(
            resolution=self.sample_resolution,
            minutes=self.minutes,
            pulse=sampler.sample
        )
        interval.run()
