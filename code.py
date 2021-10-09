"""
CircuitPython single MP3 playback example for Raspberry Pi Pico.
Plays a single MP3 once.
"""
import board
import audiocore
import audiomp3
import audiopwmio
import time
from RandomLed import RandomLed
import random
import sys

ASSETS = 'assets/'
WORKING_MSG = ASSETS + "tos-computer-working.wav"

def WorkingMessage():  
    audio = audiopwmio.PWMAudioOut(board.GP27_A1)
    
    with open(WORKING_MSG, "rb") as data:
        wav = audiocore.WaveFile(data)
        time.sleep(0.5)
        audio.play(wav)
        
        while audio.playing:
            tcount = random.randint(0, 0xffff)
            RandomLed.rdisplay(count=tcount)
            time.sleep(0.05)
        audio.stop()
        audio.deinit()

    time.sleep(0.1)

if __name__ == '__main__':
    RandomLed()
    WorkingMessage()
    RandomLed.RandomLedClose()
    sys.exit()
