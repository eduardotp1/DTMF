import sounddevice as sd
import matplotlib.pylab as plt
import numpy as np
import sched, time
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.fftpack import fft
from scipy import signal as window
import soundfile as sf


fs = 44100.0
T  = 1.0/fs
N = 1000
#Plotting
duration = 1

f, ax1 = plt.subplots(2, sharex=False)

def calcFFT(signal, fs):
	from scipy.fftpack import fft
	from scipy import signal as window

	N  = len(signal)
	T  = 1/fs
	xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
	yf = fft(signal)
	return(xf, np.abs(yf[0:N//2]))


def animate(i):
	fs = 44100.0
	audio = sd.rec(int(duration*fs), fs, channels=1)
	y = audio[:,0]
	t = np.linspace(0,1,fs*duration)
	X, Y = calcFFT(y,fs)
	ax1[0].clear()
 	ax1[0].plot(t[0:1000],y[0:1000])
	ax1[1].clear()
 	ax1[1].plot(X,Y)

    
    
ani = animation.FuncAnimation(f, animate, interval=1000)

plt.show()




