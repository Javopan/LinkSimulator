from datetime import datetime, timedelta
from time import sleep
from link import Link
from rain import Rain

# we declare the world
class World(object):
    def __init__(self, duration, time_speed):
        """
        :param duration: int, time in days the emulation will run
        :param time_speed: int, how fast the time will run
        """
        self.sim_start = datetime.now()
        # how many days the world will run
        run_time = duration  # days
        # simulation finish
        self.sim_end = self.sim_start + timedelta(days=run_time)

        # time expansion multiplyer
        time_expansion = time_speed  # how fast a second will be (1 second = 15 seconds)
        self.time_increment = timedelta(seconds=1*time_expansion)  # time expansion * 1 second

        self.link = Link(4000, 16.5, 16.5, 50, 50, 84375, 74375, [0.0005, 0.0005])
        self.rain = Rain()

    def run(self):
        # simulation current time
        sim_current = self.sim_start

        time_check = timedelta(seconds=1)
        current_time = self.sim_start
        check_time = current_time + time_check
        print(f'Starting the world at: {self.sim_start} will run for {self.sim_end - self.sim_start}')

        while sim_current <= self.sim_end:
            current_time = datetime.now()  # delete
            self.rain.rain(sim_current)  # Calculate if it is going to rain
            # TODO remove the time check so that we only have the events
            if current_time >= check_time and self.rain.raining:  # rainning check
                print(f'ST: {sim_current}')  # delete
                print(f'Link RSSI: {self.link.rssi_a}')  # delete
                if self.rain.raining_end <= sim_current:  # checking if it will stop raining
                    self.rain.rain_stop()
                    print(f'Rain stopped')  # delete
                check_time = current_time + time_check  # delete
            # ----------------------------------------------------------------------
            sim_current += self.time_increment  # increments the simulation time
            sleep(1)  # sleep for 1 second
        print(f'Simulation stopped')


if __name__ == '__main__':
    world = World(3, 15 * 4 * 10)  # *4*60)  # 3 days, 1 minute = 15 minutes
    world.run()
