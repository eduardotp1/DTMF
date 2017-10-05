import matplotlib
matplotlib.use('TkAgg')

from tkinter import *
import tkinter as tk
import time
from datetime import datetime
from encoderDTMF import audioGenerator
from encoderDTMF import graphicGenerator
import numpy as np

class Janela_Principal():

    def __init__(self):
        self.num_1 = np.array([697,1209])
        self.num_2 = np.array([697,1336])
        self.num_3 = np.array([697,1477])
        self.num_4 = np.array([770,1209])
        self.num_5 = np.array([770,1336])
        self.num_6 = np.array([770,1477])
        self.num_7 = np.array([852,1209])
        self.num_8 = np.array([852,1336])
        self.num_9 = np.array([852,1477])
        self.num_0 = np.array([941,1336])

        self.window=tk.Tk()
        self.window.geometry("200x200+50+50")  
        self.window.title("TELEPHONE")
        self.window.rowconfigure(0, minsize=20,weight=1)
        self.window.rowconfigure(1, minsize=20,weight=1)
        self.window.rowconfigure(2, minsize=20,weight=1)
        self.window.rowconfigure(3, minsize=20 ,weight=1)
        self.window.columnconfigure(0, minsize=20,weight=1)
        self.window.columnconfigure(1, minsize=20,weight=1)
        self.window.columnconfigure(2, minsize=20,weight=1)
        
        self.botao0_0=tk.Button(self.window)
        self.botao0_0.configure(command=lambda: self.botao_clicado(self.num_1), text = "1")
        self.botao0_0.grid(row=0,column=0,sticky='nsew')
        
        self.botao0_1=tk.Button(self.window)
        self.botao0_1.configure(command=lambda: self.botao_clicado(self.num_2), text = "2")
        self.botao0_1.grid(row=0,column=1,sticky='nsew')
        
        self.botao0_2=tk.Button(self.window)
        self.botao0_2.configure(command=lambda: self.botao_clicado(self.num_3), text = "3")
        self.botao0_2.grid(row=0,column=2,sticky='nsew')
        
        self.botao1_0=tk.Button(self.window)
        self.botao1_0.configure(command=lambda: self.botao_clicado(self.num_4), text = "4")
        self.botao1_0.grid(row=1,column=0,sticky='nsew')
        
        self.botao1_1=tk.Button(self.window)
        self.botao1_1.configure(command=lambda: self.botao_clicado(self.num_5), text = "5")
        self.botao1_1.grid(row=1,column=1,sticky='nsew')
        
        self.botao1_2=tk.Button(self.window)
        self.botao1_2.configure(command=lambda: self.botao_clicado(self.num_6), text = "6")
        self.botao1_2.grid(row=1,column=2,sticky='nsew')
        
        self.botao2_0=tk.Button(self.window)
        self.botao2_0.configure(command=lambda: self.botao_clicado(self.num_7), text = "7")
        self.botao2_0.grid(row=2,column=0,sticky='nsew')
        
        self.botao2_1=tk.Button(self.window)
        self.botao2_1.configure(command=lambda: self.botao_clicado(self.num_8), text = "8")
        self.botao2_1.grid(row=2,column=1,sticky='nsew')
        
        self.botao2_2=tk.Button(self.window)
        self.botao2_2.configure(command=lambda: self.botao_clicado(self.num_9), text = "9")
        self.botao2_2.grid(row=2,column=2,sticky='nsew')
        
        self.botao_zero=tk.Button(self.window)
        self.botao_zero.grid(row=3,column=1,sticky='nsew')
        self.botao_zero.configure(text='0',command=lambda: self.botao_clicado(self.num_0),fg='black')
        
        self.label_status=tk.Label()
        self.label_status.configure(text="TIRTOP", font='Arial 20 bold')
        self.label_status.grid(row=4,column=0,columnspan=3)

    def botao_clicado(self,numero):              
        audioGenerator(numero)
        graphicGenerator(numero)

    #Loop do codigo
    def iniciar(self):
        self.window.mainloop()

#Loop do codigo
app = Janela_Principal()
app.iniciar()
