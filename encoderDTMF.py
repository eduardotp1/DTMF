import sounddevice as sd
#1
fs = 44100
def audioGenetator():
    
    audio = sd.rec(int(1*fs), fs, channels=1)
    sd.wait()
    
    num_1 = [697,1209]
    num_2 = [697,1336]
    num_3 = [697,1477]
    num_4 = [770,1209]
    num_5 = [770,1336]
    num_6 = [770,1477]
    num_7 = [852,1209]
    num_8 = [852,1336]
    num_9 = [852,1477]
    num_0 = [941,1336]

    y = audio[:,0]

    # reproduz o som
    sd.play(y, fs)

audioGenetator()