import RPi.GPIO as GPIO
from time import sleep as sl
import sys

class morse:
    def __init__(self):
        self.ausgang = 11

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ausgang, GPIO.OUT)

        self.buchstaben = {'a': {0: 0.25, 1: 0.75}, 'b': {0: 0.75, 1: 0.25, 2: 0.25, 3: 0.25},
                           'c': {0: 0.75, 1: 0.25, 2: 0.75, 3: 0.25},
                           'd': {0: 0.75, 1: 0.25, 2: 0.25}, 'e': {0: 0.25}, 'f': {0: 0.25, 1: 0.25, 2: 0.75, 3: 0.25},
                           'g': {0: 0.75, 1: 0.75, 2: 0.25}, 'h': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25},
                           'i': {0: 0.25, 1: 0.25}, 'j': {0: 0.25, 1: 0.75, 2: 0.75, 3: 0.75},
                           'k': {0: 0.75, 1: 0.25, 2: 0.75}, 'l': {0: 0.25, 1: 0.75, 2: 0.25, 3: 0.25},
                           'm': {0: 0.75, 1: 0.75}, 'n': {0: 0.75, 1: 0.25},
                           'o': {0: 0.75, 1: 0.75, 3: 0.75}, 'p': {0: 0.25, 1: 0.75, 2: 0.75, 3: 0.25},
                           'q': {0: 0.75, 1: 0.75, 2: 0.25, 3: 0.75},
                           'r': {0: 0.25, 1: 0.75, 2: 0.25}, 's': {0: 0.25, 1: 0.25, 2: 0.25}, 't': {0: 0.75},
                           'u': {0: 0.25, 1: 0.25, 2: 0.75},
                           'v': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.75}, 'w': {0: 0.25, 1: 0.75, 2: 0.75},
                           'x': {0: 0.75, 1: 0.25, 2: 0.25, 3: 0.75},
                           'y': {0: 0.75, 1: 0.25, 2: 0.75, 3: 0.75}, 'z': {0: 0.75, 1: 0.75, 2: 0.25, 3: 0.25},
                           'A': {0: 0.25, 1: 0.75}, 'B': {0: 0.75, 1: 0.25, 2: 0.25, 3: 0.25},
                           'C': {0: 0.75, 1: 0.25, 2: 0.75, 3: 0.25},
                           'D': {0: 0.75, 1: 0.25, 2: 0.25}, 'E': {0: 0.25}, 'F': {0: 0.25, 1: 0.25, 2: 0.75, 3: 0.25},
                           'G': {0: 0.75, 1: 0.75, 2: 0.25},
                           'H': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25}, 'I': {0: 0.25, 1: 0.25},
                           'J': {0: 0.25, 1: 0.75, 2: 0.75, 3: 0.75},
                           'K': {0: 0.75, 1: 0.25, 2: 0.75}, 'L': {0: 0.25, 1: 0.75, 2: 0.25, 3: 0.25},
                           'M': {0: 0.75, 1: 0.75}, 'N': {0: 0.75, 1: 0.25},
                           'O': {0: 0.75, 1: 0.75, 3: 0.75}, 'P': {0: 0.25, 1: 0.75, 2: 0.75, 3: 0.25},
                           'Q': {0: 0.75, 1: 0.75, 2: 0.25, 3: 0.75},
                           'R': {0: 0.25, 1: 0.75, 2: 0.25}, 'S': {0: 0.25, 1: 0.25, 2: 0.25}, 'T': {0: 0.75},
                           'U': {0: 0.25, 1: 0.25, 2: 0.75},
                           'V': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.75}, 'W': {0: 0.25, 1: 0.75, 2: 0.75},
                           'X': {0: 0.75, 1: 0.25, 2: 0.25, 3: 0.75},
                           'Y': {0: 0.75, 1: 0.25, 2: 0.75, 3: 0.75}, 'Z': {0: 0.75, 1: 0.75, 2: 0.25, 3: 0.25},
                           '1': {0: 0.25, 1: 0.75, 2: 0.75, 3: 0.75, 4: 0.75},
                           '2': {0: 0.25, 1: 0.25, 2: 0.75, 3: 0.75, 4: 0.75},
                           '3': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.75, 4: 0.75},
                           '4': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25, 4: 0.75},
                           '5': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25},
                           '6': {0: 0.75, 1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25},
                           '7': {0: 0.75, 1: 0.75, 2: 0.25, 3: 0.25, 4: 0.25},
                           '8': {0: 0.75, 1: 0.75, 2: 0.75, 3: 0.25, 4: 0.25},
                           '9': {0: 0.75, 1: 0.75, 2: 0.75, 3: 0.75, 4: 0.25},
                           '0': {0: 0.75, 1: 0.75, 2: 0.75, 3: 0.75, 4: 0.75},
                           ':': {0: 0.75, 1: 0.75, 2: 0.75, 3: 0.25, 4: 0.25, 5: 0.25},
                           '-': {0: 0.75, 1: 0.25, 2: 0.25, 3: 0.25, 4: 0.25, 5: 0.75},
                           'ß': {0: 0.25, 1: 0.25, 2: 0.25, 3: 0.75, 4: 0.75, 5: 0.25, 6: 0.25}}

    def main(self):
        while True:
            GPIO.output(self.ausgang,1)
            sl(0.1)
            GPIO.output(self.ausgang,0)
            sl(0.1)

    def buchstabe(self,buchstabe):
        for i in self.buchstaben[buchstabe]:
            GPIO.output(self.ausgang,1)
            sl(self.buchstaben[buchstabe][i])
            GPIO.output(self.ausgang,0)
            sl(0.25)

if __name__ == '__main__':
    try:
        print('Hello')
        morse = morse()
        while True:
            zeichen = input('Zeichen: ')
            if zeichen == 'exit':
                GPIO.cleanup()
                print('Goodbye!')
                sys.exit(0)
            else:
                for buchstabe in zeichen:
                    if buchstabe == " ":
                        sl(1)
                    else:
                        print(buchstabe)
                        assert buchstabe in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                     'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                     'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', '-', 'ß']
                        morse.buchstabe(buchstabe)
    except KeyboardInterrupt:
        GPIO.cleanup()