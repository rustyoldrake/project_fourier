# Receives a WAV File, does FFT and generates a text summary of bins and scores

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
np.set_printoptions(formatter={'float_kind':'{:f}'.format})

# OUTPUT - Filename Prepare
bin_score_filename = (wav_filename[:-4]+".txt")
print(bin_score_filename)


# IMPORT FILE
samplerate, wav_data = wavfile.read(wav_filename)
total_samples = len(wav_data)
limit = int((total_samples/2)-1)

bin_scores = signal.welch(wav_data, fs=samplerate, window="hanning", nperseg=128, noverlap=None, nfft=None, detrend="constant", return_onesided=True, scaling="density", axis=-1)



# Save array as TXT file
file = open(bin_score_filename,"w")
file.write(str(bin_scores))
file.close()

# Save it as CSV file
np.savetxt((wav_filename[:-4]+".csv"), bin_scores, delimiter=",", fmt='%.4f')

## WAV File input and Summary
print("\n")
print(" --- Project Fourier - Edge Analytics --- ")
print("INPUT - wav_filename", wav_filename)
print("samplerate", samplerate)
print("total_samples from len(wav_data)",total_samples)
print("limit (samples/2)-1)",limit)
print("array 0 - Frequency Bins")
print(np.array2string(bin_scores[0]))
print("array 1 - Signal Power by bin")
print(np.array2string(bin_scores[1]))
print("\n")
print("OUTPUT - bin_score_filename_TXT", bin_score_filename)
print("OUTPUT - bin_score_CSV", (wav_filename[:-4]+".csv"))
print("\n")
