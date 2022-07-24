import rainbowhat as rh

display_temperature = False    
while True:
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
