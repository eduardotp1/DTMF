import sounddevice as sd
import matplotlib.pylab as plt
import numpy as np


def audioListener():
    
    #Plotting
    x = np.linspace(-np.pi, np.pi, 201)
    plt.plot(x, np.sin(x))
    plt.xlabel('Angle [rad]')
    plt.ylabel('sin(x)')
    plt.axis('tight')
    plt.show()

audioListener()