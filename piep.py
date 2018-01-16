import RPi.GPIO as GPIO
from time import sleep
import sys

class Test:
    def __init__(self):
        self.pin = 11

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

    def anaus(self, an_aus):
        assert an_aus in [0,1]
        GPIO.output(self.pin, an_aus)

    def piep(self, f):
        for i in range(1000):
            self.anaus(1)
            sleep(f)
            self.anaus(0)
            sleep(f)


if __name__ == '__main__':
    try:
        t = Test()
        t.piep(0.0001)
        GPIO.cleanup()

    except KeyboardInterrupt:
        GPIO.cleanup()

    except AssertionError:
        GPIO.cleanup()