import sounddevice as sd
#1
fs = 44100
def audioGenetator():
    
    audio = sd.rec(int(1*fs), fs, channels=1)
    sd.wait()

    y = audio[:,0]

    # reproduz o som
    sd.play(y, fs)

audioGenetator()