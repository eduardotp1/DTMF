import sounddevice as sd
import numpy as np
import math 
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal as sg

class Receptor():
    def __init__(self):
        self.fs = 44100.0
        self.fc = 3500

    def record(self):
        audio = sd.rec(int(5 * self.fs),self.fs,channels=1)
        sd.wait()
        y = audio[:,0]
        return y

    def carFrequencies(self, signal, f):
        t = np.linspace(0,len(signal)/self.fs,len(signal))
        y = np.sin(math.pi*2*t*f)
        return t,y

    def calcFFT(self, signal):
        from scipy.fftpack import fft
        from scipy import signal as window

        N  = len(signal)
        T  = 1/self.fs
        xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
        yf = fft(signal)

        return(xf, np.abs(yf[0:N//2]))

    def LPF(self, signal, cutoff_hz, fs):
        #####################
        # Filtro
        #####################
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))

    def main(self):
        audio = self.record()
        freqaudiox, freqaudioy = self.calcFFT(audio)

        t1,c1 = self.carFrequencies(audio, 9000)
        t2,c2 = self.carFrequencies(audio, 17000)

        demoaudio1 = c1 * audio
        demoaudio2 = c2 * audio
        fdemoaudio1x, fdemoaudio1y = self.calcFFT(demoaudio1)
        fdemoaudio2x, fdemoaudio2y = self.calcFFT(demoaudio2)

        fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        ax1.plot(fdemoaudio1x,fdemoaudio1y)
        ax2.plot(fdemoaudio2x,fdemoaudio2y)
        plt.show()

        demoaudio1_filtrada = self.LPF(demoaudio1 ,self.fc, self.fs)
        demoaudio2_filtrada = self.LPF(demoaudio2 ,self.fc, self.fs)    

        # fig, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
        # ax1.plot(fdemoaudio1x,demoaudio1_filtrada)
        # ax2.plot(fdemoaudio2x,demoaudio2_filtrada)
        # plt.show()        

        # sd.play(demoaudio1,self.fs)
        # sd.wait()
        sd.play(demoaudio1_filtrada,self.fs)
        sd.wait()
        sd.play(demoaudio2_filtrada, self.fs)
        sd.wait()

if __name__ == "__main__":
	receptor = Receptor()
	receptor.main()
