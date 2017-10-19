import sounddevice as sd
import numpy as np
import math 
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal as sg

class Transmissor:

	def __init__(self):
		self.fc = 3000	# frequencia de corte
		self.fs = 44100.0 #sample rate
		self.m1, self.sp1 = sf.read("audio/wubbalubdubdub.wav")
		self.m2, self.sp2 = sf.read("audio/what_u_know.wav")

	def calcFFT(self,signal, fs):
		from scipy.fftpack import fft
		from scipy import signal as window

		N  = len(signal)
		T  = 1/fs
		xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
		yf = fft(signal)

		return(xf, np.abs(yf[0:N//2]))

	def LPF(self,signal, cutoff_hz, fs):
		# https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
		nyq_rate = fs/2
		width = 5.0/nyq_rate
		ripple_db = 60.0 #dB
		N , beta = sg.kaiserord(ripple_db, width)
		taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
		return( sg.lfilter(taps, 1.0, signal))
	
	def carFrequencies(self, signal, f):
		t = np.linspace(0,len(signal)/self.fs,len(signal))
		y = np.sin(math.pi*2*t*f)
		return t,y
	
	# def plotGraph(self,x,y,title):
	# 	plt.plot(x,y)
	# 	plt.title(title)
	# 	plt.show()

	def main(self):
		y1 = self.m1[:,0]
		y2 = self.m2[:,0]
		f1_filtrada = self.LPF(y1,self.fc,self.fs) # f1 filtrada
		f2_filtrada = self.LPF(y2,self.fc,self.fs) # f2 filtrada
		t1,c1 = self.carFrequencies(f1_filtrada,9000) # Portadora 1
		t2,c2 = self.carFrequencies(f2_filtrada,15000) # Portadora 2
		fr1,fq1 = self.calcFFT(c1,self.fs) # Fourier portadora 1
		fr2,fq2 = self.calcFFT(c2,self.fs) # Fourier portadora 2
		fig2, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
		ax1.plot(fr1,fq1)
		ax2.plot(fr2,fq2)
		plt.show()

		
if __name__ == "__main__":
	transmissor = Transmissor()
	transmissor.main()