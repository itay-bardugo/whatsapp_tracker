from whatsapp_tracker.pipelines.wt_main_pipeline import WTMainPipeline


class WTMain:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.wt_pipeline = WTMainPipeline(**self.kwargs)

    def main(self):
        self.wt_pipeline.setup_selenium()
        self.wt_pipeline.login()
        self.wt_pipeline.track()
        self.wt_pipeline.shutdown_selenium()
        self.wt_pipeline.save_results()
