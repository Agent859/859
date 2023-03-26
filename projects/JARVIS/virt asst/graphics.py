import threading
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from itertools import count, cycle

def image(pic):
    canvas = Canvas(width = 300, height = 200, bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    gif1 = PhotoImage(file = pic)
    canvas.create_image(50, 10, image = gif1, anchor = NW)
    mainloop()

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        image("D:\Projects\jarvis\Jarvis Tk Color\blue J.A.R.V.I.S.gif")

def app():
    App()

root=Tk()
def jprint(text_var):
    root.geometry("700x500")
    txt=StringVar()
    txt.set(text_var)
    my_entry=Entry(root, bd=0, state="readonly", textvariable=txt)
    my_entry.pack(fill="both")