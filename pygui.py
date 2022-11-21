import pyautogui
from keras.models import load_model
import numpy as np
from tkinter import * 
import time

model = load_model('CNN_1.h5')
emg=np.loadtxt('exampMini.csv',delimiter=',')
emg = emg.reshape((1,4,512*7))
out = model.predict(emg)

time.sleep(0.1)
type(out), out.shape
    
out = model.predict(emg)
defi = out[0,0]

if(defi <0.5):
    pyautogui.moveTo(100,100,duration=1)
else:
    pyautogui.moveTo(100,1000,duration=1)

root = Tk()
root.title("Cursors")
root.geometry("500x500")

import os

os.system("gsettings set  org.gnome.desktop.interface cursor-theme 'redglass'")
os.system("gsettings set  org.gnome.desktop.interface cursor-theme 'DMZ-White'")
os.system("gsettings set  org.gnome.desktop.interface cursor-theme 'default'")

os.system("gsettings set  org.gnome.desktop.interface cursor-size 24")

# print("gsettings set  org.gnome.desktop.interface cursor-theme 'DMZ-Black'")
