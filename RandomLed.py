# RandomLed.py
'''
random LED display a st of binary numbers
Written by Larry T, Priest (priestlt@protonmail.com)
august 28, 2021
asumes 16 LED's on pins GPIO0 - GPIO15
'''
import board
import digitalio
import time
import random

class RandomLed():
    delay = 0.25  # seconds
    count = 0xffff  # any interger (hex 'cause it makes sense)
    LEDbits = []
    TOTALBITS = 16
    
    def __init__(self, bits=16):
        subcommand = 'RandomLed.LEDbits.append(digitalio.DigitalInOut(board.GP'
        for i in range(RandomLed.TOTALBITS):
            fullcommand = subcommand + str(i) + '))'
            exec(fullcommand)
            RandomLed.LEDbits[i].direction = digitalio.Direction.OUTPUT

    def rdisplay(count=0x0ffff, *args, **kwargs):
        count = count
        counterBits = bin(count)[2:]  # leading zero + b chopped
        while len(counterBits) < 16:
            counterBits = '0' + counterBits
        byte_list = []
        for bit in iter(counterBits):
            byte_list.append(bit)
        bit_count = 0
        for i in iter(byte_list):
            if i == '1':
                RandomLed.LEDbits[bit_count].value = True
            else:
                RandomLed.LEDbits[bit_count].value = False
            bit_count += 1
        time.sleep(0.15)
        for i in range(len(RandomLed.LEDbits)):
            RandomLed.LEDbits[i].value = False
            
    def RandomLedClose():
        for i in range(len(RandomLed.LEDbits)):
            print('Closing output GP',i)
            RandomLed.LEDbits[i].deinit()
            
    def __exit__():
        for i in range(len(RandomLed.LEDbits)):
            print('Closing output GP',i)
            RandomLed.LEDbits[i].deinit()

if __name__ == '__main__':
    RandomLed()
    while True:
#     for i in range(10):
        tcount = random.randint(0, 0xffff)
        RandomLed.rdisplay(count=tcount)
    RandomLed.__exit__()