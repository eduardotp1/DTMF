import sounddevice as sd
import numpy as np
import math 
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal as sg
import scipy.io.wavfile as swav

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

    def plotGraph(self,x,y,title):
    	plt.plot(x,y)
        plt.title(title)
        plt.show()

    def main(self):
        audio = self.record()
        freqaudiox, freqaudioy = self.calcFFT(audio)

        self.plotGraph(freqaudiox,freqaudioy,"Fourier Sinal Recebido")
        self.plotGraph(np.linspace(0, len(audio)/self.fs, len(audio)),audio,"Sinal Recebido no Tempo")

        t1,c1 = self.carFrequencies(audio, 5000)
        t2,c2 = self.carFrequencies(audio, 14000)

        demoaudio1 = c1 * audio
        demoaudio2 = c2 * audio
        fdemoaudio1x, fdemoaudio1y = self.calcFFT(demoaudio1)
        fdemoaudio2x, fdemoaudio2y = self.calcFFT(demoaudio2)

        self.plotGraph(fdemoaudio1x, fdemoaudio1y, "Fourier Audio 1 Recebido")
        self.plotGraph(fdemoaudio2x, fdemoaudio2y, "Fourier Audio 2 Recebido")

        demoaudio1_filtrada = self.LPF(demoaudio1 ,self.fc, self.fs)
        demoaudio2_filtrada = self.LPF(demoaudio2 ,self.fc, self.fs)   

        fdemoaudio1_filtradox, fdemoaudio1_filtradoy = self.calcFFT(demoaudio1_filtrada)
        fdemoaudio2_filtradox, fdemoaudio2_filtradoy = self.calcFFT(demoaudio2_filtrada)


        self.plotGraph(np.linspace(0,len(demoaudio1)/self.fs,len(demoaudio1)),demoaudio1, "Sinal no tempo do audio 1 recebido")
        self.plotGraph(np.linspace(0,len(demoaudio2)/self.fs,len(demoaudio2)),demoaudio2, "Sinal no tempo do audio 2 recebido")

        self.plotGraph(fdemoaudio1_filtradox, fdemoaudio1_filtradoy, "Fourier Audio 1 filtrado Recebido")
        self.plotGraph(fdemoaudio2_filtradox, fdemoaudio2_filtradoy, "Fourier Audio 2 filtrado Recebido")

        self.plotGraph(np.linspace(0,len(demoaudio1_filtrada)/self.fs,len(demoaudio1_filtrada)),demoaudio1_filtrada, "Sinal no tempo do audio 1 filtrado recebido")
        self.plotGraph(np.linspace(0,len(demoaudio2_filtrada)/self.fs,len(demoaudio2_filtrada)),demoaudio2_filtrada, "Sinal no tempo do audio 2 filtrado recebido")


        swav.write("audioreceive1.wav",self.fs,demoaudio1_filtrada)
        swav.write("audioreceive2.wav",self.fs,demoaudio2_filtrada)

        sd.play(demoaudio1_filtrada,self.fs)
        sd.wait()
        sd.play(demoaudio2_filtrada, self.fs)
        sd.wait()

if __name__ == "__main__":
	receptor = Receptor()
	receptor.main()
