# https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/resources/morse_code.py

import RPi.GPIO as GPIO
import time
import sys

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
ledPin=7
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)


def dot():
  GPIO.output(ledPin,1)
  time.sleep(0.2)
  GPIO.output(ledPin,0)
  time.sleep(0.2)

def dash():
  GPIO.output(ledPin,1)
  time.sleep(0.5)
  GPIO.output(ledPin,0)
  time.sleep(0.2)

input = ''
while input != 'exit':
  input = raw_input('What would you like to send? ')
  for letter in input:
      for symbol in CODE[letter.upper()]:
        if symbol == '-':
          dash()
          sys.stdout.write(symbol)
        elif symbol == '.':
          dot()
          sys.stdout.write(symbol)
        else:
          time.sleep(0.5)
      time.sleep(0.5)