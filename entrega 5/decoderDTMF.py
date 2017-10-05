import sounddevice as sd
import matplotlib.pylab as plt
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy import signal

def calcFFT(signal, fs):
	from scipy.fftpack import fft
	from scipy import signal as window

	N  = len(signal)
	T  = 1/fs
	xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
	yf = fft(signal)

	return(xf, np.abs(yf[0:N//2]))

def findFrequencies(X, Y):
	ay = max(Y)
	index_a, = np.where(Y == ay)
	ax = X[index_a]
	return ax,ay


def animate(i):
	fs = 44100.0
	duration = 1
	audio = sd.rec(int(duration*fs), fs, channels=1)
	y = audio[:,0]
	t = np.linspace(0,1,fs*duration)
	X, Y = calcFFT(y,fs)
	ax1[0].clear()
	ax1[0].plot(t[0:1000],y[0:1000])
	ax1[1].clear()
	ax1[1].plot(X[0:5000],Y[0:5000])


# BEGIN PROGRAM
show = """
DECODER

Submit File : 1
Live: 2
-----------------
Choose option:
"""

print(show)
choose = int(input())


#LIVE DEMO
if choose == 2:
	
	#Plotting
	f, ax1 = plt.subplots(2, sharex=False)
	ani = animation.FuncAnimation(f, animate, interval=1000)
	plt.show()


# SUBMIT FILE
if choose == 1:
	print('''
---------------
Choose Tone
	''')
	tone = input()
	file_string = './tones/dtmf'+ str(tone) +'.wav'


	y,fs = sf.read(file_string)
	fs = float(fs)

	# Cacula a trasformada de Fourier do sinal
	X, Y = calcFFT(y, fs)
	ax,ay = findFrequencies(X,Y) 
	peakind = signal.find_peaks_cwt(Y, np.arange(500,1500))
	print(peakind)
	
	plt.plot([ax],[ay], 'ro')

	


	## Exibe sinal no tempo
	plt.plot(X[0:3000],Y[0:3000])
	plt.grid()
	plt.title('Fourier')
	plt.show()








