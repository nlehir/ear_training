# coding: utf-8
import chords
import player
import id_nm
import frequencies
import sys
from PIL import ImageFont
import random
if sys.version_info < (3, 0):
    import Tkinter as tk
else:
    import tkinter as tk


font_choice_1 = "./Bebas-Regular.ttf"
font_choice_2 = "./Roboto-Condensed.ttf"
font_choice_3 = "./BebasNeue-Regular.ttf"
font = ImageFont.truetype(font_choice_2, 15)

positions = ["RP", "R1", "R2", "R3"]


notes = ['C', 'C#', 'Db', 'D', 'D#',
         'Eb', 'E', 'F', 'F#', 'Gb',
         'G', 'G#', 'Ab', 'A', 'A#',
         'Bb', 'B']

notes_ids = [x for x in range(13)]

colors_note = ["#74b8cc"]

colors_chord = ["#ce7feb",
                "#bc84d1",
                "#de7c91",
                "#db8489",
                "#d69a9e",
                "#bc7dd4"]

colors_chord = ["#68baa8",
                "#7ac4b4",
                "#84d1c0",
                "#6bbfad",
                "#56b39f",
                "#35b095",
                "#2fc4a4",
                "#3bd4b3",
                "#36b59a",
                "#23c2a0"]


arrows = [u"\u2191",
          u"\u2193"]

config_text = (
    "enter : next note & chords     "
    "n : change note     "
    "c : change chords     "
    "p : play chords     "
    "a : play note"
)


class Interface(tk.Frame):
    def __init__(self, fenetre):
        tk.Frame.__init__(self, fenetre)
        # self.grid_propagate(0)
        self.pack(fill=tk.BOTH)
        self.notes_buffer = notes_ids.copy()
        self.note_id = random.randint(0, 12)
        self.note_string = id_nm.id_nm(self.note_id)
        self.note_frequency = frequencies.frequency_from_id(self.note_id)
        self.t3 = False
        self.speed = 2

        fontsize = 50
        width = 10

        # pan 1
        # --------------
        # --------------
        self.pan_1 = tk.Label(self)
        self.pan_1.pack(fill=tk.BOTH)

        self.note = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_note),
            font=(font, fontsize),
            text="Appuyer")
        self.note.pack(side="left")

        self.chord_1 = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_chord),
            font=(font, fontsize),
            text="sur")
        self.chord_1.pack(side="left")

        self.chord_2 = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_chord),
            font=(font, fontsize),
            text="entrée")
        self.chord_2.pack(side="left")

        self.chord_3 = tk.Label(
            self.pan_1,
            width=width,
            height=3,
            bg=random.choice(colors_chord),
            font=(font, fontsize),
            text="!")
        self.chord_3.pack(side="left")
        # --------------
        # --------------

        # pan 2
        # --------------
        # --------------
        self.options = tk.Label(self, bg="#73abf5", width="60")
        self.options.pack(fill="both")

        self.config = tk.Label(
            self.options,
            width=70,
            height=3,
            bg="#73abf5",
            font=(font, 22),
            text=config_text)
        self.config.pack(side="left", fill="both")

        self.h_button = tk.Checkbutton(
            self.options,
            text="t3 mode (h)",
            bg="#ba9027",
            font=(font, 16),
            command=self.toggle_h_mode)
        self.h_button.pack(side=tk.LEFT, fill="both")
        # --------------
        # --------------

    def next_note(self):
        if len(self.notes_buffer) == 0:
            self.notes_buffer = notes.copy()
        next_note = random.choice(self.notes_buffer)
        self.note_id = next_note
        self.note_string = id_nm.id_nm(self.note_id)
        self.note_frequency = frequencies.frequency_from_id(self.note_id)
        self.notes_buffer.remove(next_note)
        self.note["text"] = self.note_string
        self.note["bg"] = random.choice(colors_note)

    def play_note(self):
        """
            cast float to list for convenience
        """
        frequency = [self.note_frequency]
        player.play_sequence(frequency, 1)

    def play_chords(self):
        player.play_sequence(self.freq_seq, self.speed)

    def next_chords(self):
        c1 = chords.Chord(self.t3)
        self.chord_1["text"] = c1.text
        self.chord_1["bg"] = random.choice(colors_chord)

        c3 = chords.Chord(self.t3)
        self.chord_3["text"] = c3.text
        self.chord_3["bg"] = random.choice(colors_chord)

        c2 = chords.Chord(self.t3)
        self.chord_2["text"] = c2.text
        self.chord_2["bg"] = random.choice(colors_chord)

        # generate frequencies sequence
        self.freq_seq = frequencies.frequencies_seq(self.note_id, c1, c2, c3)

    def toggle_h_mode(self):
        self.t3 = not self.t3
        self.h_button.toggle()


def next_note(event):
    interface.next_note()
    interface.play_note()


def play_note(event):
    interface.play_note()


def play_chords(event):
    interface.play_chords()


def next_chords(event):
    interface.next_chords()


def next_all(event):
    interface.next_note()
    interface.next_chords()
    interface.play_note()


def switch_h_mode(event):
    interface.toggle_h_mode()


def quit_ex(event):
    interface.quit()


fenetre = tk.Tk()
interface = Interface(fenetre)
fenetre.bind('<Return>', next_all)
fenetre.bind('<n>', next_note)
fenetre.bind('<c>', next_chords)
fenetre.bind('<p>', play_chords)
fenetre.bind('<h>', switch_h_mode)
fenetre.bind('<a>', play_note)
fenetre.bind('<q>', quit_ex)
interface.mainloop()
