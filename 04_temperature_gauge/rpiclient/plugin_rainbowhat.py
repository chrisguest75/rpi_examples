import logging
import rainbowhat as rh
import time
import colorsys

logger = logging.getLogger('rpiclient.plugins')

class plugin_rainbowhat():
    def __init__(self):
        logger.info("Initialising plugin_rainbowhat")
        rh.rainbow.clear()

    def retrieve_values(self):
        t = rh.weather.temperature()
        p = rh.weather.pressure()
        return {
            "temperature": t,
            "pressure": p,
        }

