import rainbowhat as rh

# import time

# while True:
#     for pixel in range(7):
#         rh.rainbow.clear()
#         rh.rainbow.set_pixel(pixel, 255, 0, 0)
#         rh.rainbow.show()
#         time.sleep(0.1)

import colorsys
import time

@rh.touch.A.press()
def touch_a(channel):
    print('Button A pressed')
    rh.lights.rgb(1, 0, 0)

@rh.touch.A.release()
def release_a(channel):
    print('Button A released')
    rh.lights.rgb(0, 0, 0)



rh.rainbow.clear()
rh.display.print_str('AHOY')
rh.display.show()
i = 0.0

song = [68, 68, 68, 69, 70, 70, 69, 70, 71, 72]
for note in song:
    rh.buzzer.midi_note(note, 0.5)
    time.sleep(1)

    
while True:
    t = rh.weather.temperature()
    p = rh.weather.pressure()
    print(t, p)
    rh.buzzer.midi_note(60, 1)
    for i in range(101):
        h = i / 100.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        rh.rainbow.set_all(r, g, b)
        rh.rainbow.show()
        time.sleep(0.02)
    rh.display.clear()
    rh.display.print_float(i)
    rh.display.show()
    i += 0.01        


