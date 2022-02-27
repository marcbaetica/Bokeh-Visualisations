from data import OXYGEN, TEMPERATURE, LIGHTS, BATTERY
from time import sleep


while True:
    if LIGHTS:
        BATTERY -= 0.1
    print(OXYGEN, TEMPERATURE, LIGHTS, BATTERY)
    sleep(1)
