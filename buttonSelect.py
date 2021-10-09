"""
Button example for Pico. Prints button pressed state to serial consloe
REQUIRED HARDWARE:
* Button switch on pin GP13 ( I use GP20)
Adafruit Learn Guide:
Getting Started with Raspberry Pi Pico and CircuitPython
By Kattni Rembor
Restarted by Larry Priest Sept. 20, 2021

"""
import board
import time
import digitalio

buttonpins = [16, 17, 21, 22]  # buttons 1 thru 4
buttons = []
LEDpins = [18, 19, 20]  # LED pins amber red green
amber = 0
red = 1
green = 2
LEDS = []
pressed = False

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

while True:
    LEDS[green].value = True

    if buttons[0].value:
        print("You pressed the #1 button!")
        LEDS[red].value = True
        time.sleep(0.5)
        LEDS[green].value = False
        LEDS[red].value = True
        time.sleep(0.5)
        LEDS[amber].value = False
        time.sleep(0.25)
        LEDS[red].value = False
        
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
        LEDS[green].value = False
        LEDS[amber].value = True
        time.sleep(0.5)
        LEDS[amber].value = False
        
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
   
