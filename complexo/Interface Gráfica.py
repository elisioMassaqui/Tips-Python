import tkinter as tk
from tkinter import ttk
import serial

arduino = serial.Serial(port='COM19', baudrate=9600, timeout=.1)

def send_angle(angle, joint):
    command = f'{joint}:{angle}'
    arduino.write(bytes(command, 'utf-8'))

def update_joint1(val):
    send_angle(val, 1)

def update_joint2(val):
    send_angle(val, 2)

root = tk.Tk()
root.title("Controle de Robô")

joint1_slider = ttk.Scale(root, from_=0, to=180, command=update_joint1)
joint1_slider.pack()

joint2_slider = ttk.Scale(root, from_=0, to=180, command=update_joint2)
joint2_slider.pack()

root.mainloop()
