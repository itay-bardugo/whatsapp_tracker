from whatsapp_tracker.pipelines.wt_tracking_pipeline import WTTrackingPipeline


class WhatsappTrackingMain:
    def __init__(self, **kwargs):
        self.tracking_pipeline = WTTrackingPipeline(**kwargs)

    def main(self):
        self.tracking_pipeline.search_contact()
        self.tracking_pipeline.open_contact_window()
        self.tracking_pipeline.track()
