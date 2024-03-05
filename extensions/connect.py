#Compte MultiMod
#1.0
#Team EmuKit
#-- ^ INFORMATIONS SUR L'EXTENSION ^ --
from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import showinfo, showerror, showwarning
import os

window = tk.Tk()

window.title("Connexion")
window.geometry("300x130")
window.resizable(False, False)

frame = ttk.Frame(
    window
)
frame.pack()

ttk.Label(
    frame,
    text="Adresse-mail",
    font=("Calibri", 13)
).grid(row=0, column=0, padx=5, pady=10)

ttk.Entry(
    frame,
    width=16,
    font=("Calibri", 13)
).grid(row=0, column=1, padx=5, pady=10)

ttk.Label(
    frame,
    text="Mot de passe",
    font=("Calibri", 13)
).grid(row=1, column=0, padx=5, pady=5)

ttk.Entry(
    frame,
    width=16,
    show="*",
    font=("Calibri", 13)
).grid(row=1, column=1, padx=5, pady=5)

ttk.Button(
    frame,
    text="Me connecter",
    cursor="hand2"
).grid(row=2, column=0, padx=5, pady=10)

ttk.Button(
    frame,
    text="Mot de passe oublié",
    cursor="hand2"
).grid(row=2, column=1, padx=5, pady=10)

window.mainloop()