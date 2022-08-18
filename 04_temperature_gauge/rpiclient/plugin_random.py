import logging
import time
import colorsys
import random

logger = logging.getLogger('rpiclient.plugins')

class plugin_random():
    def __init__(self):
        logger.info("Initialising plugin_random")
        pass

    def retrieve_values(self):
        temperature = random.random() * 100.0
        pressure = random.random() * 1000.0
        return {
            "temperature": temperature,
            "pressure": pressure,
        }

