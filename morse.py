import RPi.GPIO as GPIO
from time import sleep
import sys
from morselib import code, test

class Morsecode:
    def __init__(self):
        self.ausgang = 11

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ausgang, GPIO.OUT)

        self.dit = 0.06

    def test(self, range_i):
        for i in range(range_i):
            GPIO.output(self.ausgang,1)
            sleep(0.1)
            GPIO.output(self.ausgang,0)
            sleep(0.1)

    def ton_ausgabe(self, buchstabe):
        for i in code()[buchstabe]:
            GPIO.output(self.ausgang,1)
            sleep(code()[buchstabe][i]*self.dit)
            GPIO.output(self.ausgang,0)
            sleep(0.06)
        sleep(0.12)

    def encode(self):
            zeichen = ''
            zeichen = input('Zeichen: ')
            if zeichen == 'exit;' or zeichen == "EXIT;":
                GPIO.cleanup()
                print('Goodbye!')
                sys.exit(0)
            else:
                for buchstabe in zeichen:
                    if buchstabe == " ":
                        sleep(0.16)
                    else:
                        assert buchstabe in test()
                        print(buchstabe)
                        self.ton_ausgabe(buchstabe)
            self.encode()

if __name__ == '__main__':
    try:
        print('Hello')
        mc = Morsecode()
        mc.encode()

    except KeyboardInterrupt:
        GPIO.output(11,0)
        GPIO.cleanup()

    except AssertionError:
        print('Zeichen nicht verfügbar! Try again.')
        Morsecode().encode()