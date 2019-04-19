# Receives a WAV File, does FFT and generates a PNG Plot

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from scipy import signal
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
from pydub import AudioSegment

import re # for passing filename from command line
import sys # for passing filename from command line

# check if they passed WAV Filename.
if len(sys.argv) > 1:
    wav_filename = sys.argv[1]
else:
    print('Error. Please include .WAV file to process')
    sys.exit()

# print parameters for numpy
np.set_printoptions(precision=5)
np.set_printoptions(threshold=128)

# IMPORT WAV to work with
#wav_filename = "square_5kz_5seconds.wav" # this is our synthetic test pattern
#wav_filename = "square_1kz_1second.wav" # this is our synthetic test pattern

# IMPORT FILE
samplerate, wav_data = wavfile.read(wav_filename)
total_samples = len(wav_data)
limit = int((total_samples/2)-1)

## WAV File input and Summary
print("\n")
print(" --- Project Fourier - Edge Analytics --- ")
print("input - wav_filename", wav_filename)
print("samplerate", samplerate)
print("total_samples from len(wav_data)",total_samples)
print("limit (samples/2)-1)",limit)
print("\n")


## FFT - Fourier Transform Time
freqs = fftfreq(total_samples,1/samplerate)
fft_abs = abs(fft(wav_data)) # works / ABS
# FFT print("freqs",freqs)
# FFT print("length freqs", len(freqs))

# PLOTS - Filename Prepare
plot_filename = (wav_filename[:-4]+".PNG")
print(plot_filename)
# PLOTS - Plot!
plt.plot(freqs[:limit], fft_abs[:limit])
plt.savefig(plot_filename)
plt.close()
