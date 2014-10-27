import RPi.GPIO as GPIO
import sys
import time

BLUE = 24
RED = 23
GREEN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

red_on = 1
green_on = 0
blue_on = 0

while 1:
    GPIO.output(RED, red_on)
    GPIO.output(GREEN, green_on)
    GPIO.output(BLUE, blue_on)
    if red_on:
        red_on = 0
        green_on = 1
        blue_on = 0
    elif green_on:
        blue_on = 1
        red_on = 0
        green_on = 0
    elif blue_on:
        red_on = 1
        green_on = 0
        blue_on = 0
    time.sleep(.5)