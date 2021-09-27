import logging
import sys

from whatsapp_tracker.pipelines.wt_main_pipeline import WTMainPipeline


class WhatsappTrackerMain:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.wt_pipeline = WTMainPipeline(**self.kwargs)

    def main(self):
        try:
            self.wt_pipeline.setup_selenium()
            self.wt_pipeline.login()
            self.wt_pipeline.track()
            self.wt_pipeline.shutdown_selenium()
        except Exception as e:
            logging.debug(e)
            self.wt_pipeline.shutdown_selenium()
            sys.exit(0)


