import time
from machine import Pin

gpio_pins = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(30) if i not in [24, 25]]

while True:
    for i, pin in enumerate(gpio_pins):
        pin_number = i
        if i >= 23:
            pin_number += 2
        if pin.value() == 1:
            print("GPIO", pin_number)
    time.sleep(0.5)
