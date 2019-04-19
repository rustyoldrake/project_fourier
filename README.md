# project_fourier
Raw Materials and Work in Progress for FFT Fourier Transform Spectral Analysis of Audio / VIbration on Raspberry PI


# Section 0 - GENERATE TEST Signal (WAV)
generate_test_signal.py (tested OK)	

https://github.com/rustyoldrake/project_fourier/blob/master/img/%20generate_test_signal.png

# Section 1 - ACQUIRE AND CLEAN/FILTER WAV 
- (TBD)
- This will import WAV file, check OK, and clean up (e.g. low pass filter) if desired

# Section 2 - PROCESS FFT - GENERATE PNG PLOT
generate_FFT_plot_PNG.py  (tested OK)	

# Section 3 - PROCESS FFT - GENERATE BIN SCORES
generate_FFT_bin_score_text.py  (tested OK)	

# Section 4 - DELTA-DIFF - COMPARE TO PRIOR IF MATERIAL DIFFERENCE - TEST IF TRIGGER
- (TBD)
- This is LOGIC to determin if 'trigger' fires - e.g. if more than 20% change in any bin value 

# Section 5 - COMPOSE & TRANSMIT PAYLOAD
- (TBD)
- Send information 


  
  
  
===
Appendix - Other ARticles

https://benchodroff.com/2017/02/18/using-a-raspberry-pi-with-a-microphone-to-hear-an-audio-alarm-using-fft-in-python/
benchodroff.com
Using a raspberry pi with a microphone to hear an audio alarm using FFT in python - benchodroff.com
If your smoke alarm or, in my case, water alarm goes off you want to know right away – even if you are currently half way across the world traveling in China. I run a fish tank. I take many precautions but you really can’t be too safe. I bought a set of Honeywell water


WARNING - THIS IS TERRIBLE HAMFISTY CODE - WORK IN PROGRESS (approach with care :)




=====

SciPy and NumPy MANY tools for FFT and DFT:
SCIPY AND NUMPY Manuals (Beefy) -
https://docs.scipy.org/doc/scipy-0.13.0/scipy-ref.pdf
https://sites.engineering.ucsb.edu/~shell/che210d/numpy.pdf
https://docs.scipy.org/doc/numpy-1.11.0/numpy-user-1.11.0.pdf
