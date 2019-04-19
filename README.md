# project_fourier
Raw Materials and Work in Progress for FFT Fourier Transform Spectral Analysis of Audio / VIbration on Raspberry PI


# Section 0 - GENERATE TEST Signal (WAV)
generate_test_signal.py (tested OK)	

![alt text](https://github.com/rustyoldrake/project_fourier/blob/master/img/%20generate_test_signal.png)

# Section 1 - ACQUIRE AND CLEAN/FILTER WAV 
- This will import WAV file, check OK, and clean up (e.g. low pass filter) if desired

## Source File for Filter Cleaner (before)
![alt text](https://github.com/rustyoldrake/project_fourier/blob/master/img/square_2000hz_3_seconds.PNG)

## After a low pass filter (starts to remove noise over about ~7KHZ) - (after)
![alt text](https://github.com/rustyoldrake/project_fourier/blob/master/img/square_2000hz_3_seconds_post_filter.PNG)

Warning - the current filter code seems to modify general amplitude (need to work on this)


# Section 2 - PROCESS FFT - GENERATE PNG PLOT
generate_FFT_plot_PNG.py  (tested OK)	

# SIN Waves are nice and smooth and simple - note only one signal in frequency domain at 2kz
![alt text](https://github.com/rustyoldrake/project_fourier/blob/master/img/sin_2000hz_3_seconds.PNG)

# SQUARE Waves are complicated - at 1st, 3rd and 5th harmonics (2000hz, 6000hz, and 10khz)
![alt text](https://github.com/rustyoldrake/project_fourier/blob/master/img/square_2000hz_3_seconds.PNG)


# Section 3 - PROCESS FFT - GENERATE BIN SCORES
generate_FFT_bin_score_text.py  (tested OK)	
![alt text]()
![alt text]()

# Section 4 - DELTA-DIFF - COMPARE TO PRIOR IF MATERIAL DIFFERENCE - TEST IF TRIGGER
- (TBD)
- This is LOGIC to determin if 'trigger' fires - e.g. if more than 20% change in any bin value 


# Section 5 - COMPOSE & TRANSMIT PAYLOAD
- (TBD)
- Send information 


  
  
  


# Appendix and Other Useful Links
SciPy and NumPy MANY tools for FFT and DFT:
SCIPY AND NUMPY Manuals (Beefy) -
https://docs.scipy.org/doc/scipy-0.13.0/scipy-ref.pdf
https://sites.engineering.ucsb.edu/~shell/che210d/numpy.pdf
https://docs.scipy.org/doc/numpy-1.11.0/numpy-user-1.11.0.pdf
