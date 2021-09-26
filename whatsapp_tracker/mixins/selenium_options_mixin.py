class SeleniumOptionMixin:
    @classmethod
    def _add_option(cls, options, option, value):
        options.add_argument("%s=%s" % (option, value))
        return options

    @classmethod
    def add_user_data_dir_option(cls, options, dir='chrome-data'):
        cls._add_option(options=options, option='--user-data-dir', value=dir)
        return options
