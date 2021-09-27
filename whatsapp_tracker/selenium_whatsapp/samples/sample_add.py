class SampleAdd:
    @classmethod
    def add_sample_value(cls, list_, value):
        return list_.append(value)

    @classmethod
    def add_metric_sample(cls, ordered_dict, metric, value=None):
        ordered_dict[metric] = value
        return ordered_dict

    @classmethod
    def add_timestamp_sample(cls, list_, timestamp):
        return list_.append(timestamp)
