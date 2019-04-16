# AUDIO TEST PATTERN This is a simple piece of Python that generates a SINE or square
# WAVEFORM - and then writes to a plot, or a WAV FILE
# Receives: sampleRate (Hz), frequency (Hz) and length (Second)
# Produces: WAV File that can be played or analyzed as baseline

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from scipy import signal
from scipy.io import wavfile

# SINE WAVE SECTION A - works
# x = np.linspace(0, 2 * np.pi, 1024)
# sinewave = np.sin(x)
# plt.plot(sinewave)
# plt.show()

# SQUARE WAVE SECTION B - works
# t = np.linspace(0, 1, 500, endpoint=False)
# plt.plot(t, signal.square(2 * np.pi * 5 * t))
# plt.ylim(-2, 2) # Y vertical Axis limits
# plt.show()  # show on MAC


# WAV FILE - SECTION C - SINE WAVE OUTPUT - 5 SECONDS - works
# sampleRate = 44100
# frequency = 440
# length = 5
# t = np.linspace(0, length, sampleRate * length)  #  Produces a 5 second Audio-File
# y = np.sin(frequency * 2 * np.pi * t)  #  Has frequency of 440Hz
# wavfile.write('sine.wav', sampleRate, y)


# WAV FILE - SECTION D - SQUARE WAVE - works

# # 32000 Hz The Nyquist frequency of 16000 Hz is above the frequency limit of many medium quality sources, such as ferric cassette tape.
# # 22050 kHz (often lazily called "22 kHz") has been a reasonably popular sample rate for low bit rate MP3s such as 64 kbps in years past. Audio quality is significantly affected, with higher frequency content missing
sampleRate = 44100
frequency = 1000 #
length = 5 #

samples = sampleRate*length  ## Samples per second, times number of secdonds
x = np.arange(samples)   ## X Axis for numpy signal generator

####### square wave to WAV ########## - works
y = 100* signal.square(2 *np.pi * frequency * x / sampleRate ) #  scipy.signal.square(t, duty=0.5)[source]¶
wavfile.write('square.wav', sampleRate, y)  # play back on mac - afplay square.wav
# ' afplay square.wav '' to te  st


####### square wave to A PLOT (NOTE X SCALE IS GOOFY HERE - ILLUSTRATIVE ONLY) - works*
t = np.linspace(0, length, sampleRate * length)
plt.plot(t, signal.square(2 * np.pi * 5 * t))
# plt.show() # NOTE X SCALE IS GOOFY HERE - ILLUSTRATIVE ONLY
plt.savefig('square.png')
