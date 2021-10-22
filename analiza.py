import pyaudio
import wave
import sounddevice as sd
from scipy.io.wavfile import read
import numpy as np


def analize():
        
    sig_audio = read(r"C:\Users\Iulian\Desktop\ENEA\recorded.wav")
    # Extracting the length and the half-length of the signal to input to the foruier transform
    # extragerea  lungimii semnalului
    sig_length = len(sig_audio[1])
    #impartirea la doi aproximata (ex: 1.5 = 2.0)
    half_length = np.ceil((sig_length + 1) / 2.0).astype(np.int32)
    
    # se foloseste transformata fourie pentru transformarea semnalului in frecventa
    signal_freq = np.fft.fft(sig_audio[1])
    # Normalizarea domeniului de frecventa si ridicarea lui la patrat
    signal_freq = abs(signal_freq[0:half_length]) / sig_length
    signal_freq **= 2
    
    # extragerea semnalului in decibeli
    exp_signal = 20 * np.log10(signal_freq)
    
    f= open("raspuns.txt","w+")
    f.write(str(np.mean(exp_signal)))
    f.close()