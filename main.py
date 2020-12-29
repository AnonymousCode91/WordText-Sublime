# -*- coding: utf-8 -*-
# Importation des bibliothèques nécessaires
# http://www.xavierdupre.fr/app/teachpyx/helpsphinx/c_gui/tkinter.html#zone-de-texte
# https://www.youtube.com/watch?v=ENP2gslQVXk&t=41s

from tkinter import * 
import tkinter as tk
from tkinter import filedialog 
import string
import time
import os 


windows = Tk()
frame = Frame(windows)


windows.title("                                                                                                 📖  WordText Sublime  📖")
windows.geometry("880x450")
windows.tk.call(
  'wm', 
  'iconphoto', 
  windows._w, 
  tk.PhotoImage(file="icone.ico")
)

# la zone de texte
saisie = Text()
pos = "0.0"
saisie.config (width = 200, height = 500)
saisie.insert (pos, "")
saisie.pack()

def new():
    os.popen("main.py")

def sortie():
    windows.quit()

def style():
  windows = Tk()
  frame = Frame(windows)
  windows.title("📖 Préférence 📖")
  windows.geometry("280x250")

  texte = Label (frame, text="Police d'écriture :", font=("Consolas", 9))
  texte.pack()
  texte = Label (frame, text="", font=("Consolas", 8))
  texte.pack()
  case=tk.Checkbutton(frame,text="Consolas")
  case.pack()
  case=tk.Checkbutton(frame,text="Arial")
  case.pack()
  case=tk.Checkbutton(frame,text="Comic Sans M")
  case.pack()
  texte = Label (frame, text="", font=("Consolas", 8))
  texte.pack()
  bouton= Button(frame,text="OK")
  bouton.pack()

  frame.pack(expand=YES)
  windows.mainloop()
  
# menu
menu_bar = Menu(windows)

file_menu = Menu (menu_bar, tearoff=0)
file_menu2 = Menu (menu_bar, tearoff=0)
file_menu3 = Menu (menu_bar, tearoff=0)
file_menu4 = Menu (menu_bar, tearoff=0)
file_menu5 = Menu (menu_bar, tearoff=0)

menu_bar.add_cascade(label="Fichier", menu=file_menu)
file_menu.add_command(label="Nouveau", command=new)
file_menu.add_command(label="Quitter", command=sortie)

menu_bar.add_cascade(label="Edition", menu=file_menu2)
file_menu2.add_command(label="Préférence(s)", command=style)

windows.config(menu=menu_bar)
frame.pack(expand=YES)
windows.mainloop()