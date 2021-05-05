'''semitones as the fundamental building blocks 
    pitches or frequencies that are called on by the script 
    - using while loops - USE BREAK to stop, continue to move on to next iteration.
    - if statements
    and simple math around semitones to perpetuate a song for x bars.
    '''

    # frequencies of sound as they are labeled for music.


from math import log2, pow

A4 = 440
C0 = A4*pow(2, -4.75)

name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def pitch(freq):
    h = round(12*log2(freq/C0))
    octave = h // 12
    n = h % 12
    return name[n] + str(octave)

pitch(16)






import winsound
import numpy as np
from numpy import random


def song(start, end):
    winsound.Beep(int(start), np.random(500, 1000)
    for note in [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]:
	    winsound.Beep(int(note+.5), 500)
    winsound.Beep(int(end), np.random(500, 1000))

song(349.23, 329.63)
