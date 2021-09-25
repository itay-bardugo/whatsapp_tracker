from argparse import ArgumentParser

from whatsapp_tracker.wt_pipelines.wt_main_pipeline import WTPipeline


class WTMain:
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.wt_pipeline = WTPipeline(**self.kwargs)

    def main(self):
        print('HELLO!')


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--chrome-path')

    args = parser.parse_args()

    wt_main = WTMain(
        chrome_path=args.chrome_path
    )
    wt_main.main()