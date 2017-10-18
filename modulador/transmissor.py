import sounddevice as sd
import numpy as np
import math 
import matplotlib.pyplot as plt
from scipy import signal


fs = 44100.0

def transformDecibel(list_y):
	new_list = []
	for i in range (len(list_y)):
		a = 10* math.log10(list_y[i]/20000)
		new_list.append(a)
	return new_list

def calcFFT(signal, fs):
	from scipy.fftpack import fft
	from scipy import signal as window

	N  = len(signal)
	T  = 1/fs
	xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
	yf = fft(signal)

	return(xf, np.abs(yf[0:N//2]))

def findFrequencies(X, Y):
	lista_y = []
	lista_x = []
	for i in range (len(Y[0:4000])):
		if Y[i] > -5:
			if Y[i] not in lista_y:
				lista_y.append(Y[i])
				lista_x.append(i)
	return lista_x,lista_y

def audioGenerator(numero):
	t = 3
	x = np.linspace(0,t,fs*t)
	y1= np.sin(2*math.pi*x*numero[0]) + np.sin(2*math.pi*x*numero[1])
   
	sd.play(y1, fs)
	sd.wait()

def graphicGenerator(numero):
	 t = 3
	 x = np.linspace(0,t,fs*t)
	 y1= np.sin(2*math.pi*x*numero[0]) + np.sin(2*math.pi*x*numero[1])
	 plt.clf()
	 plt.plot(x[0:1000], y1[0:1000])
	 plt.xlabel('Angle [rad]')
	 plt.ylabel('sin(x)')
	 plt.axis('tight')
	 plt.show()

	# reproduz o som
	
def fourierGenerator(numero):
	t = 1
	fs = 44100.0
	x = np.linspace(0,t,fs*t)

	y= np.sin(2*math.pi*x*numero[0]) + np.sin(2*math.pi*x*numero[1])
	X, Y = calcFFT(y, fs)
	Y = transformDecibel(Y)
	lista_x,lista_y = findFrequencies(X,Y)

	## Exibe sinal no tempo
	plt.plot(X[0:4000],Y[0:4000])
	plt.grid()
	plt.title('Fourier')
	plt.show()




show = """
TRANSMISSION
	
Choose file:
1 - 2 - 3
-----------------
"""

print(show)
file_chosen = int(input())

# SUBMIT FILE

file_string = './tones/audio'+ str(file_chosen) +'.wav'

show_2 = """
-----------------
Choose frequency 1:
-----------------

"""

print(show_2)
frequency_1 = int(input())

show_3 = """
-----------------	
Choose frequency 2:
-----------------

"""

print(show_3)
frequency_2 = int(input())


y,fs = sf.read(file_string)
fs = float(fs)

# Cacula a trasformada de Fourier do sinal
X, Y = calcFFT(y, fs)
## Exibe sinal no tempo
plt.plot(X[0:4000],Y[0:4000])
plt.grid()
plt.title('Fourier')
plt.show()