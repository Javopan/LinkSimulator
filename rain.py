import numpy as np
from datetime import datetime, timedelta


class Rain(object):
    def __init__(self):
        self.raining = False
        self.raining_end = None
        self.rain_rate_delta = 0
        self.rain_rate = 0

    def rain(self, event_time):
        rain_prob = np.random.uniform(0, 1)
        if rain_prob <= 0.03 and not self.raining:
            self.raining = True
            rain_rate = round(abs(np.random.normal(0, 30)), 2)
            self.rain_rate = rain_rate
            self.rain_rate_delta = rain_rate
            if rain_rate <= 11:
                self.raining_end = event_time + timedelta(hours=np.random.randint(1, 5))
            elif rain_rate <= 25:
                self.raining_end = event_time + timedelta(minutes=np.random.randint(30, 120))
            elif rain_rate <= 55:
                self.raining_end = event_time + timedelta(minutes=np.random.randint(10, 60))
            else:
                self.raining_end = event_time + timedelta(minutes=np.random.randint(1, 30))
            print(f'Rain started @ {rain_rate} mmr/h it will rain for {self.raining_end - event_time}, ST: {event_time}')
        elif self.raining:
            self.rain_rate_delta = round(abs(np.random.normal(self.rain_rate, 10)), 2)
            print(f'Changed rainrate to: {self.rain_rate_delta} mmr/h')

    def rain_stop(self):
        self.raining = False
        # random gas attenuation during day
        # random_gases = np.random.randint(0, 4)
        # random_rain_rate = round(abs(np.random.normal(0, 25)), 2)
        # rain_event = np.random.uniform(0, 1)  # rain 3% of time