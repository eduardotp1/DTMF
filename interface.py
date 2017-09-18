import matplotlib
matplotlib.use('TkAgg')

from Tkinter import *
import Tkinter as tk
import time
from datetime import datetime
from PIL import ImageTk, Image


class Janela_Principal():

    def __init__(self):

        self.window=tk.Tk()
        self.window.geometry("400x500+500+500")  
        self.window.title("TELEPHONE")
        self.window.rowconfigure(0, minsize=100,weight=1)
        self.window.rowconfigure(1, minsize=100,weight=1)
        self.window.rowconfigure(2, minsize=100,weight=1)
        self.window.rowconfigure(3, minsize=100 ,weight=1)
        self.window.columnconfigure(0, minsize=100,weight=1)
        self.window.columnconfigure(1, minsize=100,weight=1)
        self.window.columnconfigure(2, minsize=100,weight=1)
    
        
        
        
        self.botao0_0=tk.Button(self.window)
        self.botao0_0.configure(command=None, text = "1")
        self.botao0_0.grid(row=0,column=0,sticky='nsew')
        
        
        self.botao0_1=tk.Button(self.window)
        self.botao0_1.configure(command=None, text = "2")
        self.botao0_1.grid(row=0,column=1,sticky='nsew')
        
        self.botao0_2=tk.Button(self.window)
        self.botao0_2.configure(command=None, text = "3")
        self.botao0_2.grid(row=0,column=2,sticky='nsew')
        
        self.botao1_0=tk.Button(self.window)
        self.botao1_0.configure(command=None, text = "4")
        self.botao1_0.grid(row=1,column=0,sticky='nsew')
        
        self.botao1_1=tk.Button(self.window)
        self.botao1_1.configure(command=None, text = "5")
        self.botao1_1.grid(row=1,column=1,sticky='nsew')
        
        self.botao1_2=tk.Button(self.window)
        self.botao1_2.configure(command=None, text = "6")
        self.botao1_2.grid(row=1,column=2,sticky='nsew')
        
        self.botao2_0=tk.Button(self.window)
        self.botao2_0.configure(command=None, text = "7")
        self.botao2_0.grid(row=2,column=0,sticky='nsew')
        
        self.botao2_1=tk.Button(self.window)
        self.botao2_1.configure(command=None, text = "8")
        self.botao2_1.grid(row=2,column=1,sticky='nsew')
        
        self.botao2_2=tk.Button(self.window)
        self.botao2_2.configure(command=None, text = "9")
        self.botao2_2.grid(row=2,column=2,sticky='nsew')
        
        self.botao_reiniciar=tk.Button(self.window)
        self.botao_reiniciar.grid(row=3,column=1,sticky='nsew')
        self.botao_reiniciar.configure(text='0',command=None,fg='black')
        
        self.label_status=tk.Label()
        self.label_status.configure(text="TIRTOP", font='Arial 20 bold')
        self.label_status.grid(row=4,column=0,columnspan=3)

    #Loop do codigo
    def iniciar(self):
        self.window.mainloop()

    

#Loop do codigo
app = Janela_Principal()
app.iniciar()
