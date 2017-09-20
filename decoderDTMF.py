import sounddevice as sd
import matplotlib.pylab as plt
import numpy as np
import sched, time
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cPickle as pickle


fs = 44100

#Plotting
duration = 1

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
plt.xlabel('Time')
plt.ylabel('sin(x)')

def animate(i):
    audio = sd.rec(int(1*fs), fs, channels=1)
    xar = []
    yar = []
    y = audio[:,0]
    t = np.linspace(0,1,fs*duration)    
    # with open('number1.p', 'w+') as f:
    #     pickle.dump(audio, f)
    
    ax1.clear()
    ax1.plot(t[0:1000],y[0:1000])
    
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

