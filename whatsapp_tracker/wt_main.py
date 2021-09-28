import logging
import os
import sys
from argparse import ArgumentParser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from whatsapp_tracker.configs.default_vars_config import DEFAULT_BROWSER_DRIVER_PATH, DEFAULT_SAMPLE_RESOLUTION, \
    DEFAULT_MINUTES
from whatsapp_tracker.mains.whatsapp_tracker_main import WhatsappTrackerMain

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    parser = ArgumentParser()
    parser.add_argument('--browser-path', default=DEFAULT_BROWSER_DRIVER_PATH, help='an absolute path for executable chromedriver')
    parser.add_argument('--contact', required=True, help='contact name for tracking ')
    parser.add_argument('--save-path', required=True, help='where to store the results')
    parser.add_argument('--minutes', default=DEFAULT_MINUTES, type=int, help='for how long you want to tracking your contact, in minutes')
    parser.add_argument('--resolution', default=DEFAULT_SAMPLE_RESOLUTION, type=int, help='represents the sampling resolution in seconds')

    args = parser.parse_args()

    wt_main = WhatsappTrackerMain(
        browser_path=args.browser_path,
        search_input=args.contact,
        save_path=args.save_path,
        resolution=args.resolution,
        minutes=args.minutes,
    )
    wt_main.main()
