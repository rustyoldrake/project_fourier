# AUDIO TEST PATTERN This is a simple piece of Python that generates a SINE or square
# WAVEFORM - and then writes to a plot, or a WAV FILE
# Receives: sampleRate (Hz), frequency (Hz) and duration (Second)
# Produces: WAV File that can be played or analyzed as baseline

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from scipy import signal
from scipy.io import wavfile

import os

os.system('clear')

print ("\n")
frequency = int(input("Test Frequency? (HZ) e.g. '5000'  : "))
duration = int(input("Duration of Tone? (Seconds) e.g. '2' : "))

sampleRate = 22050
print ("Using default sampleRate of : ",sampleRate," - change in code if needed ")
# sampleRate = int(input("Sample Rate? (HZ) e.g. '22050'   : "))

shape = int(input("(1) for SIN Wave; (2) or any other key for SQUARE : "))
print ("\n")

t = np.linspace(0, duration, sampleRate * duration)  #


if (shape == 1):
    y = np.sin(frequency * 2 * np.pi * t)  #  Has frequency of 7kz
    # Filename
    filename = ("sin_" + str(frequency) + "hz_" + str(duration) + "_seconds.wav")
    wavfile.write(filename, sampleRate, y)

else:
    samples = sampleRate*duration  ## Samples per second, times number of seconds
    x = np.arange(samples)   ## X Axis for numpy signal generator

    t = np.linspace(0, 1, sampleRate)  #  Produces a 2 second Audio-File
    y = 100 * signal.square(2 *np.pi * frequency * x / sampleRate ) #  Has frequency of 7kz
    # Filename
    filename = ("square_" + str(frequency) + "hz_" + str(duration) + "_seconds.wav")
    wavfile.write(filename, sampleRate, y)

# Strong Finish
print (" FILENAME will be: " + filename)
os.system('afplay ' + filename)

print ("\n Here is list of WAV files in directory.  'afplay file.wav' to test \n")
os.system('ls *.wav')
print ("\n")
