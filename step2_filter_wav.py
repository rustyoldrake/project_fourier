# Step 2 - FILTER WAV FILE
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
from scipy import signal
from scipy.io import wavfile

# source ; https://python-forum.io/Thread-Frequency-Filter-for-wav-file-plotting-in-python
from scipy.fftpack import fft, fftfreq
from pydub import AudioSegment

wav_filename = "square.wav"
samplerate, data = wavfile.read(wav_filename)

total_samples = len(data)
limit = int((total_samples /2)-1)

fft_abs = abs(fft(data))
freqs = fftfreq(total_samples,1/samplerate)

# plot the frequencies
# plt.plot(freqs[:limit], fft_abs[:limit])
# plt.title("Frequency spectrum of %s" % wav_filename)
# plt.xlabel('frequency in Hz')
# plt.ylabel('amplitude')
# plt.show()

####### FFT PLOT - PNG File - works
plt.plot(freqs[:limit], fft_abs[:limit]) # comment out if you dont want both before and after to display
#plt.savefig('square_fft.png')


## LOW PASS BUTTERWORTH FILTER  - works
## https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.lfilter.html

# Create an order 3 lowpass butterworth filter
b, a = signal.butter(3, 0.05)

# REPEAT ABOVE ON FILTERED DATA
# Use filtfilt to apply the filter:
data_filtered = signal.filtfilt(b, a, data)
fft_abs_filtered = abs(fft(data_filtered))
freqs_filtered = fftfreq(total_samples,1/samplerate)
plt.plot(freqs_filtered[:limit], fft_abs_filtered[:limit])
plt.savefig('square_fft_filtered.png')
