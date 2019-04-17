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

####### square wave to A PLOT (NOTE X SCALE IS GOOFY HERE - ILLUSTRATIVE ONLY) - works*
plt.plot(freqs[:limit], fft_abs[:limit])
plt.savefig('square_fft.png')
