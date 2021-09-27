import logging
from argparse import ArgumentParser

from whatsapp_tracker.configs.default_vars_config import DEFAULT_BROWSER_DRIVER_PATH, DEFAULT_SAMPLE_RESOLUTION, \
    DEFAULT_MINUTES
from whatsapp_tracker.mains.whatsapp_tracker_main import WhatsappTrackerMain

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = ArgumentParser()
    parser.add_argument('--browser-path', default=DEFAULT_BROWSER_DRIVER_PATH)
    parser.add_argument('--contact', required=True)
    parser.add_argument('--save-path', required=True)
    parser.add_argument('--resolution', default=DEFAULT_SAMPLE_RESOLUTION, type=int)
    parser.add_argument('--minutes', default=DEFAULT_MINUTES, type=int)

    args = parser.parse_args()

    wt_main = WhatsappTrackerMain(
        browser_path=args.browser_path,
        search_input=args.contact,
        save_path=args.save_path,
        resolution=args.resolution,
        minutes=args.minutes,
    )
    wt_main.main()
