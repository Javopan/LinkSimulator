import numpy as np


class Link(object):
    def __init__(self, link_distance, tx_a, tx_b, ant_a, ant_b, freq_a, freq_b, other_losses=[]):
        """
        :param time_step:  how are we going to compress time
        :param link_distance: int, distance in meters
        :param tx_a: float, transmit power of radio A in dBm
        :param tx_b: float, transmit power of radio B in dBm
        :param ant_a: int, gain in dBi of antenna for radio A
        :param ant_b: int, gain in dBi of antenna for radio B
        :param freq_a: int, frequency of radio A in MHz
        :param freq_b: int, frequency of radio B in MHz
        :param other_losses:  list, other losses to the link that has not been accounted for
        :return: int, calculated rssi of the link in dB
        """
        # free space pathloss calculaton based on Mhz and meters
        fspl = 20 * np.log10(link_distance) + 20 * np.log10((freq_a + freq_b) / 2) - 27.55

        # rssi calculation simple formula
        self.rssi_a = round(tx_b + ant_a + ant_b - fspl - (other_losses[0] * link_distance))
        self.rssi_b = round(tx_a + ant_a + ant_b - fspl - (other_losses[1] * link_distance))

        # # random gas attenuation during day
        # random_gases = np.random.randint(0, 4)
        # random_rain_rate = round(abs(np.random.normal(0, 25)), 2)
        # rain_event = np.random.uniform(0, 1)  # rain 3% of time


if __name__ == '__main__':
    link = Link(4000, 16.5, 16.5, 50, 50, 84375, 74375, [0.0005, 0.0005])
