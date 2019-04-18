# Step 2 - FILTER WAV FILE
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from scipy import *
from scipy import stats as stats
from scipy import signal as signal
from scipy import histogram
from scipy.io import wavfile
from scipy.fftpack import fft, fftfreq
from pydub import AudioSegment

# print parameters for numpy
np.set_printoptions(precision=8)
np.set_printoptions(threshold=256)

# IMPORT WAV to work with
#wav_filename = "square_5kz_5seconds.wav" # this is our synthetic test pattern
wav_filename = "square_20kz_1second.wav" # this is our synthetic test pattern
samplerate, wav_data = wavfile.read(wav_filename)
total_samples = len(wav_data)
limit = int((total_samples/2)-1)

## WAV File input and Summary
print("\n")
print(" --- Project Fourier - Edge Analytics --- ")
print("input - wav_filename", wav_filename)
print("samplerate", samplerate)
print("wav_data appended", wav_data)
print("total_samples from len(wav_data)",total_samples)
print("limit (samples/2)-1)",limit)
print("precision=5")
print("\n")

## FFT Fourier Basics - RAW
#fft_abs = abs(fft(wav_data)) # works / ABS
fft_abs = fft(wav_data)
#
# # works -
# data3 = signal.get_window("triang", 100)
# print("triang test:",data3,"\n")
# #
# data4 = signal.periodogram(wav_data)
# print("periodogram:",data4,"\n")

fs = 1 # fs : float, optional Sampling frequency of the x time series in units of Hz. Defaults to 1.0.

# works -
# f, Pxx_den = signal.periodogram(wav_data, fs)
# plt.semilogy(f, Pxx_den)
# plt.xlabel("frequency [Hz]")
# plt.ylabel("PSD [V**2/Hz]")
# plt.show()

# works
# f, Pxx_spec = signal.periodogram(wav_data, fs, "flattop", scaling="spectrum")
# plt.figure()
# plt.semilogy(f, np.sqrt(Pxx_spec))
# plt.xlabel("frequency [Hz]")
# plt.ylabel("Linear spectrum [V RMS]")
# plt.show()

# works sortof
# data5 = stats.relfreq(wav_data, numbins=128, defaultreallimits=None, weights=None)
# # data5 = stats.histogram2(wav_data,bins) # fail
# print("stats.relfreq:",data5,"\n")


# not really working - but no errors
#scipy.stats.histogram(a, numbins=10, defaultlimits=None, weights=None, printextras=False)
relfreqs, lowlim, binsize, extrapoints = stats.relfreq(wav_data, numbins=128)
# print("relfreqs:",relfreqs,"\n")
print("lowlim:",lowlim,"\n")
print("binsize:",binsize,"\n")
print("extrapoints:",extrapoints,"\n")

# signal.welch(x, fs=1.0, window=’hanning’, nperseg=256, noverlap=None, nfft=None, detrend=’
# constant’, return_onesided=True, scaling=’density’, axis=-1)
# Estimate power spectral density using Welch’s method
# data7 = signal.welch(wav_data, fs=samplerate, window="hanning", nperseg=256, noverlap=None, nfft=None, detrend="constant", return_onesided=True, scaling="density", axis=-1)

data7 = signal.welch(wav_data, fs=samplerate, window="hanning", nperseg=128, noverlap=None, nfft=None, detrend="constant", return_onesided=True, scaling="density", axis=-1)
# print("Data7:",data7)
print("array 0 - Frequency Bins", array2string(data7[0]))
print("array 1 - Signal Power by bin", array2string(data7[1]))


file = open("step3_spectralestimator_data7.txt","w")
file.write(str(data7))
file.close()



#data6 = stats.histogram(wav_data)
#print("stats.histogram:",data6,"\n")
#array([ 0.25, 0.5 , 0.75, 1. , 0.75, 0.5 , 0.25])
