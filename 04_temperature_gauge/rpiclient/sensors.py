import logging
import rainbowhat as rh
import time
import colorsys

logger = logging.getLogger('rpiclient.sensors')

class sensors():
    def __init__(self):
        rh.rainbow.clear()

    def retrieve_values(self):
        t = rh.weather.temperature()
        p = rh.weather.pressure()
        return {
            "temperature": t,
            "pressure": p,
        }

