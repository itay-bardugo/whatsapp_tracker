from argparse import ArgumentParser

from whatsapp_tracker.configs.default_vars_config import DEFAULT_BROWSER_DRIVER_PATH
from whatsapp_tracker.mains.wt_main import WTMain

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--browser-path', default=DEFAULT_BROWSER_DRIVER_PATH)

    args = parser.parse_args()

    wt_main = WTMain(
        browser_path=args.browser_path
    )
    wt_main.main()
