# BS.py
'''This program will incorporate button and sound
Larry T. Priest  -   priestlt@protonmail.com
Sept. 28, 2021
'''
import time
import board
from working import WorkingMessage
import digitalio
from RandomLed import RandomLed
from phazer import PhazerFire


buttonpins = [16, 17, 21, 22]  # buttons 1 thru 4
buttons = []
LEDpins = [18, 19, 20]  # LED pins amber red green
amber = 0
red = 1
green = 2
LEDS = []
pressed = False

class ActOne():
    def __init__(self):
        subcommand = 'buttons.append(digitalio.DigitalInOut(board.GP'
        for pin in range(len(buttonpins)):
            fullcommand = subcommand + str(buttonpins[pin]) + '))'
            print(fullcommand)
            exec(fullcommand)
            buttons[pin].direction = digitalio.Direction.OUTPUT

        subcommand = 'LEDS.append(digitalio.DigitalInOut(board.GP'
        for pin in range(len(LEDpins)):
            fullcommand = subcommand + str(LEDpins[pin]) + '))'
            exec(fullcommand)
            LEDS[pin].direction = digitalio.Direction.OUTPUT
    def ButtonRun():
        while True:
            LEDS[green].value = True

            if buttons[0].value:
                print("You pressed the #1 button!")
                WorkingMessage()

            elif buttons[1].value:
                print("You pressed the #2 button!")
                LEDS[amber].value = True
                LEDS[green].value = False
                LEDS[red].value = True
                time.sleep(0.5)
                LEDS[amber].value = False
                time.sleep(0.25)
                LEDS[red].value = False
                
            elif buttons[2].value:
                print("You pressed the #3 button!")
                PhazerFire()
#                 LEDS[green].value = False
#                 LEDS[amber].value = True
#                 time.sleep(0.5)
#                 LEDS[amber].value = False
                
            elif buttons[3].value:
                print("You pressed the #4 button!")
                LEDS[green].value = True
                LEDS[amber].value = True
                LEDS[red].value = True
                time.sleep(0.5)
                LEDS[amber].value = False
                LEDS[red].value = False
                
            else:    
                LEDS[green].value = True
           
if __name__ == '__main__':
    RandomLed()
    ActOne()
    ActOne.ButtonRun()
    RandomLed.__exit__()
