import logging

logger = logging.getLogger('rpiclient.sensors')


#!/usr/bin/env python3
#
# TODO:
#
# Load config 
# Post values to the prometheus server 
# 

import rainbowhat as rh
import time
import colorsys

rh.rainbow.clear()

display_temperature = False    
while True:
    t = rh.weather.temperature()
    p = rh.weather.pressure()
    print(t, p)

    if display_temperature:
        segment_string = f"{t:.1f}"
    else:
        segment_string = f"{p:.0f}"

    rh.display.print_str(segment_string)
    rh.display.show()

    h = t
    r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 0.25)]
    pixels = int((7 / 100) * t)
    for pixel in range(pixels):
        rh.rainbow.set_pixel(6 - pixel, r, g, b)
    #rh.rainbow.set_all(r, g, b)
    rh.rainbow.show()

    time.sleep(3.00)
    display_temperature = not display_temperature
