import sounddevice as sd
import numpy as np
import math 
import matplotlib.pyplot as plt

fs = 44100
def audioGenerator(numero):
    
    
    t = 0.4
    x = np.linspace(0,t,fs*t)
    y1= np.sin(2*math.pi*x*numero[0]) + np.sin(2*math.pi*x*numero[1])
   
    sd.play(y1, fs)
    sd.wait()

def graphicGenerator(numero):
     t = 0.5
     x = np.linspace(0,t,fs*t)
     y1= np.sin(2*math.pi*x*numero[0]) + np.sin(2*math.pi*x*numero[1])
     plt.clf()
     plt.plot(x[0:1000], y1[0:1000])
     plt.xlabel('Angle [rad]')
     plt.ylabel('sin(x)')
     plt.axis('tight')
     plt.show()

    # reproduz o som
    


