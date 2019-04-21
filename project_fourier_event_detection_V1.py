# #  Project Fourier # Test SCript (work in progress)
# #  TO be run on RAspberry PI with USB Microphone
#
#
print("Importing matplotlib") # doing this to test load times
import matplotlib
#matplotlib.use('TkAgg')
#import matplotlib.pyplot as plt
#
print("Importing numpy") # doing this to test load times
import numpy as np

print("Importing scipy") # doing this to test load times
from scipy import signal
from scipy.io import wavfile
# from scipy.fftpack import fft, fftfreq
# from pydub import AudioSegment
#
# import re # for passing filename from command line
#import sys # for passing filename from command line
import os # for using Raspi command line
import time

# # print parameters for numpy
np.set_printoptions(precision=5)
np.set_printoptions(threshold=256)
np.set_printoptions(formatter={'float_kind':'{:f}'.format})

wav_raw_input = 'wav_raw_input.wav'
wav_filtered_output = 'wav_filtered_output.wav'
index = 1  # lets count how many tests run, and use to remember "prior"
duration = 5 # time that it samples for (Seconds)

# These are variables that store the PRIOR SAMPLE - we use them to COMPARE
prior_frequency_bin_1 = 999
prior_frequency_signal_1 = 0.99
prior_frequency_bin_2 = 2999
prior_frequency_signal_2 = 0.09
# We initialize here to nonsense numbers - so the first time through will trigger event

## LOOP BEGINS Here

count = 0
while (count < 9):
    count = count + 1

    # arecord, aplay - command-line sound recorder and player for ALSA soundcard driver.
    # aquire for duration sections (works)
    print("Next recording started.....")
    os.system('arecord -D plughw:1,0 -d '+ str(duration) + ' ' + wav_raw_input)
    print("Recording Stopped")

    os.system('clear')

    #IMPORT FILE
    samplerate, wav_data = wavfile.read(wav_raw_input)
    print(samplerate)
    total_samples = len(wav_raw_input)
    limit = int((total_samples/2)-1)

    print("Calculating Bin Scores")
    bin_scores = signal.welch(wav_data, fs=samplerate, window="hanning", nperseg=128, noverlap=None, nfft=None, detrend="constant", return_onesided=True, scaling="density", axis=-1)
    bin_scores = np.transpose(bin_scores)
    # # Save it as CSV file
    # print("\n This is the RAW output \n ")
    # print(bin_scores)
    np.savetxt((wav_raw_input[:-4]+".csv"), bin_scores, delimiter=",", fmt='%.3f')

    #print(bin_scores[:,1]) # column 1

    os.system('clear')
    print ('Project Fourier - Test # ' + str(count))

    print("\n Sort SIgnal strength - descending - TOP 5 \n ")
    bin_score_sorted = bin_scores[bin_scores[:,1].argsort()]
    bin_score_sorted[:] = bin_score_sorted[::-1] # descending
    print(bin_score_sorted[:5])
    print("\n")

    # BIN 1
    print("#1 Frequency & Signal Strength")
    print("PRIOR F1: " + str(prior_frequency_bin_1) )
    print("NEW F1: " + str(bin_score_sorted[0][0])) # column 1
    #TEST F1 Change
    if prior_frequency_bin_1 != bin_score_sorted[0][0]:
      print("Trigger - Material Change Detected - Frequency Bin")
    else:
      print("Status OK - Same Frequency Bin")

    print("PRIOR S1: " + str(prior_frequency_signal_1) )
    print("NEW S1: " + str(bin_score_sorted[0][1])) # column 1
    delta = (abs(prior_frequency_signal_1 - bin_score_sorted[0][1])/prior_frequency_signal_1)
    print("SIGNAL DELTA: " + str(round(delta,2)))

    if delta > 0.20:
      print("Trigger - Material Change Detected - Signal Level")
    else:
      print("Status OK - Same Signal Level")




    print("\n")

    # Bin2
    print("#2 Frequency & Signal Strength")
    print("PRIOR F2 " + str(prior_frequency_bin_2) )
    print("NEW F2: " + str(bin_score_sorted[1][0])) # column 1
    # TEST F2 Change
    if prior_frequency_bin_2 != bin_score_sorted[1][0]:
      print("Trigger - Material Change Detected - Frequency Bin")
    else:
      print("Status OK - Same Frequency Bin")

    print("PRIOR S2: " + str(prior_frequency_signal_2) )
    print("NEW S2: " + str(bin_score_sorted[1][1])) # column 1
    delta = (abs(prior_frequency_signal_2 - bin_score_sorted[1][1])/prior_frequency_signal_2)
    print("SIGNAL DELTA: " + str(round(delta,2)))
    if delta > 0.20:
      print("Trigger - Material Change Detected - Signal Level")
    else:
      print("Status OK - Same Signal Level")


    print("\n")

    # now update Variables for next time / next test
    prior_frequency_bin_1 = bin_score_sorted[0][0] # [:1,column 0 is frequency]
    prior_frequency_signal_1 = bin_score_sorted[0][1] # [:1,column 1 is signal strength]
    prior_frequency_bin_2 = bin_score_sorted[1][0] # [:1,column 0 is frequency]
    prior_frequency_signal_2 = bin_score_sorted[1][1] # [:1,column 1 is signal strength]

    # Playback with Aplay - ORIGINAL Recording (works) - #
    # os.system('aplay ' + wav_raw_input)

    time.sleep(duration) # pause for as long as sample time (50% duty cycle ish)
