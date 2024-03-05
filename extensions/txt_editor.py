#Editeur de cheats (Simple Text Editor)
#1.0
#Team EmuKit
#-- ^ INFORMATIONS SUR L'EXTENSION ^ --
from tkinter import ttk
import tkinter as tk
import pyautogui
import sys
import os
from tkinter.messagebox import showerror, showinfo, showwarning

window = tk.Tk()
version = 1.0

window.title("Editeur de cheats")
window.resizable(False, False)
window.geometry("400x500")

menubar = tk.Menu()
file_menu = tk.Menu(tearoff=0)
edit_menu = tk.Menu(tearoff=0)
help_menu = tk.Menu(tearoff=0)

menubar.add_cascade(menu=file_menu, label="Fichier")
menubar.add_cascade(menu=edit_menu, label="Edition")
menubar.add_cascade(menu=help_menu, label="?")

file_menu.add_command(label="Nouveau fichier", state="disabled")
file_menu.add_command(label="Ouvrir un fichier")
file_menu.add_separator()
file_menu.add_command(label="Sauvegarder")
file_menu.add_command(label="Sauvegarder sous", state="disabled")
file_menu.add_separator()
file_menu.add_command(label="Fermer l'éditeur de cheats", command=lambda:(sys.exit()))

edit_menu.add_command(label="Annuler")
edit_menu.add_command(label="Rétablir")
edit_menu.add_separator()
edit_menu.add_command(label="Tout sélectionner")
edit_menu.add_command(label="Copier")
edit_menu.add_command(label="Coller")

help_menu.add_command(label="A propos", command=lambda:(showinfo("A propos", f"Simple Text Editor, version {version}. Développé par Luckyluka17 et Team EmuKit.")))

text_area = tk.Text(
    window,
)
text_area.pack(fill="y", side="left")


window.config(menu=menubar)
window.mainloop()