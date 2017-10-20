import sounddevice as sd
import numpy as np
import math 
import matplotlib.pyplot as plt
import soundfile as sf
from scipy import signal as sg

class Transmissor:

	def __init__(self):
		self.fc = 3500	# frequencia de corte
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
	
	def plotGraph(self,x,y,title):
		plt.plot(x,y)
		plt.title(title)
		plt.show()
	
	def sumLists(self,signal1,signal2):
		if len(signal1) > len(signal2):
			largest = signal1
			smallest = signal2
		else:
			largest = signal2
			smallest = signal1

		x = np.linspace(0, len(largest)/self.fs, len(largest))        
		dif = len(largest) - len(smallest)
		smallest = np.pad(smallest, (0, dif),'constant', constant_values=(0,0))
		return x,largest + smallest 

	def main(self):
		y1 = self.m1[:,0]
		y2 = self.m2[:,0]
		f1_filtrada = self.LPF(y1, self.fc, self.fs) # f1 filtrada
		f2_filtrada = self.LPF(y2, self.fc, self.fs) # f2 filtrada
		t1, c1 = self.carFrequencies(f1_filtrada, 9000) # Portadora 1
		t2, c2 = self.carFrequencies(f2_filtrada, 17000) # Portadora 2
		fr1, fq1 = self.calcFFT(c1, self.fs) # Fourier portadora 1
		fr2, fq2 = self.calcFFT(c2, self.fs) # Fourier portadora 2
		print("tocando audio 1 filtrado")
		xaas = input()
		sd.play(f1_filtrada,self.fs)
		sd.wait()
		print("tocando audio 2 filtrado")
		xaaas = input()
		sd.play(f2_filtrada,self.fs)
		sd.wait()

		# fig2, (ax1,ax2) = plt.subplots(1,2,figsize=(15,5))
		# ax1.plot(fr1,fq1)
		# ax2.plot(fr2,fq2)
		# plt.show()
		self.plotGraph(fr1, fq1, "FOURIER portadora 1")
		self.plotGraph(fr2, fq2, "FOURIER portadora 2")

		modulo1 = f1_filtrada*c1
		modulo2 = f2_filtrada*c2
		fmodulo1,fq1 = self.calcFFT(modulo1, self.fs) # Fourier portadora 1
		fmodulo2,fq2 = self.calcFFT(modulo2, self.fs) # Fourier portadora 2
		# self.plotGraph(fmodulo1,fq1, "Fourier modulada 1")
		# self.plotGraph(fmodulo2,fq2, "Fourier modulada 2")
		xm,ym = self.sumLists(modulo1, modulo2)
		mx,my = self.calcFFT(ym, self.fs) # Fourier portadora 1
		self.plotGraph(mx, my, "FOURIER soma modulado ")


		# print("Clique em um numero para tocar o som")
		# x = input()
		# sd.play(ym, self.fs)
		# sd.wait()


		

		
if __name__ == "__main__":
	transmissor = Transmissor()
	transmissor.main()