# coding: utf-8
import sys
import random
if sys.version_info < (3, 0):
    import Tkinter as tk
else:
    import tkinter as tk


notes = ['C', 'C#', 'Db', 'D', 'D#',
         'Eb', 'E', 'F', 'F#', 'Gb',
         'G', 'G#', 'Ab', 'A', 'A#',
         'Bb', 'B']


class Interface(tk.Frame):
    def __init__(self, fenetre):
        color = "#6596e6"
        tk.Frame.__init__(self,
                          fenetre)
        self.grid_propagate(0)
        self.pack(fill=tk.BOTH)

        self.texte_principal = tk.Label(
            self,
            width=20,
            height=3,
            bg=color,
            font=("Symbol", 60),
            text="Appuyer sur enter")
        self.texte_principal.pack()

    def next_note(self):
        self.texte_principal["text"] = random.choice(notes)


def next_ex(event):
    interface.next_note()


def quit_ex(event):
    interface.quit()


fenetre = tk.Tk()
interface = Interface(fenetre)
fenetre.bind('<Return>', next_ex)
fenetre.bind('<q>', quit_ex)
interface.mainloop()
