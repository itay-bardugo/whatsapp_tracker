from time import sleep


class SampleInterval:
    def __init__(self, resolution, minutes, pulse):
        self.resolution = resolution
        self.minutes = minutes
        self.pulse = pulse

    def run(self):
        for _ in range(60 * self.minutes // self.resolution):
            self.pulse()
            sleep(self.resolution)
